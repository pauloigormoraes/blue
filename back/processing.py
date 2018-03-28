# nltk.download() for download packages
import re as rexpression
from nltk.corpus import stopwords
from nltk.stem import rslp
import tempfile
from string import punctuation
import unicodedata
import time

i_file = open('/home/paulomoraes/Projects/blue/back/dataset/reviews.csv', 'r')
# i_file = i_file.read().strip().split('\n')
o_file = open('/home/paulomoraes/Projects/blue/back/dataset/data_clean.csv', 'a')

# i_file = ['Eu estou aqqui querendo,o que,eu quero qqquiser','','Será que isso realmente =D vai atualizar?']

def text_space_reduce(text):
    review = []
    aux = []
    words = text.split()
    for word in words:
        none = ''.join(['' if i > 1 and e == word[i-1] else e for i, e in enumerate(word)])
        one = list(none)
        for index, letter in enumerate(none):
            if letter == ',':
                one[index] = ', '
            nword = ''.join(one)
        aux.append(nword)
        aux.append(' ')
    review = ''.join(aux)
    return review

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
    tokens = [r for r in tclean if len(r) > 1 and not r.isdigit()]
    tprepared = ' '.join(tokens)
    return tprepared

def stemming(text):
    words = text.split()
    stm = []
    for word in words:
        stm.append(rslp.RSLPStemmer().stem(word))
    return (' '.join(stm))

def trigrams(words):
    arr = words.read().strip().split(' ')
    trigrams = []
    print(o)
    for r in range(0, len(words)):
        if(r == len(words)-2):
            break
        else:
            trigram = words[r]+'_'+words[r+1]+'_'+words[r+2]
            trigrams.append(trigram)
    return trigrams

def main():
    arr = []

    empty = 0
    reviews = 0
    all_rw = 0

    start = time.time()
    for row in i_file:
        all_rw += 1
        docw = text_space_reduce(row)
        docw = rm_punctuation(docw)
        docw = rm_stopwords(docw)
        docw = tokenize(docw)
        docw = stemming(docw)
        if docw == '':
            empty += 1
        else:
            reviews += 1
            o_file.write(docw)
            o_file.write('\n')
            o_file.close
            arr.append(docw)
        print('... processing')
    end = time.time()

    print()
    print('# INFOs #')
    print('total: ', all_rw)
    print('empty: ', empty)
    print('saved: ', reviews)
    print('time: {:.2f}'.format(end - start),'s')
    print()
    print('********* PREPARED STOPWORDS *********')
    print()

if __name__ == "__main__":
    main()
