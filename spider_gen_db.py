"""
hire_info: title,company {div class=title-info/h1 string /a string}


job_info: div class="content content-word"


"""

import csv
import requests
import time
from bs4 import BeautifulSoup

headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",\
           "Accept-Encoding":"gzip, deflate, sdch, br",\
           "Accept-Language":"zh-CN,zh;q=0.8",\
           "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",\
           "Host":"www.liepin.com",\
           }
proxies = {"http":"http://test1:123@101.231.135.147:808"} #最好还是添加代理池分布式爬取，推荐 IPProxyTool


#links from crawler
with open("url_pools.csv",'r') as f:
    f_csv = csv.reader(f)
    info_pools = []
    for i in f_csv:
        info_pools.append(i)
    info_pools = info_pools[0]
f.close()

from pymongo import MongoClient
client = MongoClient() #默认连接 localhost:27017
db = client.testdb
collections = db.job_infoo

"""
db model:
{
"company":company,
"salary":salary,
"skill":skill,
"position",
}

就不创建数据库对象了
"""

def result(url):
    r = requests.get(url,headers=headers,proxies=proxies)
    soup = BeautifulSoup(r.text,"lxml")
    position = soup.find('div',class_="title-info").find('h1').string.lstrip()
    try:
        company = soup.find('div', class_="title-info").find('h3').find('a').string.lstrip()
    except:
        company = soup.find('div', class_="title-info").find('h3').string.lstrip()
    skill = soup.find('div',class_="content content-word").text.lstrip()
    salary = soup.find('p',class_="job-item-title").text.lstrip()

    raw = {"company":company,"position":position,"skill":skill,"salary":salary}
    collections.insert_one(raw).inserted_id

def test(pool):
    oks = 1
    fails = 1
    for link in pool:
        try:
            result(link)
            print("log info: %s success, request success %d" %(link,oks))
            oks+=1
        except:
            print("log info: %s error, request error %d,"%(link,fails))
            fails+=1
        time.sleep(5)
        
if __name__ == '__main__':
    test(info_pools)
