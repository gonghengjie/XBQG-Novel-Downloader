# -*- encoding: utf-8 -*-

import requests
import sys
sys.path.append("..")
from download.whole import *
from search.search import *

def Keyword(keyword):
    books=SearchBook(keyword)
    while books[0][0]=="Failure":
        books=SearchBook(keyword)
    if len(books)==0:
        print("未找到任何项目!")
        return
    else:
        print("找到",len(books),"个项目")
        if len(books)>10:
            print("项目过多,仅显示前 10 项!")
        for i in range(0,min(len(books),10)):
            print("ID={} URL={}\nName={} Author={}\nUpdateDate={}".format(i,books[i][0],books[i][1],books[i][4],books[i][5]))
    for i in books:
        # startRequest
        pass
