# new day,new diff
# written in: 2020/10/30 20:50
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup as bs
import re
import os
#添加header，其中Referer是必须的,否则会返回403错误，User-Agent是必须的，这样才可以伪装成浏览器进行访问
header=\
{
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
     "referer": "https://beijing.8684.cn/"

    }
url = "https://beijing.8684.cn/"
keyword = "beijing"
#keyword = input("请输入搜索关键字：")
#转码
#keyword = urllib.parse.quote(keyword,"utf-8")

n = 0
j = 0

while(n<3000):
    error = 0
    rep = urllib.request.Request(url,headers=header)
    #打开网页
    rep = urllib.request.urlopen(rep)
    #获取网页内容

    html = rep.read().decode("utf-8")
    bs = bs(html)
    station = bs.find('title')
    print(station)

    #正则匹配
    p = re.compile(r"thumbURL.*?\.jpg")
    #获取正则匹配到的结果，返回list
    s = p.findall(html)

    if os.path.isdir("D://test_pic1") != True:
        os.makedirs("D://test_pic1")
    with open("test_pic1.txt","a") as f:
        #获取图片
        for i in s:
            i = i.replace('thumbURL":"','')
            print(i)
            f.write(i)
            f.write("\n")
            #保存图片
            urllib.request.urlretrieve(i,"D://test_pic1/pic.{num}.jpg".format(num=j))
            j+=1
        f.close()
print("总共爬取图片数为："+str(j))
