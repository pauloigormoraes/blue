import csv
from nltk.stem import rslp
# nltk.download('rslp')
import unicodedata

a__ifile = csv.reader(open('/home/paulomoraes/Projects/lise/creep/data/prepared/t_stopwords/wcat-a.csv', 'r'))
a__ofile = open('/home/paulomoraes/Projects/lise/creep/data/prepared/t_stemming/scat-a.csv', 'w')

b__ifile = csv.reader(open('/home/paulomoraes/Projects/lise/creep/data/prepared/t_stopwords/wcat-b.csv', 'r'))
b__ofile = open('/home/paulomoraes/Projects/lise/creep/data/prepared/t_stemming/scat-b.csv', 'w')

c__ifile = csv.reader(open('/home/paulomoraes/Projects/lise/creep/data/prepared/t_stopwords/wcat-c.csv', 'r'))
c__ofile = open('/home/paulomoraes/Projects/lise/creep/data/prepared/t_stemming/scat-c.csv', 'w')

def stemming(document):
    words = document.split()
    stm = []
    for word in words:
        stm.append(rslp.RSLPStemmer().stem(word))
        tprepared = (' '.join(stm))

    return tprepared

for row in a__ifile:
    for value in row:
        docw = stemming(value)
        a__ofile.write(docw)
        a__ofile.write('\n')

for row in b__ifile:
    for value in row:
        docw = stemming(value)
        b__ofile.write(docw)
        b__ofile.write('\n')

for row in c__ifile:
    for value in row:
        docw = stemming(value)
        c__ofile.write(docw)
        c__ofile.write('\n')

print('********* PREPARED STEMMING *********')
