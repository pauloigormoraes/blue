import nltk
nltk.download('rslp')

def Stemming(instancia):
  stemmer = nltk.stem.RSLPStemmer()
  	palavras=[]
  for w in instancia.split():
      palavras.append(stemmer.stem(w))
  return (" ".join(palavras))


v = Stemming("Eu nao quero mais ficar trabalhando na criacao desse projeto estou super cansado")
print(v)
