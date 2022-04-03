# -*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
from search.contents import *
import requests

url="https://www.xbiquge.la/79/79721/"
savepath="${novelName}$.${chapterTotal}$.txt"

while True:
    contents=GetContents(url)
    if contents[0][0]=="Failure":
        continue
    break
soup=BeautifulSoup(requests.get(url).text,"html.parser")
savepath=savepath.replace("${novelName}$",soup.find_all('h1')[0].text).replace("${chapterTotal}$",str(len(contents)))
