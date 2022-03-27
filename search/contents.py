# -*- encoding: utf-8 -*-

import requests
from faker import Factory
from bs4 import BeautifulSoup
def GetContents(url):
    headers={
        "User-Agent":Factory.create().user_agent(),
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
