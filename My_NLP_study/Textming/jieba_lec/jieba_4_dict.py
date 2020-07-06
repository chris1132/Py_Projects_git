import jieba

def cuttest(test):
    r = jieba.cut(test,cut_all=False)
    print(" ".join(r))

def testcase():
    cuttest("这是一个伸手不见五指的黑夜。我叫孙悟空，我爱北京，我爱Python和C++。")
    cuttest("我不喜欢日本和服。")
    cuttest("雷猴回归人间。")
    cuttest("工信干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作")
    cuttest("我需要廉租房")
    cuttest("永和服装饰品有限公司")
    cuttest("我爱北京天安门")
    cuttest("abc")
    cuttest("隐马尔可夫")
    cuttest("雷猴是个好网站")
    cuttest("kis51888,15701350422,15900813203")

if __name__=="__mian__":
    testcase()
    jieba.set_dictionary("dict/dict_big.txt")
    print("================================")
    testcase()

