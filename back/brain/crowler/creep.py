import sys
import urllib
import urllib.request as ur
import json
import codecs
from bs4 import BeautifulSoup
import re
import numpy as np

url = "https://play.google.com/store/getreviews"
struct = {
    "reviewType": "0",
    "pageNum": "2",
    "lang": "pt",
    "id": "com.wonder",
    "reviewSortOrder": "0",
    "xhr": "1"
}

def content(page):
    struct["pageNum"] = str(page)
    data = urllib.parse.urlencode(struct).encode("utf-8")
    request = ur.Request(url, data)
    response = ur.urlopen(request)
    jsond = response.read()
    page = json.loads(jsond[6:])
    try:
        review = page[0][2]
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
    count = 0
    for r in range(0, 101):
    # while True:
        cont = content(page)
        soup = BeautifulSoup(cont, 'html.parser')
        data = list(soup.children)[1]
        header = data.find(class_='review-header')
        auxs = header.find(class_='star-rating-non-editable-container')
        username = header.find(class_='author-name').get_text()
        date = header.find(class_='review-date').get_text()
        score = select(auxs['aria-label'])
        auxb = data.find(class_='review-body').get_text()
        body = configure(auxb)
        review = {
            "author": username,
            "date": date,
            "score": score,
            "content": body
        }
        print(review)
        print(count)
        if review is None:
            break
        else:
            reviews.append(review)
        page += 1
        count += 1


if __name__ == "__main__":
    main()
