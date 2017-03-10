#conding=utf-8
from pymongo import MongoClient
import jieba
import wordcloud
from wordcloud import WordCloud   #接受 空格分隔 字符串对象
import matplotlib.pyplot as plt

con = MongoClient()
db = con.liepin
datas = db.job_info #data from your mongodb

#返回以空格分隔的分词后的字符串
def after_jieba(item):
    skill = item['skill']
    ssk = jieba.cut(skill,cut_all=True)  #返回迭代器
    return " ".join(ssk).strip('\t\r\n')

s = ""
for i in datas.find():
    s = s +" "+ after_jieba(i)

if __name__ == '__main__':
    mywod = WordCloud(font_path='Kaiti.ttc',max_words=500,
            max_font_size=80).generate(s)
    plt.imshow(mywod)
    plt.axis('off')
    plt.show()