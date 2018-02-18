import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

iris = load_iris()
data = iris.data
labels = iris.target
labels_names = iris.target_names

kmeans = KMeans(n_clusters = 3, init = 'random')
kmeans.fit(data)
print(kmeans.cluster_centers_)

distance = kmeans.fit_transform(data)
# print(distance)

labels = kmeans.labels_
# print(labels)


# wcss = []

# for i in range(1, 11):
#     kmeans = KMeans(n_clusters = i, init = 'random')
#     kmeans.fit(data)
#     print i,kmeans.inertia_
#     wcss.append(kmeans.inertia_)
# plt.plot(range(1, 11), wcss)
# plt.title('METODO ELBOW')
# plt.xlabel('No Clusters')
# plt.ylabel('WSS')
# plt.show()

plt.scatter(data[:, 0], data[:,1], s = 100, c = kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'red',label = 'centroids')
plt.title('CLUSTERS REVIEWS - CATEGORY EDUCATION GAME')
plt.xlabel('LENGHT')
plt.ylabel('WIDHT')
plt.legend()
plt.show()

print("***** -------- *******")
