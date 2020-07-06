
from urllib import request
from bs4 import BeautifulSoup
import re
if __name__ == '__main__':
    url = 'http://www.qu.la/book/394/296472.html'
    #url = 'http://www.136book.com/huaqiangu/ebxeew/'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req=request.Request(url,headers=head)
    response=request.urlopen(req)
    html=response.read()

    soup=BeautifulSoup(html,'lxml')
    contents=soup.find('div',attrs={'id':'content'})

    rege=r'<div id="content">(.*)泰国.*'
    scon=re.findall(rege,str(contents.prettify()),re.S)
    with open('e:\save.txt','w') as f:
        for content in scon:
            f.write(str(content).replace("<br/>",""))
