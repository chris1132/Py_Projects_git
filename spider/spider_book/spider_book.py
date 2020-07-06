from urllib import request
from bs4 import BeautifulSoup
import re
if __name__ == '__main__':
    #url = 'http://www.136book.com/huaqiangu/'
    #head = {}
    #head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    #req = request.Request(url, headers = head)
    #response = request.urlopen(req)
    #html = response.read()
    #soup = BeautifulSoup(html, 'lxml')
    #soup_texts = soup.find('div', id = 'book_detail', class_= 'box1').find_next('div')
    #f = open('F:/huaqiangu.txt','w')
    #for link in soup_texts.ol.children:
    #    if link != '\n':
    #        download_url = link.a.get('href')
    #        download_req = request.Request(download_url, headers = head)
    #        download_response = request.urlopen(download_req)
    #        download_html = download_response.read()
    #        download_soup = BeautifulSoup(download_html, 'lxml')
    #        download_soup_texts = download_soup.find('div', id = 'content')
    #        download_soup_texts = download_soup_texts.text
    #        f.write(link.text + '\n\n')
    #        f.write(download_soup_texts)
    #        f.write('\n\n')
    #f.close()


    url = 'http://www.qu.la/book/394/'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(url, headers = head)
    response = request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    soup_texts = soup.find('div',id='list')
    print(soup_texts.prettify())
    with open('E:/'+soup.title.string+'.txt','w') as f:
        coup_contents = soup_texts.dl.contents
        for i in range(len(coup_contents)):
            link = coup_contents[i]
            if link != '\n' and i>2:
                download_url = 'http://www.qu.la'+link.a.get('href')
                download_req = request.Request(download_url, headers = head)
                download_response = request.urlopen(download_req)
                download_html = download_response.read()
                download_soup = BeautifulSoup(download_html, 'lxml')
                download_soup_texts = download_soup.find('div', id = 'content')
                download_soup_texts = download_soup_texts.prettify()
                rege=r'<div id="content">(.*)泰国.*'
                scon=re.findall(rege,str(download_soup_texts),re.S)
                for content in scon:
                    f.write(str(content).replace("<br/>",""))