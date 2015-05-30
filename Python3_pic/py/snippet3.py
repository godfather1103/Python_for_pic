import urllib
import urllib.request

import time 
import random 
from bs4 import BeautifulSoup
def user_agent(url): 
    req_timeout = 20
    req = urllib.request.Request(url,headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    page = urllib.request.urlopen(req,None,req_timeout)
    html = page.read().decode()
    return html 
def pic(url,count_limt):
    count = 0 
    soup = BeautifulSoup(user_agent(url))
    img = soup.find_all(['img'])
    for pic in img:
        if count >= count_limt:
           return count_limt
        link = pic.get('src')
        #print(link)       
        if link is None:
            continue
        if  link[-3:] in ['gif','png']:
            continue
        try: 
            content = urllib.request.urlopen(link).read()
            if len(content)<=9999:
                continue
        except:
            continue    
        flag = random.randint(0, 1000)
        name = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))+str(flag)
        with open(u'D:\\JSP\\pic'+'\\'+name+link[-5:],'wb') as code:
            code.write(content)
            count += 1
            print (len(content))
            print (name)
            #print (count)
    return count        