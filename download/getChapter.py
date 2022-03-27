# -*- encoding: utf-8 -*-

import requests
from faker import Factory
from bs4 import BeautifulSoup

def GetChapter(url):
    headers={
        "User-Agent":Factory.create().user_agent(),
        "Host":"www.xbiquge.la"
    }
    try:
        response=requests.get(url=url,headers=headers,timeout=5)
    except:
        return "Failure"
    soup=BeautifulSoup(response.content,"html.parser")
    return soup.find_all("div",id="content")[0].text
