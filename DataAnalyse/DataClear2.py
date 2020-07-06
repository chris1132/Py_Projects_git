import pandas as pd
from pandas import Series,DataFrame


def dataFrameFun():
    df1 = DataFrame({"name":['zhangfei','likui','liubei1','a','b'],'data1':range(5)})
    df2 = DataFrame({"name":['b','s','e','zhangfei','t'],'data2':range(5)})

    # df3 = pd.merge(df1,df2,on='name')
    # print_f(df3)
    df4 = pd.merge(df1,df2,how='left')
    print_f(df4)

def print_f(value,title=""):
    print(title,"-----------------")
    print(value)
    print(title+"-----------------")


if __name__=="__main__":
    dataFrameFun()