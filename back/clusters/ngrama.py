
list_rw = open('/home/paulomoraes/Projects/blue/back/dataset/data_clean.csv', 'r')
o_file = open('/home/paulomoraes/Projects/blue/back/dataset/ngrama.csv', 'a')
arr = list_rw.read().strip().split(' ')

def trigrams(words):
    trigrams = []
    for r in range(0, len(words)):
        if(r == len(words)-2):
            break
        else:
            trigram = words[r]+'_'+words[r+1]+'_'+words[r+2]
            trigrams.append(trigram)
    return trigrams

def main():
    unigrams = []
    r_trigrams = []
    for word in arr:
        unigrams.append(word)
    r_trigrams = trigrams(unigrams)

    print(r_trigrams)

if __name__ == "__main__":
    main()
