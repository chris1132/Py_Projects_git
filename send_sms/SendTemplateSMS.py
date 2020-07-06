# coding:utf-8


from CCPRestSDK import REST
import ConfigParser
import pandas as pd
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


def group_send():
    """
    群发
    """
    """
    各位家长，您好！辅助公交现已开通{1}线路招募通道，请在微信小程序搜索“嘉兴辅助公交”并进行购票, 首批招募截止日期为{2}。
    如已有线路未能满足您的需求，您可提交需求并等待后续招募。如有疑问，请拨打服务热线(0573-82131705)反馈。
    
    各位家长好，感谢您的耐心等待！根据所有已提交需求，辅助公交线路信息更新完毕，请您前往{1}进行查看与购买，购票截止日期为{2}。
    各位家长好，您购买的{1}辅助公交班车在{2}正式开始运行，请准时乘坐{3}发车且标识为{4}的公交车。如不乘坐请在小程序中请假，谢谢。
    """
    phones = []
    with open('phone_36', 'r') as f:
        for line in f.readlines():
            if line.strip() != "":
                phones.append(line.strip())
    phones.append('13967395631')
    phones.append('13738260356')
    print(len(phones))

    for group in max_numbers(phones):
        print(group)
        # sendTemplateSMS(group,[], 563452)
        # sendTemplateSMS(group,["1月15日明天(周三)","辅51-54","10:50","辅55-58","11:30","辅59-62","12:00。15日晚辅76-78正常运行。1月16日辅79发车时间12:00"], 480617)


def each_custom_send():
    # 按车辆发送
    basepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'file')
    for i in range(79, 80):
        df = pd.read_excel(u"辅" + str(i) + u".xlsx")
        global time, busnum, starttime
        for index, row in df.iterrows():
            time = row[u'时间段'].encode("utf-8")
            starttime = "每周六" + row[u'发车时间'].encode("utf-8")
            busnum = row[u'车号'].encode("utf-8")
            # print("各位家长好，您购买的{}辅助公交班车在{}正式开始运行，请准时乘坐{}发车且标识为{}的公交车。如不乘坐请在小程序中请假，谢谢。{}"
            # .format(row[u'时间段'].encode("utf-8"),'9月7日', "每周六"+row[u'发车时间'].encode("utf-8"),row[u'车号'].encode("utf-8"), row[u'电话']))

            # sendTemplateSMS(row[u'电话'],[row[u'时间段'].encode("utf-8"),'9月7日',"每周六"+row[u'发车时间'].encode("utf-8"),row[u'车号'].encode("utf-8")], 471378)

        # print("{}各位家长好，您购买的{}辅助公交班车在{}正式开始运行，请准时乘坐{}发车且标识为{}的公交车。如不乘坐请在小程序中请假，谢谢。"
        # .format('13967395631',time,'9月7日',starttime, busnum))
        # sendTemplateSMS('13967395631',[time,'9月7日',starttime, busnum], 471378)
        # sendTemplateSMS('13738260356',[time,'9月7日',starttime, busnum], 471378)


def send_sms_from_excel():
    import pandas as pd
    from time import sleep
    '''
    【嘉科电子】您购买{1}该周的辅助公交车票将从{2}运行，
    请乘坐标志为:{3}公交车。上班车辆的发车时间为{4}，
    请在您购买的站点({5})上车。下班车辆的发车时间为{6}，上车地点为{7}。{8}
    '''
    # data = ['2月24日-2月28日', '2月24日', '辅81', "7:20", "进度九月", "17:15", "东门", "【明日首次运行通勤线，为保证您乘车顺利，请尽早在站点候车。谢谢!】"]

    # send_sms_one_by_one()
    # each_custom_send()
    # sendTemplateSMS('13738260356', data, 563828)
    # group_send()

    # 车号 下车点	 电话 候车地点
    dfs = pd.read_excel(u"辅95.xlsx")
    for index, row in dfs.iterrows():
        phone = row[u'电话']

        busnumber = row[u'车号'].encode('utf-8')
        station = row[u'下车点'].encode('utf-8')
        place = row[u'候车地点'].encode('utf-8')

        tips = "【明日首次运行通勤线，为保证您乘车顺利，请尽早在站点候车。谢谢!】"
        startTime = "7:00"

        # data = ['2月24日-2月28日', '2月24日', '辅81', "7:20", "36所智慧园", "17:15", "东门", "【明日首次运行通勤线，为保证您乘车顺利，请尽早在站点候车。谢谢!】"]

        data = ['2月24日-2月28日', '2月24日', busnumber, startTime, station, "17:15", place, tips]

        # print(phone, data)
        # sendTemplateSMS(phone, data, 563828)

        if row[u'姓名'] == u'朱耀':
            print(phone, data)
            # sendTemplateSMS(phone, data, 563828)
        # sleep(0.2)


def send_sms_from_text_phonenumber():
    phones = []
    with open('phone', 'r') as f:
        for line in f.readlines():
            if line.strip() != "":
                phones.append(line.strip())
    phones.append('13967395631')
    phones.append('13738260356')
    print(len(phones))

    for group in max_numbers(phones):
        print(group)
        sendTemplateSMS(group, [], 584141)


if __name__ == '__main__':
    # TODO 群发短信
    send_sms_from_text_phonenumber()

    # Todo 测试短信
    # sendTemplateSMS('13967395631,13738260356', [], 584141)
