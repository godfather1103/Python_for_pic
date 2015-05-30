# encoding: utf-8
'''
Created on 2015年5月29日

@author: ccb
'''
#import py.snippet3  
from py import snippet3
from bs4 import BeautifulSoup
from collections import deque

queue = deque()
urlcont = 0
#入口地址
#url = 'http://www.wmpic.me/tupian/yijing/'
url = 'http://www.mzitu.com/share'
queue.append(url)
count1 = 0
#设置爬取的图片数和网页数
pic_cont = 1000
url_cont = 20

def loop(url):
    print(url)
    global count1
    count1 += snippet3.pic(url,pic_cont-count1)
    #print('count1='+str(count1))
    soup = BeautifulSoup(snippet3.user_agent(url))
    tag_a = soup.find_all(['a','A'])
    for a in tag_a:
        link = a.get('href')
        try:   
            if link not in queue:
                queue.append(link)
                loop(link)
                #snippet3.pic(link)
                #print(link)
        except:
            continue    
        #爬取的页面数
        if len(queue)==url_cont or count1==pic_cont:
           return
loop(url)