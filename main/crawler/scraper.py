import sys
import urllib
import urllib.request as ur
import json
import codecs
from bs4 import BeautifulSoup
import re
import requests
import time
import numpy as np
import csv

arq = open('/home/paulomoraes/Projects/blueway/main/dataset/page/.html')

def select(arr):
    a = str(arr)
    _str = a.split(' ')
    for r in _str:
        if _str.index(r) == 3:
            num = r
    return int(num)

def clean_string(name):
    nm = ' '.join(name.split())
    return nm

def configure(arr):
    print(arr)
    x = arr.split( )
    y = np.delete(x, len(x)-1)
    z = np.delete(y, len(y)-1)
    new_str = ''
    for r in z:
        new_str = new_str + r + " "
    return new_str

def main():
    soup = BeautifulSoup(arq, 'html.parser')
    data = soup.find_all(jscontroller='H6eOGe')
    # data = soup.find_all(class_='single-review')
    for i in range(0, len(data)):
        header = data[i].find(class_='Boieuf')
        auxb = data[i].find(class_='Z8UXhc').get_text()
        username = clean_string(header.find(class_='js5pLc').get_text())
        date = clean_string(header.find(class_='oldIDd').get_text())
        auxs = header.find(class_='pf5lIe')
        score = select(auxs.find(role='img'))
        body = clean_string(auxb)
        struct = {
            "author": username,
            "date": date,
            "score": score,
            "content": body
        }
        with open('/home/paulomoraes/Projects/blueway/main/dataset/high/full_reviews/.csv', 'a') as r:
            r.write(str(struct))
            r.write(',')
            r.write('\n')
            r.close
        print("get::review:::",i+1)

    print()
    print("::::: REVIEWS SAVED :::::")
    print()

if __name__ == "__main__":
    main()
