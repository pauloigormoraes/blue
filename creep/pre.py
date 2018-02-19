import csv
import re as rexpression
from nltk.corpus import stopwords
from nltk.stem import rslp
# nltk.download('stopwords')
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import tempfile
from string import punctuation
import unicodedata
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

fp = tempfile.TemporaryFile(mode='w+t')

a__ifile = csv.reader(open('/home/paulomoraes/Projects/lise/creep/data/organized/cat-a.csv', 'r'))
a__ofile = open('/home/paulomoraes/Projects/lise/creep/data/prepared/cat-a.csv', 'w')

b__ifile = csv.reader(open('/home/paulomoraes/Projects/lise/creep/data/organized/cat-b.csv', 'r'))
b__ofile = open('/home/paulomoraes/Projects/lise/creep/data/prepared/cat-b.csv', 'w')

c__ifile = csv.reader(open('/home/paulomoraes/Projects/lise/creep/data/organized/cat-c.csv', 'r'))
c__ofile = open('/home/paulomoraes/Projects/lise/creep/data/prepared/cat-c.csv', 'w')

def rm_punctuation(text):
    regex = rexpression.compile('[%s]' % rexpression.escape(punctuation))
    noponctuation = []
    words = text.split()
    for word in words:
        ntoken = regex.sub(u'', word)
        if not ntoken == u'':
            noponctuation.append(ntoken)
    return noponctuation

def rm_stopwords(text):
    swords = stopwords.words('portuguese')
    content = [r for r in text if r.lower().strip() not in swords]
    return content

def tokenize(text):
    tclean = []
    for word in text:
        nfkd = unicodedata.normalize('NFKD', word)
        noword = u''.join([r for r in nfkd if not unicodedata.combining(r)])
        # ^[A-Za-z][A-Za-z0-9!@#$%^&*]*$ ou [^a-zA-Z0-9 \\\]
        join = rexpression.sub('[^a-zA-Z \\\]',' ', noword)
        tclean.append(join.lower().strip())
    tokens = [r for r in tclean if len(r) > 2 and not r.isdigit()]
    tprepared = ' '.join(tokens)
    return tprepared

def stemming(document):
    words = document.split()
    stm = []
    for word in words:
        stm.append(rslp.RSLPStemmer().stem(word))
    return (' '.join(stm))

for row in a__ifile:
    docw = rm_punctuation(unicode(row[0]))
    docw = rm_stopwords(docw)
    docw = tokenize(docw)
    docw = stemming(unicode(docw))
    a__ofile.write(docw)
    a__ofile.write('\n')

for row in b__ifile:
    docw = rm_punctuation(unicode(row[0]))
    docw = rm_stopwords(docw)
    docw = tokenize(docw)
    docw = stemming(unicode(docw))
    b__ofile.write(docw)
    b__ofile.write('\n')

for row in c__ifile:
    docw = rm_punctuation(unicode(row[0]))
    docw = rm_stopwords(docw)
    docw = tokenize(docw)
    docw = stemming(unicode(docw))
    c__ofile.write(docw)
    c__ofile.write('\n')

# CÓDIGO PARA GERAR UMA WORDCLOUD -> palavras que mais se repetem na base de dados
# fp.writelines(docw)
# fp.seek(0)
# data = fp.read()
# wordcloud = WordCloud().generate(data)
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()


print('********* PREPARED STOPWORDS *********')
