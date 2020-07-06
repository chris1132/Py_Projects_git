from urllib import parse
from urllib import request
from bs4 import BeautifulSoup
import re

import jieba
import jieba.posseg as posseg

from colorama import init,Fore
init()

def open_webbrowser_count(question,choices):
    print('\n-- 方法2： 题目+选项搜索结果计数法 --\n')
    print('Question: ' + question)
    if '不是' in question:
        print('**请注意此题为否定题,选计数最少的**')

    #TODO jieba
    wordlist = posseg.cut(question)

    head = {}
    head['User-Agent'] =  'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
    counts = []
    for i in range(len(choices)):
        url = 'https://www.baidu.com/s?wd='+parse.quote((question + choices[i]))
        req = request.Request(url=url,headers=head)
        response = request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html,'lxml')
        te = soup.find('div',attrs={'class':'nums'})
        count = re.findall("百度为您找到相关结果约(.*)个",str(te),re.S)
        counts.append(int(count[0].replace(",","")))
    output(choices, counts)

def output(choices, counts):
    counts = list(map(int, counts))
    #print(choices, counts)
    # 计数最高
    index_max = counts.index(max(counts))
    # 计数最少
    index_min = counts.index(min(counts))

    if index_max == index_min:
        print(Fore.RED + "高低计数相等此方法失效！" + Fore.RESET)
        return

    for i in range(len(choices)):
        print()
        if i == index_max:
            # 绿色为计数最高的答案
            print(Fore.GREEN + "{0} : {1} ".format(choices[i], counts[i]) + Fore.RESET)
        elif i == index_min:
            # 红色为计数最低的答案
            print(Fore.MAGENTA + "{0} : {1}".format(choices[i], counts[i]) + Fore.RESET)
        else:
            print("{0} : {1}".format(choices[i], counts[i]))

if __name__ == '__main__':
    question = '新装修的房子通常哪种化学物质含量会比较高?'
    choices = ['甲醛', '苯', '甲醇']
    open_webbrowser_count(question, choices)