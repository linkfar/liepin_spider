import requests
from bs4 import BeautifulSoup
url_pools = []  #可以使用数据库存储

proxies = {
    "http":"http://test1:123@101.231.135.147:808"
} #100个请求也可以不用代理池


index = "https://www.liepin.com/zhaopin/?industries=&dqs=020&salary=&jobKind=&pubTime=&compkind=&compscale=&industryType=&searchType=1&clean_condition=&isAnalysis=&init=1&sortFlag=15&flushckid=1&fromSearchBtn=2&headckid=3a7c11d0ba0fd4fa&key=python"

headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",\
           "Accept-Encoding":"gzip, deflate, sdch, br",\
           "Accept-Language":"zh-CN,zh;q=0.8",\
           "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",\
           "Host":"www.liepin.com",\
           }           
n = 1
def gen_pool(index):
    print(index)
    try:
        r = requests.get(index,headers=headers,proxies=None)
        soup = BeautifulSoup(r.text,"lxml")
        #find info url
        ch1_page_hrefs = soup.find_all("div",class_="job-info")
        for href in ch1_page_hrefs:
            url_pools.append(href.find('a')['href'])
        #find next page
        index = soup.find("a",string="下一页")['href']
        if index!="javascript:;":
            time.sleep(10)
            gen_pool(index)    #处理分页process split pages
        else:
            print("Done")
    except:
        print(index)

import time
import csv
if __name__ == "__main__":
    gen_pool(index)
    with open('url_pools.csv', 'w') as f:
        w = csv.writer(f)
        w.writerow(url_pools)
    f.close()




