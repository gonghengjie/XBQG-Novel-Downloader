# -*- encoding: utf-8 -*-

import sys
from search.contents import *
from search.search import *
from download.whole import *
sys.path.append('..')
from parse import *

text=DownloadWhole(url).replace(u'\xa0',' ')
print("正在写文件...")
file=open(savepath,"w",encoding="utf-8")
file.write(text)
file.close()
