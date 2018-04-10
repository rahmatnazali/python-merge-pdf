import PyPDF2
import datetime, time, os

class PDFMerger():

    def __init__(self):
        self.pdfWriter = PyPDF2.PdfFileWriter()
        self.pdfInputPointers = []

    def generateFileName(self):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H_%M_%S')
        return 'result/combined_' + timestamp + '.pdf'

    def mergePDF(self, fileList):
        # todo: add exception if file not exist

        # open all PDF files
        for file in fileList:
            self.pdfInputPointers.append(open(file, 'rb'))
            print('\tmerging', file, ': ', os.stat(file).st_size/1000, 'kb')

        # read all the data
        for filePointer in self.pdfInputPointers:
            pdfReader = PyPDF2.PdfFileReader(filePointer)

            for pageNumber in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNumber)
                self.pdfWriter.addPage(pageObj)

        # write to a new PDF File
        outputFileName = self.generateFileName()
        with open(outputFileName, 'wb') as pdfOutputFile:
            self.pdfWriter.write(pdfOutputFile)
            print('exported', outputFileName, ':', os.stat(outputFileName).st_size/1000, 'kb')

        # close all file pointer
        for filePointer in self.pdfInputPointers:
            filePointer.close()

if __name__ == '__main__':
    print('Python PDF Merger')
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