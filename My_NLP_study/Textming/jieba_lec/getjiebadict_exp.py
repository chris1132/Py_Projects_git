from urllib import request
import re
from bs4 import BeautifulSoup

url="http://blog.sina.com.cn/s/blog_628cc2b70102wb7z.html"
req = request.Request(url)
response = request.urlopen(req)
html = response.read()
#html = open("dict/index.html",'r',encoding="utf-8")
soup = BeautifulSoup(html,'lxml')
# cont_arr = soup.tbody.find_all(text=re.compile(u"[\u4e00-\u9fa5]|[a-zA-Z]+"))
cont_arr = soup.tbody.find_all("td")
i=1
with open('dict/save_jieba.txt','w',encoding="utf-8") as f:
    appstr=""
    for cont in cont_arr:
        appstr+=str(cont).replace('\n','')+"  "
        if i%3==0:
            soup2 = BeautifulSoup(appstr,'lxml')
            con = soup2.find_all(text=re.compile(u"[\u4e00-\u9fa5]|[a-zA-Z]+"))
            appstr = ""
            f.write("   ".join(con)+"\n")
        i+=1