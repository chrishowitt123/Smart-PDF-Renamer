import fitz
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk import Text
import pandas as pd


pdf_document = "pdf-sample.pdf"
doc = fitz.open(pdf_document)
print ("number of pages: %i" % doc.pageCount)
print(doc.metadata)

page = doc.loadPage(0)
pagetext = page.getText("text")

    
textList = Text(tokens)
list(page1text)
tokens = sent_tokenize(page1text)    
tokens = [t.replace('\n', ', ') for t in tokens]
tokens = str(tokens)
tokens_list = tokens.split(",")

items = pd.DataFrame(tokens_list)

items.columns = ['Info']

Company_name = items.loc[6]
Responsible = items.loc[19]

Company_name = str(Company_name).replace('\nName:', '')
Responsible = str(Responsible).replace('\nName:', '')
Company_name + Responsible
