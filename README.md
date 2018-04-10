# python-merge-pdf
Simple script to merge several pdf files written in pure python

# Usage

```
python merge.py <pdf_directory> [first.pdf] [second.pdf] [third.pdf] ...
```

1. Merge specified files by giving it as the parameter
```
>>> python merge.py target pdf_sample_1.pdf pdf_sample_2.pdf pdf_sample_3.pdf
- Python PDF Merger -
Merging specified files
        merging target/pdf_sample_1.pdf :  7.945 kb
        merging target/pdf_sample_2.pdf :  433.994 kb
        merging target/pdf_sample_3.pdf :  54.836 kb
exported result/combined_2018-04-10 11_24_13.pdf : 485.462 kb
```

2. Merge all of the PDF Files inside specified directory by ommiting the file parameters
```
>>> python merge.py target
- Python PDF Merger -
Merging all PDF files in the directory: target/
        merging target/pdf_sample_1.pdf :  7.945 kb
        merging target/pdf_sample_2.pdf :  433.994 kb
        merging target/pdf_sample_3.pdf :  54.836 kb
        merging target/pdf_sample_4.pdf :  3.028 kb
exported result/combined_2018-04-10 11_01_19.pdf : 487.898 kb
```

# Requirements
1. [Python 3](https://www.python.org/download/releases/3.0/)
2. [PyPDF2](https://pypi.python.org/pypi/PyPDF2)


# Acknowledgements
Source of the PDF example files:
- [sample_pdf_1.pdf](http://www.africau.edu/images/default/sample.pdf)
- [sample_pdf_2.pdf](http://www.pdf995.com/samples/pdf.pdf)
- [sample_pdf_3.pdf](http://unec.edu.az/application/uploads/2014/12/pdf-sample.pdf)
- [sample_pdf_4.pdf](http://gahp.net/wp-content/uploads/2017/09/sample.pdf)