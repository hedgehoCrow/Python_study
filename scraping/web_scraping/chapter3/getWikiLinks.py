# coding: UTF-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")

    return bsObj.find("div", {"id": "bodyContent"}).findAll("a",
            href=re.compile("^(/wiki/)((?!:).)*$"))

def main():
    links = getLinks("/wiki/Kevin_Bacon")
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)

if __name__ == '__main__':
    main()


