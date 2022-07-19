# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def GetContents(url):
    headers={
        "User-Agent":"Mozilla/5.0 (iPod; U; CPU iPhone OS 3_3 like Mac OS X; os-RU) AppleWebKit/531.18.3 (KHTML, like Gecko) Version/4.0.5 Mobile/8B115 Safari/6531.18.3",
        "Host":"www.xbiquge.la",
    }
    t=[]
    try:
        az=requests.get(headers=headers,url=url)
    except:
        t.append(["Failure","Failure"])
        return t
    soup=BeautifulSoup(az.content,"html.parser")
    for i in soup.find_all("dd"):
        for j in i.find_all("a"):
            temp=[]
            temp.append(j.text)
            temp.append("https://www.xbiquge.la"+j["href"])
            t.append(temp)
    return t
