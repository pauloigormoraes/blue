import sys
import urllib
import urllib.request as ur
import json
import codecs
from bs4 import BeautifulSoup
import re

url = "https://play.google.com/store/getreviews"
struct = {
    "reviewType": "0",
    "pageNum": "0",
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

def main():
    page = 0
    sysenc = sys.stdout.encoding
    for x in range(0, 1):
    # while True:
        review = content(page)
        soup = BeautifulSoup(review, 'html.parser')
        data = list(soup.children)[1]
        header = data.find(class_='review-header')
        username = header.find(class_='author-name').get_text()
        date = header.find(class_='review-date').get_text()
        # score = header.find(class_='star-rating-non-editable-container').get_text()
        body = data.find(class_='review-body').get_text()
        print(username)
        print(date)
        # print(score)
        print(body)
        # if review is None:
        #     break
        # if sysenc == 'cp949':
        #     review = codecs.encode(review, sysenc, 'ignore')
        page += 1


if __name__ == "__main__":
    main()
