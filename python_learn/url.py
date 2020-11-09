# new day,new diff
# written in: 2020/11/1 16:24
from urllib.request import urlopen as ulp
from bs4 import BeautifulSoup as bs
html  = ulp(r"http://www.jueshitangmen.info/tian-meng-bing-can-11.html").read().decode("utf_8")
print(html)
print("=================")
soup = bs(html,features="lxml")
all_p=soup.find_all('p')
print(all_p)
print("==================")
for i in all_p:
    print("\t",i.get_text())