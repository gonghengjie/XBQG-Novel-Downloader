# -*- encoding: utf-8 -*-

import sys,inspect
from search.contents import *
from search.search import *
from download.keyword import *
from download.whole import *

savepath = "Examples/${novelName}$.${chapterTotal}$.txt"

def Download(novelURL):
    print("正在获取章数...",end='')
    while True:
        contents=GetContents(novelURL)
        if contents[0][0]=="Failure":
            continue
        break
    chapterCount  = len(contents)
    print(chapterCount)
    print("正在获取书名...",end='')
    bookname      = ""
    while True:
        bookname=BookName(novelURL)
        if bookname=="Failure":
            continue
        break
    print(bookname)
    savepathFinal = savepath.replace("${novelName}$",bookname)
    savepathFinal = savepathFinal.replace("${chapterTotal}$",str(chapterCount))
    print("最终存储路径:",savepathFinal)
    text=DownloadWhole(novelURL)[0].replace(u'\xa0',' ').replace('手机站全新改版升级地址：https://wap.xbiquge.la，数据和书签与电脑站同步，无广告清新阅读！','').replace('亲,点击进去,给个好评呗,分数越高更新越快,据说给香书小说打满分的最后都找到了漂亮的老婆哦!','')
    f=open(savepathFinal,"w",encoding='utf-8')
    f.write(text)
    f.close()

def DownloadAll(keyword):
    raw=SearchBook(keyword)
    print("将要下载",len(raw),"本书:")
    for i in raw:
        print("网址:{};\n作者:{},名称:{}\n".format(i[0],i[1],i[4]))
    for i in range(0,len(raw)):
        print("开始下载第 {} 部小说 ({})".format(i+1,raw[i][1]))
        Download(raw[i][0])
    print("\n---\n下载完成")

# Download('https://www.xbiquge.la/51/51097/')
DownloadAll(input("输入关键字:"))
