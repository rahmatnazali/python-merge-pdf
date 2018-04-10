import PyPDF2
import datetime, time

class PDFMerger():

    def __init__(self):
        self.pdfWriter = PyPDF2.PdfFileWriter()
        self.pdfInputPointer = None

    def generateFileName(self):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H_%M_%S')
        return 'result/combined_' + timestamp + '.pdf'

    def mergePDF(self, fileList):
        for file in fileList:
            self.pdfInputPointer = open(file, 'rb')
            print('merging', file, ': ', self.pdfInputPointer.__sizeof__(), 'kb')
            pdfReader = PyPDF2.PdfFileReader(self.pdfInputPointer)

            for pageNumber in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNumber)
                self.pdfWriter.addPage(pageObj)

        pdfOutputFile = open(self.generateFileName(), 'wb')
        print('final file:', pdfOutputFile.__sizeof__())
        self.pdfWriter.write(pdfOutputFile)
        print('final file:', pdfOutputFile.__sizeof__())
        pdfOutputFile.close()
        self.pdfInputPointer.close()


if __name__ == '__main__':
    print('main')
    pdfMergerInstance = PDFMerger()
    pdfMergerInstance.mergePDF([
        'pdf-sample_1.pdf',
        'pdf-sample_2.pdf',
        'pdf-sample_3.pdf',
        'scan0003.pdf',
        'scan0004.pdf',
        'scan0005.pdf',
    ])

    # workingCode()