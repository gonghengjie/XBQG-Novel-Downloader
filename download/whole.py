# -*- encoding: utf-8 -*-

import requests
from faker import Factory
from bs4 import BeautifulSoup

def DownloadWhole(url):
    contents=[]
    print("正在下载目录")
    while True:
        contents=GetContents(url)
        if contents[0][0]=="Failure":
            print("Failure!")
            continue
        break
    print("共发现",len(contents),"章")
    content_all=""
    cnt=0
    for i in contents:
        cnt+=1
        print("正在下载第",cnt,"章(",i[0],")")
        content_all+=i[0]+"\n\n"
        while True:
            content=GetChapter(i[1])
            if content=="Failure":
                print("Failure!")
                continue
            if content.find("亲,点击进去,给个好评呗")!=-1:
                content=content[0:content.find("亲,点击进去,给个好评呗")]
            content_all+=content
            break
        content_all+="\n\n"
    f=open(i[0]+".txt","w")
    f.write(content_all)
