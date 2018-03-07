import sys
import urllib
import urllib.request as ur
import json
import codecs
from bs4 import BeautifulSoup

url = "https://play.google.com/store/getreviews"
struct = {
    "reviewType": "0",
    "pageNum": "0",
    "id": "com.google.android.apps.youtube.mango",
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
        print(soup.prettify())
        if review is None:
            break
        if sysenc == 'cp949':
            review = codecs.encode(review, sysenc, 'ignore')
        print()
        page += 1


if __name__ == "__main__":
    main()