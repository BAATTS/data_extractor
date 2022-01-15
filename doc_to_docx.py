from glob import glob
import re
import os
import win32com.client as win32
from win32com.client import constants
from bookmark_data_to_text import bookmark_data_to_text


# Create list of paths to .doc files
paths = glob('I:\\PycharmProjects\\data_extractor\\files\\*.doc', recursive=True)

for files in paths:
    if files.endswith('.doc'):
        # Opening MS Word
        word = win32.gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(files)

        doc.Activate()

        # Rename path with .docx
        new_file_abs = os.path.abspath(files)
        new_file_abs = re.sub(r'\.\w+$', '.docx', new_file_abs)

        # Save and Close
        word.ActiveDocument.SaveAs(
            new_file_abs, FileFormat=constants.wdFormatXMLDocument
        )
        doc.Close(False)

        bookmark_data_to_text()
