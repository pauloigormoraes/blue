# import pandas as pd
import csv
from sklearn.datasets import load_iris
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import tempfile
import numpy as np

def main():

    list_rw = open('/home/paulomoraes/Projects/blue/back/dataset/data_clean.txt', 'r')
    arr = list_rw.read().strip().split('\n')

    # vectorizer = TfidfVectorizer(use_idf=True)
    # bag_of_words = vectorizer.fit_transform(arr)

    vectorizer = CountVectorizer(max_df=0.95, min_df=5)
    bag_of_words = vectorizer.fit_transform(arr)
    # print(bag_of_words)

    kmeans = KMeans(n_clusters = 5, init = 'random')
    kmeans.fit(bag_of_words)
    # print(kmeans.labels_)

    distance = kmeans.fit_transform(bag_of_words)
    # print(distance)

    # labels = kmeans.labels_
    # print(labels)

    # wcss = []
    # for r in range(1, 21):
    #     kmeans = KMeans(n_clusters = r, init = 'random')
    #     kmeans.fit(bag_of_words)
    #     print(r, kmeans.inertia_)
    #     wcss.append(kmeans.inertia_)
    # plt.plot(range(1, 21), wcss)
    # plt.title('ELBOW METHOD')
    # plt.xlabel('No Clusters')
    # plt.ylabel('DB')
    # plt.show()

    plt.scatter(distance[:, 0], distance[:,1], s = 50, c = kmeans.labels_)
    # plt.scatter(distance[:, 0], distance[:,1], marker='x', s=50, linewidths=3, c=kmeans.labels_)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 50, color = 'gray', label = 'Centroids')
    plt.title('Reviews Clusters and Centroids')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

    print("***** ---- END ---- *******")

if __name__ == "__main__":
    main()
