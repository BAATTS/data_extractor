# Extracting bookmarks from doc. and docx files 
I created two python scripts:

# doc_to_docx.py
This scripts handles conversion from old doc files to docx files. The idea behind converting
them is to take advantage of the XML format of newer docx files.

# bookmark_data_to_text.py
This script now takes in the converted docx file to extract the bookmark data onto a text file.
More formatting for this would be nice to have when it outputs the bookmark data.

# Notes:
The file paths are specific to my machine so they would need to be configured to individual
machine.
The end goal: to run these on a website, hence why they are split.

# Example Commands:
- python bookmark_data_to_text.py
- python doc_to_docx.py
