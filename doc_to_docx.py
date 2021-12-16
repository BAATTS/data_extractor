from glob import glob
import re
import os
import win32com.client as win32
from win32com.client import constants


# Create list of paths to .doc files
paths = glob('C:\\Users\\JORGE\\Documents\\word_files\\*.doc', recursive=True)
word = 'quote example.docx'


# Convert old .doc files to .docx
def save_as_docx(path):
    # Opening MS Word
    word = win32.gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(path)

    doc.Activate()

    # Rename path with .docx
    new_file_abs = os.path.abspath(path)
    new_file_abs = re.sub(r'\.\w+$', '.docx', new_file_abs)

    # Save and Close
    word.ActiveDocument.SaveAs(
        new_file_abs, FileFormat=constants.wdFormatXMLDocument
    )
    doc.Close(False)


for files in paths:
    if files.endswith('.doc'):
        save_as_docx(files)
