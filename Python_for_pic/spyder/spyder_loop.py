# encoding: utf-8
'''
Created on 2015年5月27日

@author: ccb
'''
import spyder_for_pic
from bs4 import BeautifulSoup
from collections import deque
 
queue = deque()


#入口地址
url = 'http://www.wmpic.me/tupian/yijing/'
url = 'http://www.mzitu.com'
queue.append(url)
count1 = 0
#设置爬取的图片数和网页数
pic_cont = 200
url_cont = 100

def loop(url):
    print(url)
    global count1
    count1 += spyder_for_pic.pic(url,pic_cont-count1)
    soup = BeautifulSoup(spyder_for_pic.user_agent(url))
    tag_a = soup.find_all(['a','A'])
    
    for a in tag_a:
        link = a.get('href')
        try:   
            if link not in queue:
                queue.append(link)
                loop(link)
                #spyder_for_pic.pic(link)
                #print (link) 
        except:
            continue    
        #爬取的页面数
        if len(queue)==url_cont or count1==pic_cont:
           return
loop(url)        
    