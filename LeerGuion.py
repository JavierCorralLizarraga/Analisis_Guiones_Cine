# -*- coding: utf-8 -*-

# Utilizamos pdfminer.six para extraer el texto de los pdfs con guiones
from pdfminer.high_level import extract_text

peli='Roma'
text = extract_text(peli + '.pdf')
print(text)
with open(peli+'.txt', 'w') as f:
    print('Filename:', text, file=f) 
