import pdfplumber
import PyPDF2

def textFromPdf(pdf_file):
    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pages = pdfReader.numPages

    alltextlist = []

    with pdfplumber.open(pdf_file) as pdf:
        # Loop through the number of pages
        for i in range(0, pages):
            page = pdf.pages[i]
            text = page.extract_text()
            alltextlist.append(text)

    pdfText = ','.join(alltextlist)

    pdfText = pdfText.replace("\n", "")
    pdfText = pdfText.replace("'", "")
    pdfText = pdfText.replace('"', "")
    pdfText = pdfText.replace("|", "")
    pdfText = pdfText.replace(":", "")
    pdfText = pdfText.replace(";", "")
    pdfText = pdfText.replace("–", "")
    pdfText = pdfText.replace("\uf0b7", "")

    return pdfText

# pdfFile = 'static/files/TestPDF.pdf'
# pdfText = textFromPdf(pdfFile)
# print(pdfText)