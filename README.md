### spider_link _pools.py 
抓取liepin.com关于python关键词搜索信息的所有招聘岗位的链接

生成url_pools.csv的链接池

---
### spider_gen _db.py
爬取招聘岗位的非结构性数据，构造字典对象输入MongoDB

documents structure

		job_info:
		{
		
			“company”:company
			
			"salary":salary
			
			"position":position
			
			"skill":skill
		
			“_id”:Obj
		}

### analyze.py
利用jieba分词API，解构skill数据（skill包含招聘方的具体需求和要求）

利用wordcloud生成高频数据展示图

### Result
从分词结果的频度可以看出，截止 2017-03-10 liepin.com 有关招聘方对python工程师在数据分析方向有很大的需求
![result](https://github.com/sstoner/liepin_spider/tree/master/demo/demo.png)
