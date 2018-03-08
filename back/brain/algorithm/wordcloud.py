import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import tempfile

a__ifile = csv.reader(open('./dataset/.csv', 'r'))

fp = tempfile.TemporaryFile(mode='w+t')

for row in a__ifile:
    for i in row:
        fp.writelines(i)

fp.seek(0)
data = fp.read()

wordcloud = WordCloud().generate(data)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
