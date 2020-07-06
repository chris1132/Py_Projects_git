import numpy as np
import random
import matplotlib.pyplot as plt
import xlrd


def initial(N, fun, x_num, x_min, x_max, f_num,siteArray,len):
    P = []

    # 种群初始化以及产生lamda
    for i in range(N):
        # chromo 个体  chromo[] 封装个体数组
        chromo = []
        #生成个体


        for j in range(car_num):
            line_start_index = j * (site_num - 1) * 2 + car_num


        for j in range(x_num):

            print(j)
            '''
                取需求站点数据，封装个体
            '''
            if j<car_num :
                chromo.append(random.randint(1,3))
            else:
                chromo.append(random.randint(0,(len-1)))


        pop = Individual(chromo)
        P.append(pop)
    return P


class Individual():
    def __init__(self, x):
        self.x = x
        self.nnd = 0
        self.paretorank = 0
        if (fun == 'ZDT1'):
            f1 = float(x[0])
            sum1 = 0.0
            for i in range(x_num - 1):
                sum1 = sum1 + x[i + 1]
            g = float(1 + 9 * (sum1 / (x_num - 1)))
            f2 = g * (1 - (f1 / g) ** (0.5))
            self.f = [f1, f2]


def funfun(fun, car_num, site_num):
    if fun == 'ZDT1':
        f_num = 2;  # 目标函数个数
        x_num = car_num + 2 * (site_num - 1) * car_num  # 决策变量个数(个体里基因片段数)
        x_min = np.zeros((1, x_num))  # 决策变量的最小值
        x_max = np.ones((1, x_num))  # 决策变量的最大值
        zdt1 = np.loadtxt('ZDT1.txt')
        plt.scatter(zdt1[:, 0], zdt1[:, 1], marker='o', color='green', s=40)
        PP = zdt1
    return f_num, x_num, x_min, x_max, PP


data = xlrd.open_workbook('file/zhy.xlsx')
# 查看工作表
table = data.sheet_by_name("Sheet1")
global siteArray
siteArray = {}
for i in range(table.nrows):
    siteName = table.cell(i, 0).value
    lng = table.cell(i, 1).value
    lat = table.cell(i, 2).value
    sitePCount = table.cell(i, 3).value
    site = {}
    site["siteName"] = siteName
    site["lng"] = lng
    site["lat"] = lat
    site["sitePCount"] = sitePCount
    siteArray[i] = site
print(siteArray)

car_num = 6  # 投入车辆数
site_num = 3  # 最多允许停靠站点数
N = 100  # 种群规模
fun = 'ZDT1'  # 测试函数DTLZ2

f_num, x_num, x_min, x_max, PP = funfun(fun, car_num, site_num)
chromo = initial(N, fun, x_num, x_min, x_max, f_num,siteArray,len(siteArray))
