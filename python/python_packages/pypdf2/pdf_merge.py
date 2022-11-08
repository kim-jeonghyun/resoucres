import argparse
from glob import glob
import os

from PyPDF2 import PdfFileMerger

def main(book_title, directory=".", sub_dir='merged'):
    """
    book_title과 directory, sub_dir를 받으면 directory내에 있는 book_title로 시작하는 이름의 pdf 파일들을 하나로 합쳐 sub_dir 하에 book_title.pdf 형태로 저장하는 함수
    """

    merger = PdfFileMerger()

    for f in sorted(glob(f"{directory}/{book_title}*.pdf")):
        merger.append(f)

    os.chdir(directory)
    if not os.path.isdir(sub_dir):
        os.mkdir(sub_dir)

    merger.write(f"{directory}/{sub_dir}/{book_title}.pdf")
    merger.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="directory where files to be merged")
    parser.add_argument("bookname")
    args = parser.parse_args()
    directory = args.directory
    bookname = args.bookname

    main(args.bookname, args.directory)