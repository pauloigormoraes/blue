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

# i_file = open('/home/paulomoraes/Projects/blue/back/dataset/reviews.csv', 'r')
o_file = open('/home/paulomoraes/Projects/blue/back/dataset/data_clean.csv', 'a')

i_file = ['Eu estou aqqui querendo,o que,eu quero qqquiser',
          '',
          'Será que isso realmente =D vai atualizar?']

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

def remove_space(text):
    arr = text.split()
    print(arr)


def trigrams(words):
    arr = words.read().strip().split(' ')
    trigrams = []
    for r in range(0, len(words)):
        if(r == len(words)-2):
            break
        else:
            trigram = words[r]+'_'+words[r+1]+'_'+words[r+2]
            trigrams.append(trigram)
    return trigrams

def main():
    arr = []
    r_trigrams = []

    for row in i_file:
        # docw = text_space_reduce(row)
        # docw = rm_punctuation(docw)
        # docw = rm_stopwords(docw)
        # docw = tokenize(docw)
        # docw = stemming(docw)
        docw = remove_space(row)
        # for i in adocwrr:
        #     unigrams.append(word)
        # r_trigrams = trigrams(unigrams)
        # o_file.write(docw)
        # o_file.write('\n')
        # o_file.close
        # arr.append(docw)

    # o_file.write(str(arr))
    # o_file.close

    # with open('/home/paulomoraes/Projects/blue/back/dataset/data_clean.csv', 'a') as csvfile:
    #     spamwriter = csv.writer(csvfile, delimiter=' ')
    #     spamwriter.writerow([arr])

    print()
    print('********* PREPARED STOPWORDS *********')
    print()

if __name__ == "__main__":
    main()
