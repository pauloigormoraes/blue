import csv
import re
import nltk
# nltk.download()
import string
import unicodedata
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

file = csv.reader(open('/home/paulomoraes/Projects/lise/creep/data/organized/education-game.csv', 'r'))
rnews = []

def rmStopWord(text):

    regex = re.compile('[%s]' % re.escape(string.punctuation))
    vtr = []
    words = text.split()

    for wd in words:
        ntoken = regex.sub(u'', wd)
        if not ntoken ==u'':
            vtr.append(ntoken)

    swords = nltk.corpus.stopwords.words('portuguese')
    content = [r for r in vtr if r.lower().strip() not in swords]
    tclean = []

    for word in content:
        nfkd = unicodedata.normalize('NFKD', word)
        noword = u''.join([r for r in nfkd if not unicodedata.combining(r)])
        # ^[A-Za-z][A-Za-z0-9!@#$%^&*]*$ ou [^a-zA-Z0-9 \\\]
        join = re.sub('[^a-zA-Z \\\]',' ', noword)
        tclean.append(join.lower().strip())
        tokens = [r for r in tclean if len(r) > 2 and not r.isdigit()]
        tprepared = ' '.join(tokens)

    return tprepared

for row in file:
    docw = rmStopWord(unicode(row[0]))
    rnews.append(docw)
    print(docw)
