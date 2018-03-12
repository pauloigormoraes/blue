import pandas as pd
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

    vectorizer = TfidfVectorizer(use_idf=True)
    bag_of_words = vectorizer.fit_transform(arr)

    # vectorizer = CountVectorizer(max_df=0.95, min_df=5)
    # bag_of_words = vectorizer.fit_transform(vtr)
    print(bag_of_words)

    kmeans = KMeans(n_clusters = 2, init = 'random')
    kmeans.fit(bag_of_words)
    # print(kmeans.labels_)

    distance = kmeans.fit_transform(bag_of_words)
    # print(distance)

    # labels = kmeans.labels_
    # print(labels)

    vtr = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters = i, init = 'random')
        kmeans.fit(bag_of_words)
        print i,kmeans.inertia_
        vtr.append(kmeans.inertia_)
    plt.plot(range(1, 11), wcss)
    plt.title('ELBOW METHOD')
    plt.xlabel('No Clusters')
    plt.ylabel('WSS')
    plt.show()

    # plt.scatter(bag_of_words[:, 0], bag_of_words[:,1], s = 100, c = kmeans.labels_)
    # plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, color = 'green', label = 'Centroids')
    # plt.title('Reviews Clusters and Centroids')
    # plt.xlabel('X')
    # plt.ylabel('Y')
    # plt.legend()
    #
    # plt.show()

    print("***** -------- *******")

if __name__ == "__main__":
    main()
