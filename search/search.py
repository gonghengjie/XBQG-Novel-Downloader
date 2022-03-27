# -*- encoding: utf-8 -*-

import requests
from faker import Factory
from bs4 import BeautifulSoup

def SearchBook(keyword):
    data={
        "searchkey":keyword
    }
    headers={
        "User-Agent":Factory.create().user_agent(),
        "Host":"www.xbiquge.la"
    }
    t=[]
    try:
        response=requests.post(url="https://www.xbiquge.la/modules/article/waps.php",data=data,headers=headers)
    except:
        t.append(["Failure","Failure"])
        return t
    soup=BeautifulSoup(response.content,"html.parser")
    tr=soup.find_all("tr")
    for i in range(1,len(tr),1):
        temp=[]
        td=tr[i].find_all("td")
        temp.append(td[0].find_all("a")[0]["href"])
        temp.append(td[0].find_all("a")[0].text)
        temp.append("https://www.xbiquge.la"+td[1].find_all("a")[0]["href"])
        temp.append(td[1].find_all("a")[0].text)
        temp.append(td[2].text)
        temp.append(td[3].text.replace(" ",""))
        t.append(temp)
    return t
