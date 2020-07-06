
from urllib import request
from bs4 import BeautifulSoup
if __name__ == '__main__':
    url = 'http://www.qu.la/book/394/'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req=request.Request(url,headers=head)
    response=request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html,'lxml')
#    print(soup.title.string)
    soup_text = soup.find('div',id='list')
    coup_contents = soup_text.dl.contents
    for i in range(len(coup_contents)):
        if coup_contents[i] !='\n' and i>2:
            print(coup_contents[i].text)
            print(coup_contents[i].a.get('href'))

    #url = 'http://www.136book.com/huaqiangu/'
    #head = {}
    #head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    #req = request.Request(url, headers = head)
    #response = request.urlopen(req)
    #html = response.read()
    #soup = BeautifulSoup(html, 'lxml')
    #soup_texts = soup.find('div', id = 'book_detail', class_= 'box1').find_next('div')
    #coup_contents = soup_texts.ol.contents
    #for i in range(len(coup_contents)):
    #    link = coup_contents[i]
    #    if link != '\n':
    #        print(link.text + ':  ', link.a.get('href'))
