# -*- coding:utf-8*-


import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import time


def getFileName(filedir):

    file_list = [os.path.join(root, filespath) \
                 for root, dirs, files in os.walk(filedir) \
                 for filespath in files \
                 if str(filespath).endswith('pdf')
                 ]
    return file_list if file_list else []

def MergePDF(filepath, outfile):

    output = PdfFileWriter()
    outputPages = 0
    pdf_fileName = getFileName(filepath)

    if pdf_fileName:
        for pdf_file in pdf_fileName:
            print("dir：%s"%pdf_file)


            input = PdfFileReader(open(pdf_file, "rb"))

            
            pageCount = input.getNumPages()
            outputPages += pageCount
            print("number_pages：%d"%pageCount)

   
            for iPage in range(pageCount):
                output.addPage(input.getPage(iPage))

        print("all_pages:%d."%outputPages)
        # 写入到目标PDF文件
        outputStream = open(os.path.join(filepath, outfile), "wb")
        output.write(outputStream)
        outputStream.close()
        print("merge done")

    else:
        print("no .pdf files")

def main():
    time1 = time.time()
    file_dir = r'./pdf' 
    outfile = "merge.pdf" 
    MergePDF(file_dir, outfile)
    # size_of_pdf(file_dir)
    time2 = time.time()
    print('times：%s s.' %(time2 - time1))

main()
