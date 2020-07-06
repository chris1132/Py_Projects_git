from urllib import request
from bs4 import BeautifulSoup
import re
url = "http://www.zjtxztb.gov.cn/txcms/jsgczhaobgg/index_{page}.htm"

for i in range(35):
    url_page = url.format(page=(i+1))
    req = request.Request(url_page)
    response = request.urlopen(req)
    html = response
    soup = BeautifulSoup(html,"lxml")
    conts = soup.find_all("div",class_="bg3 FloatL")
    html_chil = str(conts)
    soup_chil = BeautifulSoup(html_chil, "lxml")
    newc = soup_chil.find_all(text=re.compile(u"[\u4e00-\u9fa5]|[a-zA-Z]+"))
    for con in newc:
        if con.find("公交")>0:
            print("第",i+1,"页：",con)
