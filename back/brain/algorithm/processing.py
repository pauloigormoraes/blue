# nltk.download() for download packages
import re as rexpression
from nltk.corpus import stopwords
from nltk.stem import rslp
import tempfile
from string import punctuation
import unicodedata
# import sys
#
# reload(sys)
# sys.setdefaultencoding("utf-8")

fp = tempfile.TemporaryFile(mode='w+t')

i_file = open('/home/paulomoraes/Projects/blue/back/dataset/reviews.csv', 'r')
o_file = open('/home/paulomoraes/Projects/blue/back/dataset/data_clean.txt', 'a')

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

def main():
    arr = []
    for row in i_file:
        docw = rm_punctuation(row)
        docw = rm_stopwords(docw)
        docw = tokenize(docw)
        docw = stemming(docw)
        o_file.write(docw)
        o_file.write('\n')
        o_file.close
        arr.append(docw)

    # o_file.write(str(arr))
    # o_file.close

    # with open('/home/paulomoraes/Projects/blue/back/dataset/data_clean.csv', 'a') as csvfile:
    #     spamwriter = csv.writer(csvfile, delimiter=' ')
    #     spamwriter.writerow([arr])

    print
    print('********* PREPARED STOPWORDS *********')
    print

if __name__ == "__main__":
    main()
