import PyPDF2
import datetime, time, os

class PDFMerger():
    def __init__(self):
        self.pdfWriter = PyPDF2.PdfFileWriter()
        self.pdfInputPointers = []
        self.totalByteMerged = 0

    def generateFileName(self, export_directory = ''):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H_%M_%S')
        if export_directory != '':
            return export_directory + '/' + 'combined_' + timestamp + '.pdf'
        else:
            return 'result/combined_' + timestamp + '.pdf'

    def mergePDF(self, fileList):

        try:
            # open all PDF files
            for file in fileList:
                if os.path.isfile(file):
                    self.pdfInputPointers.append(open(file, 'rb'))
                    print('\tmerging', file, ': ', os.stat(file).st_size/1000, 'kb')
                    self.totalByteMerged += os.stat(file).st_size
                else:
                    print('\t[Error]', file, 'did not exist and will be skipped')

            # read all the data
            for filePointer in self.pdfInputPointers:
                pdfReader = PyPDF2.PdfFileReader(filePointer)

                for pageNumber in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(pageNumber)
                    self.pdfWriter.addPage(pageObj)


            # write to a new PDF File
            if self.totalByteMerged == 0:
                print('No files merged.')
            else:
                outputFileName = self.generateFileName()
                with open(outputFileName, 'wb') as pdfOutputFile:
                    self.pdfWriter.write(pdfOutputFile)
                print('exported', outputFileName, ':', os.stat(outputFileName).st_size/1000, 'kb')

            # close all file pointer
            for filePointer in self.pdfInputPointers:
                filePointer.close()

        except Exception as exception:
            print(exception)
