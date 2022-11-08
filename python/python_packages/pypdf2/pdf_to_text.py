from PyPDF2 import PdfReader
import argparse
from glob import glob
import os
from io import StringIO


# for test

def pdf_to_text_by_pypdf2(directory="."):
    for f in sorted(os.listdir(directory)):
        if f[-3:] == 'pdf':
            print(f)
            reader = PdfReader(directory+f)
            text = str()

            for index in range(len(reader.pages)):
                page = reader.pages[index]
                text += page.extract_text()
                # print(text)
            with open(f"{directory}/{f[:-4]}.txt", "w") as text_file:
                text_file.write(text)
            text_file.close()
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="directory where files to be merged")
    args = parser.parse_args()
    directory = args.directory
    pdf_to_text_by_pypdf2(args.directory)

