#coding=utf-8

from CCPRestSDK import REST
import ConfigParser
import pandas as pd
import numpy as np
import os

accountSid = '8a216da86add82c9016ae239181701d9';

accountToken = 'ec2dd1d228704e2b982afab042ba29bf';

appId = '8a216da86add82c9016aed8d9d690e05';

serverIP = 'app.cloopen.com';

serverPort = '8883';

softVersion = '2013-12-26';

def sendTemplateSMS(to, datas, tempId):
    rest = REST(serverIP, serverPort, softVersion)
    rest.setAccount(accountSid, accountToken)
    rest.setAppId(appId)

    result = rest.sendTemplateSMS(to, datas, tempId)
    for k, v in result.iteritems():

        if k == 'templateSMS':
            for k, s in v.iteritems():
                print '%s:%s' % (k, s)
        else:
            print '%s:%s' % (k, v)


def send_sms_from_text_phonenumber():
    phones = []
    with open('phone', 'r') as f:
        for line in f.readlines():
            if line.strip() != "":
                phones.append(line.strip())
    phones.append('13967395631')
    phones.append('15757313553')
    print(len(phones))

    for group in max_numbers(phones):
        print(group)
        sendTemplateSMS(group, ["5月7日11:30"], 591885)

'''
5-8  10:30、11:30、12:30、13:30、15:30、16:30
5-9   9:30、10:30、11:30、12:30、13:30、16:30
5-10  9:30、10:30、11:30、12:30、13:30、14:30、15:30、16:30
'''
def send_sms_from_excel_fail():
    import pandas as pd
    from time import sleep
    import time
    # 车号 下车点	 电话 候车地点
    dfs = pd.read_excel(u"南洋未开行5-10.xlsx",dtype={'时间':np.datetime64})
    modeId = 592286 #未开行通知
    for index, row in dfs.iterrows():
        phone = row[u'电话']
        name = row[u'姓名'].encode('utf-8')
        data = [name,"5月10日","9:30、10:30、11:30、12:30、13:30、14:30、15:30、16:30"]
        sendTemplateSMS(phone, data, modeId)
        sleep(0.2)


def send_sms_from_excel_success():
    import pandas as pd
    from time import sleep
    import time
    # 车号 下车点	 电话 候车地点
    dfs = pd.read_excel(u"南洋5-10.xlsx",dtype={'时间':np.datetime64})
    modeId = 591885 #开行通知
    for index, row in dfs.iterrows():
        phone = row[u'电话']
        print(phone)
        name = row[u'姓名'].encode('utf-8')
        start_time = row[u'时间']
        date = "5月10日"+str(start_time)
        data = [name,date]
        sendTemplateSMS(phone, data, modeId)

        sleep(0.2)

def max_numbers(phones):
    tmp = []
    for i in range(1, len(phones) + 1):
        if i % 100 == 0:
            tmp.append(phones[i - 1])
            print(len(tmp))
            yield ','.join(tmp)
            tmp = []
        elif i == len(phones):
            tmp.append(phones[i - 1])
            print(len(tmp))
            yield ','.join(tmp)
        else:
            tmp.append(phones[i - 1])

def send_sms_from_excel_notrun():
    import pandas as pd
    from time import sleep
    import time
    # 车号 下车点	 电话 候车地点
    dfs = pd.read_excel(u"第一医院退票名单.xlsx")
    modeId = 612960  # 不开行通知
    for index, row in dfs.iterrows():
        phone = row[u'电话']
        print(phone)
        date = "7月1日"
        data = [date, date]
        sendTemplateSMS(phone, data, modeId)

        sleep(0.2)
if __name__ == '__main__':
    # 群发短信
    send_sms_from_excel_notrun()
    # send_sms_from_excel_fail()

