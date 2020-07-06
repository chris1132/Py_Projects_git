# -*- coding: utf-8 -*-

import requests  # 导入网页请求模块
import pymysql
import time, math


# 百度米转百度经纬度
def meter2Degree(x, y):
    url = "http://api.map.baidu.com/geoconv/v1/?coords=" + x + "," + y + "&from=6&to=5&output=json&ak=d82UUNUkRvsQcpuaeIAmHCFQktV3GVuX"
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}  # 构造请求头
    response = requests.get(url, headers=header)  # 发出请求
    answer = response.json()  # json化
    result = answer["result"]
    lng = result[0]["x"]
    lat = result[0]["y"]
    return lng, lat


# 提取百度米坐标字符串，转为经纬度坐标串
def coordinateToPoints(coordinates):
    points = ""
    if coordinates and coordinates.index("-") >= 0:
        coordinates = coordinates.split("-")
        temp_coordinates = coordinates[1]
        if temp_coordinates and temp_coordinates.index(",") >= 0:
            temp_coordinates = temp_coordinates.replace(";", "").split(",")
            temp_points = []
            for i in range(0, len(temp_coordinates), 2):
                x = temp_coordinates[i]
                y = temp_coordinates[i + 1]
                point = {}
                point["x"] = x
                point["y"] = y
                temp_points.append(point)

            for point in temp_points:
                x = point["x"]
                y = point["y"]
                lng, lat = meter2Degree(x, y)
                points += str(lng) + "," + str(lat) + ";"

    return points


# 获取边界
def getBorder(uid):
    url = "http://map.baidu.com/?pcevaname=pc4.1&qt=ext&ext_ver=new&l=12&uid=" + uid
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}  # 构造请求头
    response = requests.get(url, headers=header)  # 发出请求
    answer = response.json()  # json化
    content = answer["content"]
    points = ""

    if "geo" in content and content["geo"] != None and content["geo"] != "":
        geo = content["geo"]
        points = coordinateToPoints(geo)

    return points


def getUid(uname):
    url = "http://map.baidu.com/su?cid=334&type=0&pc_ver=2&wd=" + uname
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}  # 构造请求头
    response = requests.get(url, headers=header)  # 发出请求
    answer = response.json()  # json化
    content = answer["s"]
    points = ""

    for s in content :
        geo = content["geo"]
        points = coordinateToPoints(geo)

    return points

if __name__ == "__main__":
    getUid('艺墅家')

    # uid  = '42bc8dc4db7c4244be484230'
    # uname  = '艺墅家'
    # points = getBorder(uid).rstrip(';')
    # print(points)
    #
    # print("connecting mysql......\n")
    # db = pymysql.connect("39.100.48.77", "root", "Cetcjkdz123", "paratransit", port=3306,charset='utf8')  # 链接mysql数据库community
    # print("connect successfully,start creating table community_zh in database community\n")
    # cursor = db.cursor()  # 创建游标对象
    # insertsql = "insert into electronic_fence (blockName,location, cityCode,createTime) values ('"+uname+"','"+points+"','334',now())"
    # cursor.execute(insertsql)
    # db.commit()
    #
    # cursor.execute("SELECT id FROM `electronic_fence` ORDER BY id desc limit 1;")
    # cds = cursor.fetchall()
    #
    # insertsql2 = "insert into electronic_fence_community(reqtime,electronicFenceId,stopCode,count,cityCode,createTime)values (156,"+str(cds[0][0])+",'',0,'334',now())"
    # cursor.execute(insertsql2)
    # db.commit()