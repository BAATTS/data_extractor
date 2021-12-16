import docx
import os
from docx.oxml.shared import qn
from docx import Document

base_path = 'quote example.docx'

document = docx.Document(base_path)
doc_element = document.part._element
bookmark_list = doc_element.xpath(".//w:bookmarkStart")
bookmark_text = []
for bookmark in bookmark_list:
    par = bookmark.getparent()
    runs = par.findall(qn('w:r'))
    for run in runs:
        try:
            print(' ', run.find(qn('w:t')).text, end=' ')
            bookmark_text.append(run.find(qn('w:t')).text)
            with open('bookmarks_data.txt', 'w') as file:
                file.write(str(bookmark_text) + '\n')
        except:
            pass
            print('\n', '-' * 10)


