# -*- encoding: utf-8 -*-

import requests
import sys,threading
from faker import Factory
from bs4 import BeautifulSoup
sys.path.append("..")
from search.contents import *
from download.chapter import *

runningThread=0
contents=[]
available=[]
result=[]
threads=[]

def Thread():
    global runningThread
    global threads
    self=threads[int(threading.current_thread().name.replace("Thread",""))-1]
    while True:
        idn=-1
        for i in range(0,len(contents)):
            if available[i]==True:
                idn=i
                available[i]=False
                break
        if idn==-1:
            runningThread-=1
            print("[{}] 停止运行,{} 线程正在运行\n".format(threading.current_thread().name,runningThread))
            return
        con=""
        while True:
            con=GetChapter(contents[idn][1])
            if con!="Failure":
                break
        result[idn]=con
        print("[{}] 完成第 {} 章,{} 线程正在运行\n".format(threading.current_thread().name,idn+1,runningThread))

def DownloadWhole(url):
    global threads
    global runningThread
    global contents
    global result
    global available
    contents=[]
    available=[]
    result=[]
    threads=[]
    print("正在下载目录")
    while True:
        contents=GetContents(url)
        if contents[0][0]=="Failure":
            print("Failure!")
            continue
        break
    print("共发现",len(contents),"章")
    for i in range(0,len(contents)):
        available.append(True)
        result.append("")
    threadCount=128
    runningThread=0
    # WARNING: Don't set the value to a too high value!!!
    for i in range(0,threadCount):
        threads.append(threading.Thread(target=Thread,name="Thread"+str(i+1)))
        threads[i].start()
        runningThread+=1
    for i in range(0,threadCount):
        threads[i].join()
    print("完成，正在返回结果...")
    result2=""
    for i in range(0,len(contents)):
        result2+=contents[i][0]
        result2+="\n\n"
        result2+=result[i]
        result2+="\n\n"
    return result2
