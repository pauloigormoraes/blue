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

# i_file = open('/home/paulomoraes/Projects/blueway/back/dataset/apps_filters_less.csv', 'r')
# data = i_file.read().strip().split('\n')
# ids = []
# for row in data:
#     aux = row.split('=')
#     ids.append(aux[1])
# https://play.google.com/store/apps/details?id=com.knoozapps.thumbnaildownloader
url = "/home/paulomoraes/Projects/blueway/back/dataset/web-pages/app_test.html"
url = "https://play.google.com/store/getreviews"

options = {
    "reviewType": "0",
    "pageNum": "5",
    "lang": "pt",
    "id": "com.weberdo.apps.serviceinfo",
    "reviewSortOrder": "2",
    "xhr": "1"
}

def loading(page):
    # options["pageNum"] = str(page)
    data = urllib.parse.urlencode(options).encode("utf-8")
    req = ur.Request(url, data)
    response = ur.urlopen(req)
    jdata = response.read()
    page = json.loads(jdata[6:])
    try:
        review = page[0][2]
        return (review)
    except IndexError:
        return None

def select(arr):
  _str = arr.split( )
  for r in _str:
      if _str.index(r) == 3:
        num = r
  return int(num)

def configure(arr):
    x = arr.split( )
    y = np.delete(x, len(x)-1)
    z = np.delete(y, len(y)-1)
    new_str = ''
    for r in z:
        new_str = new_str + r + " "
    return new_str

def main():
    page = 0
    sysenc = sys.stdout.encoding
    reviews = []
    while True:
    # for i in range(0, 1):
        review = loading(page)
        if review is None:
            break
        if sysenc == 'cp949':
            review = codecs.encode(review, sysenc, 'ignore')
        soup = BeautifulSoup(review, 'html.parser')
        data = list(soup.children)[1]
        header = data.find(class_='review-header')
        auxs = header.find(class_='star-rating-non-editable-container')
        username = header.find(class_='author-name').get_text()
        date = header.find(class_='review-date').get_text()
        score = select(auxs['aria-label'])
        auxb = data.find(class_='review-body').get_text()
        body = configure(auxb)
        struct = {
        "author": username,
        "date": date,
        "score": score,
        "content": body
        }
        reviews.append(struct)
        with open('/home/paulomoraes/Projects/blueway/back/dataset/full_reviews_more.txt', 'a') as r:
            r.write(str(struct))
            r.write(',')
            r.write('\n')
            r.close
        # with open('/home/paulomoraes/Projects/blueway/back/dataset/reviews.csv', 'a', newline='') as csvfile:
        #     spamwriter = csv.writer(csvfile, delimiter=' ')
        #     # spamwriter.writerow([''])
        #     spamwriter.writerow([body])
        print("get::review:::",page+1)
        page += 1

    print()
    print("::::: FILES SAVE :::::")
    print()

if __name__ == "__main__":
    main()
