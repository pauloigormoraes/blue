import csv
import re as rexpression
from nltk.corpus import stopwords
# nltk.download('stopwords')
from string import punctuation
import unicodedata
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

a__ifile = csv.reader(open('/home/paulomoraes/Projects/lise/creep/data/organized/cat-a.csv', 'r'))
a__ofile = open('/home/paulomoraes/Projects/lise/creep/data/prepared/t_stopwords/wcat-a.csv', 'w')

b__ifile = csv.reader(open('/home/paulomoraes/Projects/lise/creep/data/organized/cat-b.csv', 'r'))
b__ofile = open('/home/paulomoraes/Projects/lise/creep/data/prepared/t_stopwords/wcat-b.csv', 'w')

c__ifile = csv.reader(open('/home/paulomoraes/Projects/lise/creep/data/organized/cat-c.csv', 'r'))
c__ofile = open('/home/paulomoraes/Projects/lise/creep/data/prepared/t_stopwords/wcat-c.csv', 'w')

def rmStopWord(text):

    regex = rexpression.compile('[%s]' % rexpression.escape(punctuation))
    noponctuation = []
    words = text.split()

    for word in words:
        ntoken = regex.sub(u'', word)
        if not ntoken == u'':
            noponctuation.append(ntoken)

    swords = stopwords.words('portuguese')
    nospace = [r for r in noponctuation if r.lower().strip() not in swords]

    tclean = []
    for word in nospace:
        nfkd = unicodedata.normalize('NFKD', word)
        noword = u''.join([r for r in nfkd if not unicodedata.combining(r)])
        # ^[A-Za-z][A-Za-z0-9!@#$%^&*]*$ ou [^a-zA-Z0-9 \\\]
        join = rexpression.sub('[^a-zA-Z \\\]',' ', noword)
        tclean.append(join.lower().strip())
        tokens = [r for r in tclean if len(r) > 2 and not r.isdigit()]
        tprepared = ' '.join(tokens)

    return tprepared

for row in a__ifile:
    docw = rmStopWord(unicode(row[0]))
    a__ofile.write(docw)
    a__ofile.write('\n')

for row in b__ifile:
    docw = rmStopWord(unicode(row[0]))
    b__ofile.write(docw)
    b__ofile.write('\n')

for row in c__ifile:
    docw = rmStopWord(unicode(row[0]))
    c__ofile.write(docw)
    c__ofile.write('\n')

print('********* PREPARED STOPWORDS *********')
