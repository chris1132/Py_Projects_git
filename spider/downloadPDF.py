# coding = UTF-8
from urllib import request
import os
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from pathlib import Path
def getFile(url):
    file_name = url.split('/')[-1]
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(url, headers=head)
    u = request.urlopen(req)
    f = open(file_name, 'wb')

    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()
    print ("Sucessful to download" + " " + file_name)



def test_job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    os.chdir(os.path.join('E:\\', 'pdf_download'))
    for i in range(3):
        url = "http://jxrb.cnjxol.com/page/1/2019-08/23/0" + str(i + 1) + "/201908230" + str(i + 1) + "_pdf.pdf"
        getFile(url)

if __name__=="__main__":
    path = 'E:\\pdf_download'
    my_file = Path(path)
    if my_file.exists():
        print("file exit")
    else:
        os.mkdir(path)
        print("create file path")

    scheduler = BlockingScheduler()
    scheduler.add_job(test_job, 'interval', seconds=15, id='test_job')
    scheduler.start()