#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import pandas as pd
import csv
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import tempfile
import numpy as np
from sklearn.datasets.samples_generator import make_blobs

def main():

    list_rw = open("C:/Projects/blueway/main/dataset/clean_data/clean_high.csv", "r")
    list_rw = list_rw.read().strip().split("\n")
    print(len(list_rw))

    arr_1 = []
    arr_2 = []
    arr_3 = []
    arr_4 = []
    arr_5 = []
    arr_6 = []
    arr_7 = []
    arr_8 = []
    arr_9 = []
    arr_10 = []
    arr_11 = []
    arr_12 = []
    arr_13 = []

    values_np = np.array(list_rw)
    # print(len(values_np))

    vectorizer = TfidfVectorizer(use_idf=True)
    bag_of_words = vectorizer.fit_transform(values_np)

    # vectorizer = CountVectorizer(max_df=0.95, min_df=5)
    # bag_of_words = vectorizer.fit_transform(values_np)
    # print(bag_of_words)

    kmeans = KMeans(n_clusters = 13, init = 'k-means++', max_iter = 600).fit(bag_of_words)
    # kmeans = KMeans(n_clusters = 13, init = 'random').fit(bag_of_words)
    # print(kmeans.cluster_centers_)

    # distance = kmeans.fit_transform(bag_of_words)

    labels = kmeans.labels_
    # print(labels)

    # Onde cada instância vai ser clusterizada, i. e., em qual grupo cada review será agrupado;
    predict = kmeans.predict(bag_of_words)

    for value in predict:
        if value == 1:
            arr_1.append(value)
        elif value == 2:
            arr_2.append(value)
        elif value == 3:
            arr_3.append(value)
        elif value == 4:
            arr_4.append(value)
        elif value == 5:
            arr_5.append(value)
        elif value == 6:
            arr_6.append(value)
        elif value == 7:
            arr_7.append(value)
        elif value == 8:
            arr_8.append(value)
        elif value == 9:
            arr_9.append(value)
        elif value == 10:
            arr_10.append(value)
        elif value == 11:
            arr_11.append(value)
        elif value == 12:
            arr_12.append(value)
        else:
            arr_13.append(value)

    print('g1 > ', len(arr_1))
    print('g2 > ', len(arr_2))
    print('g3 > ', len(arr_3))
    print('g4 > ', len(arr_4))
    print('g5 > ', len(arr_5))
    print('g6 > ', len(arr_6))
    print('g7 > ', len(arr_7))
    print('g8 > ', len(arr_8))
    print('g9 > ', len(arr_9))
    print('g10 > ', len(arr_10))
    print('g11 > ', len(arr_11))
    print('g12 > ', len(arr_12))
    print('g13 > ', len(arr_13))

    print()
    print('total: ', len(arr_1)+len(arr_2)+len(arr_3)+len(arr_4)+len(arr_5)+len(arr_6)+len(arr_7)+len(arr_8)+len(arr_9)+len(arr_10)+len(arr_11)+len(arr_12)+len(arr_13))

    # wcss = []
    # for r in range(1, 11):
    #     kmeans = KMeans(n_clusters = r, init = 'random')
    #     kmeans.fit(bag_of_words)
    #     print(r, kmeans.inertia_)
    #     wcss.append(kmeans.inertia_)
    # plt.plot(range(1, 11), wcss)
    # plt.title('Método Elbow')
    # plt.xlabel('No Clusters')
    # plt.ylabel('Base de Dados')
    # plt.show()

    # print(kmeans.cluster_centers_[:1,:])
    # print(kmeans.cluster_centers_[:1,:])

    # plt.scatter(distance[:, 0], distance[:,1], s = 50, c = labels, alpha=0.5)
    # plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 50, c = 'red', label = 'Centroids')
    # # plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, color = 'black', alpha=0.5)
    # plt.title('Reviews Clusters and Centroids')
    # plt.xlabel('X')
    # plt.ylabel('Y')
    # plt.legend()
    # plt.show()

if __name__ == "__main__":
    main()
