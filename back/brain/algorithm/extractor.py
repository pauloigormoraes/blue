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

    print("***** -------- *******")

if __name__ == "__main__":
    main()
