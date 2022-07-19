# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def SearchBook(keyword):
    data={
        "searchkey":keyword
    }
    headers={
        "User-Agent":"Mozilla/5.0 (iPod; U; CPU iPhone OS 3_3 like Mac OS X; os-RU) AppleWebKit/531.18.3 (KHTML, like Gecko) Version/4.0.5 Mobile/8B115 Safari/6531.18.3",
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
        # bookURL
        temp.append(td[0].find_all("a")[0].text)
        # bookName
        temp.append("https://www.xbiquge.la"+td[1].find_all("a")[0]["href"])
        # newestChapterURL
        temp.append(td[1].find_all("a")[0].text)
        # newestChapterName
        temp.append(td[2].text)
        # author
        temp.append(td[3].text.replace(" ",""))
        # updateDate
        t.append(temp)
    return t
