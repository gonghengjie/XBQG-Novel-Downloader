# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def GetChapter(url):
    headers={
        "User-Agent":"Mozilla/5.0 (iPod; U; CPU iPhone OS 3_3 like Mac OS X; os-RU) AppleWebKit/531.18.3 (KHTML, like Gecko) Version/4.0.5 Mobile/8B115 Safari/6531.18.3",
        "Host":"www.xbiquge.la"
    }
    try:
        response=requests.get(url=url,headers=headers,timeout=5)
    except:
        return "Failure"
    soup=BeautifulSoup(response.content,"html.parser")
    return soup.find_all("div",id="content")[0].text
