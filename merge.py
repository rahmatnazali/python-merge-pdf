import Core, sys, os

def printUsage():
    print("""
    Usage

    1. To merge all PDF files on a certain directory
        merge.py [your_directory_target]
    2. To merge certain specified files
        merge yout_first.pdf your_second.pdf [your_third.pdf] ...

    """)

if __name__ == '__main__':

    print('- Python PDF Merger -')

    if len(sys.argv) == 1:
        printUsage()
    elif len(sys.argv) == 2:
        print('Merging all PDF files in the directory:', sys.argv[1] + '/')
        pdfFiles = [sys.argv[1] + '/' + pdfFile for pdfFile in os.listdir(sys.argv[1]) if pdfFile.endswith('.pdf')]
        pdfMergerInstance = Core.PDFMerger()
        pdfMergerInstance.mergePDF(pdfFiles)
    elif len(sys.argv) > 2:
        print('Merging specified files')
        pdfFiles = [sys.argv[1] + '/' + pdfFile for pdfFile in sys.argv[2:] if pdfFile.endswith('.pdf')]
        pdfMergerInstance = Core.PDFMerger()
        pdfMergerInstance.mergePDF(pdfFiles)