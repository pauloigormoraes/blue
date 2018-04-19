# import pandas as pd
import csv
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import tempfile
import numpy as np

def main():

    list_rw = open('/home/paulomoraes/Projects/blue/back/dataset/data_clean.csv', 'r')
    aux = open('/home/paulomoraes/Projects/blue/back/dataset/reviews.csv', 'r')
    arr = list_rw.read().strip().split('\n')
    reviews = aux.read().strip().split('\n')

    group_a_file = open('/home/paulomoraes/Projects/blue/back/dataset/group_a.csv', 'w')
    group_b_file = open('/home/paulomoraes/Projects/blue/back/dataset/group_b.csv', 'w')
    group_c_file = open('/home/paulomoraes/Projects/blue/back/dataset/group_c.csv', 'w')
    group_d_file = open('/home/paulomoraes/Projects/blue/back/dataset/group_d.csv', 'w')
    group_e_file = open('/home/paulomoraes/Projects/blue/back/dataset/group_e.csv', 'w')

    values_np = np.array(arr)
    # print(values_clnp)

    vectorizer = TfidfVectorizer(use_idf=True)
    bag_of_words = vectorizer.fit_transform(values_np)
    # print(bag_of_words)

    # vectorizer = CountVectorizer(max_df=0.95, min_df=5)
    # bag_of_words = vectorizer.fit_transform(arr)

    # kmeans = KMeans(n_clusters = 4, init = 'k-means++', max_iter = 600).fit(bag_of_words)
    kmeans = KMeans(n_clusters = 5, init = 'random').fit(bag_of_words)
    # print(kmeans.cluster_centers_)

    distance = kmeans.fit_transform(bag_of_words)
    # print(distance)

    labels = kmeans.labels_
    # print(labels)

    # Onde cada instância vai ser clusterizada, i. e., em qual grupo cada review será agrupado;
    predict = kmeans.predict(bag_of_words)

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

    # plt.scatter(distance[:, 0], distance[:,1], s = 100, c = kmeans.labels_)
    # # plt.scatter(distance[:, 0], distance[:,1], marker='x', s=50, linewidths=3, c=kmeans.labels_)
    # plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, color = 'red', label = 'Centroids')
    # plt.title('Reviews Clusters and Centroids')
    # plt.xlabel('X')
    # plt.ylabel('Y')
    # plt.legend()
    # plt.show()

    print()
    print("***** ---- --- ---- *******")
    print()

    results = []
    group_a = []
    group_b = []
    group_c = []
    group_d = []
    group_e = []

    for ix_pdc, value in enumerate(predict):
        for ix_rvw, content in enumerate(arr):
            if ix_pdc == ix_rvw:
                if value == 0:
                    a = [value, content]
                    group_a.append(a)
                    group_a_file.write(content)
                    group_a_file.write('\n')
                    group_a_file.close
                elif value == 1:
                    b = [value, content]
                    group_b.append(b)
                    group_b_file.write(content)
                    group_b_file.write('\n')
                    group_b_file.close
                elif value == 2:
                    c = [value, content]
                    group_c.append(c)
                    group_c_file.write(content)
                    group_c_file.write('\n')
                    group_c_file.close
                elif value == 3:
                    d = [value, content]
                    group_d.append(d)
                    group_d_file.write(content)
                    group_d_file.write('\n')
                    group_d_file.close
                elif value == 4:
                    e = [value, content]
                    group_e.append(e)
                    group_e_file.write(content)
                    group_e_file.write('\n')
                    group_e_file.close
                aux = [value, content]
                results.append(aux)

    print("CLUSTERS")
    print()
    print("Group [A]:", len(group_a))
    print("Group [B]:", len(group_b))
    print("Group [C]:", len(group_c))
    print("Group [D]:", len(group_d))
    print("Group [E]:", len(group_e))
    print()
    print("TOTAL:", len(group_a) + len(group_b) + len(group_c) + len(group_d) + len(group_e))

    print()
    print("***** ---- END ---- *******")
    print()

if __name__ == "__main__":
    main()
