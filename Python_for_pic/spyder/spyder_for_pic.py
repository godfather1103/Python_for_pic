# -*- coding: utf-8 -*-
"""
Created on Tue May 26 09:13:20 2015

@author: ccb 
""" 

import urllib2
from bs4 import BeautifulSoup
import socket
import time
import random


#伪装浏览器,以免被封
def user_agent(url):
    req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    req_timeout = 20
    try:
        req = urllib2.Request(url,None,req_header)
        page = urllib2.urlopen(req,None,req_timeout)
        html = page
    except urllib2.URLError as e:
        print (e.message)
    except socket.timeout as e:
        user_agent(url)
    return html

def pic(url,count_limt):
    count = 0
    soup = BeautifulSoup(user_agent(url))
    img = soup.find_all(['img'])
    for pic in img:
            link = pic.get('src')
            
            if link is None:
                continue
            if  link[-3:] in ['gif']:
                continue
            try:
                #读取图片到content
                #content = urllib2.urlopen(link).read()
                content = user_agent(link).read()
                #定义图片大小，过滤小图片，例如：20480过滤小于20480B的图片
                if len(content)<=20480:
                    continue
                #print len(content)
            except:
                continue    
            flag = random.randint(0, 1000)
            #设置图片的名称
            name = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))+str(flag)
            #D:\\JSP\\pic书图片的存储路径
            with open(u'D:\\JSP\\pic'+'\\'+name+link[-5:],'wb') as code:
                code.write(content)
                count += 1
                #print count
            if count == count_limt:
               return count_limt   
    return count