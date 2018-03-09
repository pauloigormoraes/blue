import sys
import urllib
import urllib.request as ur
import json
import codecs
from bs4 import BeautifulSoup
import re
import requests
import numpy as np

url = "https://play.google.com/store/getreviews"
options = {
    "reviewType": "0",
    "pageNum": "50",
    "hl": "pt",
    "id": "com.wonder",
    "reviewSortOrder": "2",
    "xhr": "1"
}

def loading(page):
    options["pageNum"] = str(page)
    data = urllib.parse.urlencode(options).encode("utf-8")
    request = ur.Request(url, data)
    response = ur.urlopen(request)
    jsond = response.read()
    page = json.loads(jsond[6:])
    try:
        review = page[0][50]
        return review
    except IndexError:
        return None

def select(arr):
  _str = arr.split( )
  for r in _str:
    #   if (math.isnan(r)) == False:
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
    reviews = []
    sysenc = sys.stdout.encoding
    # while True:
    for r in range(0, 1):
        review = loading(page)
        if review is None:
            break
        if sysenc == 'cp949':
            review = codecs.encode(review, sysenc, 'ignore')
            print(review)
        print (page)
        page += 1

    print(page)

if __name__ == "__main__":
    main()
