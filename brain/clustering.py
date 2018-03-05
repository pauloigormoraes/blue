import pandas as pd
import csv
from sklearn.datasets import load_iris
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import tempfile

a__ifile = csv.reader(open('/home/paulomoraes/Projects/lise/creep/data/prepared/cat-b.csv', 'r'))

data = []
for row in a__ifile:
    for i in row:
        data.append(i)

vectorizer = TfidfVectorizer(use_idf=True)
x = vectorizer.fit_transform(data)

tf_ = CountVectorizer(max_df=0.95, min_df=5)
xx = tf_.fit_transform(data)

# iris = load_iris()
# data = iris.data
# labels = iris.target
# labels_names = iris.target_names
#
# print(data)
#
# kmeans = KMeans(n_clusters = 3, init = 'random')
# kmeans.fit(x)
# print(kmeans.cluster_centers_)
#
# distance = kmeans.fit_transform(data)
# print(distance)

# labels = kmeans.labels_
# print(labels)


# wcss = []
# for i in range(1, 11):
#     kmeans = KMeans(n_clusters = i, init = 'random')
#     kmeans.fit(x)
#     print i,kmeans.inertia_
#     wcss.append(kmeans.inertia_)
# plt.plot(range(1, 11), wcss)
# plt.title('METODO ELBOW')
# plt.xlabel('No Clusters')
# plt.ylabel('WSS')
# plt.show()

# plt.scatter(x[:, 0], x[:,1], s = 100, c = kmeans.labels_)
# plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'red',label = 'centroids')
# plt.title('CLUSTERS REVIEWS - CATEGORY EDUCATION GAME')
# plt.xlabel('LENGHT')
# plt.ylabel('WIDHT')
# plt.legend()
# plt.show()

print("***** -------- *******")
