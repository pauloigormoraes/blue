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

arr = [
    'br.com.vivo',
    'br.com.mobicare.minhaoi',
    'com.keyboard.flagard',
    'br.com.timbrasil.meutim',
    'com.app99.driver',
    'com.gvt.minhagvt.enterprise',
    'br.gov.serpro.cnhe',
    'br.gov.fazenda.receita.irpf',
    'br.gov.dataprev.sinefacil',
    'com.knoozapps.thumbnaildownloader',
    'codematics.universal.tv.remote.control',
    'br.gov.sp.fazenda.nfp.app',
    'com.androidaplicativos.rastrearcelularpelonumero',
    'braveheart.apps.apkinstaller',
    'br.com.vivo.meuvivomais',
    'com.samsung.smartviewad',
    'one.mobileapps.apkbackup',
    'com.latin.leichte',
    'com.apple.movetoios',
    'com.rusdelphi.wifipassword',
    'us.rajaematechkr.downloadvideo.downloaderhd',
    'br.com.mobicare.tim.recarga',
    'Face.Sorter',
    'com.wwagad.l5',
    'com.mobile.myeye',
    'com.emoji.wifipassword',
    'br.com.sabesp.android.sabespmobile',
    'com.phongphan.miracast',
    'br.com.mobicare.samsung.recarga',
    'fahrbot.apps.undelete',
    'houssamos.eyes.catcher',
    'com.asamiyuma.zip',
    'com.ticktalk.cameratranslator',
    'screenmirroring.mirrorcast.com.kiwahapps',
    'com.outfall.inss',
    'com.embratec.ecofrotas',
    'com.clipcomm.WiFiRemocon',
    'com.basf.suvinil.crie',
    'br.com.mobicare.oi.recarga',
    'com.Tv.IR.Remote'
]

url = "https://play.google.com/store/getreviews"
options = {
    "reviewType": "0",
    "pageNum": "5",
    "lang": "pt",
    "id": "br.com.mobicare.minhaoi",
    "reviewSortOrder": "2",
    "xhr": "1"
}

def loading(page):
    options["pageNum"] = str(page)
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
    # while True:
    for i in range(0, 1):
        review = loading(page)
        if review is None:
            break
        if sysenc == 'cp949':
            review = codecs.encode(review, sysenc, 'ignore')
        soup = BeautifulSoup(review, 'html.parser')
        data = list(soup.children)[1]
        print(data)
        # header = data.find(class_='review-header')
        # auxs = header.find(class_='star-rating-non-editable-container')
        # username = header.find(class_='author-name').get_text()
        # date = header.find(class_='review-date').get_text()
        # score = select(auxs['aria-label'])
        # auxb = data.find(class_='review-body').get_text()
        # body = configure(auxb)
        # struct = {
        # "author": username,
        # "date": date,
        # "score": score,
        # "content": body
        # }
        # reviews.append(struct)
        # with open('/home/paulomoraes/Projects/blueway/back/dataset/full_reviews.txt', 'a') as r:
        #     r.write(str(struct))
        #     r.write('\n')
        #     r.close
        # with open('/home/paulomoraes/Projects/blueway/back/dataset/reviews.csv', 'a', newline='') as csvfile:
        #     spamwriter = csv.writer(csvfile, delimiter=' ')
        #     # spamwriter.writerow([''])
        #     spamwriter.writerow([body])
        # print("get::review:::",page+1)
        # page += 1

    print()
    print("::::: FILES SAVE :::::")
    print()

if __name__ == "__main__":
    main()
