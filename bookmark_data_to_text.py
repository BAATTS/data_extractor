import glob
import os
import zipfile
import re
import json
import docx
from docx.oxml.shared import qn
from lxml import etree

dictionary = {}
bookmark_data = []
base_path = 'files'
saved_data = 'data'
complete_saved_data = os.path.join(saved_data, 'bookmarks_data.txt')
regex_for_price = '<w:t>(\\$[0-9]+,[0-9]+)</w:t>'
path = glob.glob("I:\\PycharmProjects\\data_extractor\\files\\*.docx")


def bookmark_data_to_text():
    global dollar_amounts
    for files in path:
        document = docx.Document(files)
        doc_element = document.part._element
        bookmark_list = doc_element.xpath(".//w:bookmarkStart")

        documentZip = zipfile.ZipFile(files)
        xml_content = documentZip.read('word/document.xml')
        documentZip.close()

        xml_str_object = xml_content
        root = etree.fromstring(xml_str_object)
        xml_string = str(xml_str_object)

        dollar_amounts = re.findall(regex_for_price, xml_string)

        for bookmark in bookmark_list:
            name = bookmark.get(qn('w:name'))
            par = bookmark.getparent()
            runs = par.findall(qn('w:r'))

            bookmark_data = []
            dictionary[name] = bookmark_data

            for run in runs:
                try:
                    dictionary[name].append(run.find(qn('w:t')).text)
                    json_object = json.dumps(bookmark_data, indent=4)
                    with open(complete_saved_data, 'w') as file:
                        file.write(str(json_object) + '\n')
                except Exception as e:
                    pass

    dictionary['INVESTMENT'].append(dollar_amounts)
    json_object = json.dumps(dictionary, indent=4)
    with open(complete_saved_data, 'w') as file:
        file.write(str(json_object) + '\n')
