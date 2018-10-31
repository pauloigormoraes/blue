import sys
import urllib
import urllib.request as ur
import json
import codecs
from bs4 import BeautifulSoup as bs
import re
import requests
import time
import numpy as np
import csv

arq = open('C:/Projects/blueway/main/dataset/apps_high_pages/high_app_5.html', encoding="utf8")

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
    x = arr.split( )
    y = np.delete(x, len(x)-1)
    z = np.delete(y, len(y)-1)
    new_str = ''
    for r in z:
        new_str = new_str + r + " "
    return new_str

def main():
    soup = bs(arq, 'html.parser')
    data = soup.find_all(jscontroller='H6eOGe')

    for i in range(0, len(data)):
        auxb = data[i].find(class_='UD7Dzf').get_text()
        header = data[i].find(class_='zc7KVe')
        username = clean_string(header.find(class_='X43Kjb').get_text())
        date = clean_string(header.find(class_='p2TkOb').get_text())
        auxs = header.find(class_='pf5lIe')
        score = select(auxs.find(role='img'))
        body = clean_string(auxb)

        struct = {
            "author": username,
            "date": date,
            "score": score,
            "content": body
        }

        with open('C:/Projects/blueway/main/dataset/full_reviews/high/app_5.csv', 'a', encoding="utf8") as r:
            r.write(str(struct))
            r.write(',')
            r.write('\n')
            r.close

        # file = csv.writer(open("C:/Projects/blueway/main/dataset/full_reviews/low/low_app_one.csv", "a", encoding="utf8"))
        # file.writerow([str(username),str(date),str(score),str(body)])

        print("get:::review:::",i+1)

    print()
    print("::::: REVIEWS SAVED :::::")
    print()

if __name__ == "__main__":
    main()
