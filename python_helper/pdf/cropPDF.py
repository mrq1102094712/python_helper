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

def size_of_pdf(filepath):

    output = PdfFileWriter()
    outputPages = 0
    pdf_fileName = getFileName(filepath)

    A4_width = 595.32
    A4_high = 841.92
    if pdf_fileName:
        for pdf_file in pdf_fileName:
            print("路径：%s"%pdf_file)

            # 读取源PDF文件
            input = PdfFileReader(open(pdf_file, "rb"))

            pageCount = input.getNumPages()
            writerObj = PdfFileWriter()
            # outputPages += pageCount
            for iPage in range(pageCount):

                page = input.getPage(iPage)

                old_width = input.getPage(iPage).mediaBox.getUpperRight_x()
                old_high = input.getPage(iPage).mediaBox.getUpperRight_y()
                # print(input.getPage(0).mediaBox)
                print(old_width, old_high)
                if old_high != A4_high or old_width != A4_width:
                    page.cropBox.setLowerLeft((0, 0))
                    page.cropBox.setLowerRight((595.32, 0))
                    page.cropBox.setUpperLeft((0, 841.92))
                    page.cropBox.setUpperRight((595.32, 841.92))
                    writerObj.addPage(page)
                new_width = input.getPage(iPage).mediaBox.getUpperRight_x()
                new_high = input.getPage(iPage).mediaBox.getUpperRight_y()
                print(new_width, new_high)

        outstream = open('./croped.pdf', 'wb')
        writerObj.write(outstream)
        outstream.close()
        print('crop succeed!')
    else:
        print(pdf_fileName)



file_dir = r'./croppdf'

size_of_pdf(file_dir)