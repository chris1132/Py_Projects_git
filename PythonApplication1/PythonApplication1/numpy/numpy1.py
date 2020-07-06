import numpy as np


# 3x3的浮点型2维数组，并且初始化所有元素值为1
e=np.ones((3,3),dtype=np.float)

# 创建一个一维数组，元素值是把3重复4次，array([3, 3, 3, 3])
f=np.repeat(3,4)

# 2x2x3的无符号8位整型3维数组，并且初始化所有元素值为0
g=np.zeros((3,2,3))
# print(g)
#转为float型
h=g.astype(np.float)

l = np.arange(10)      	# 类似range，array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
m = np.linspace(0, 6, 5)# 等差数列，0到6之间5个取值，array([ 0., 1.5, 3., 4.5, 6.])

#对0-23的一位数组，分为4个维度，每个维度2行3列 
l=np.arange(24).reshape(4,2,3)

#按照下标位置进行划分，将数组分为左2个元素，右3个元素的3个数组
h=np.split(np.arange(9),[2,-3])

l0=np.arange(6).reshape((2,3))
l1=np.arange(6,12).reshape((2,3))
# print(l1)
#vstack是指沿着纵轴拼接两个array，vertical
m=np.hstack((l0,l1))
#hstack是指沿着横轴拼接两个array，horizontal
m=np.hstack((l0,l1))
#stack不是拼接而是在输入array的基础上增加一个新的维度 l0一个维度，l1一个维度
s=np.stack((l0,l1))

#rot90 逆时针旋转90度，第二个参数是旋转次数
#transpose 默认转置将维度倒序，对于2维就是横纵轴互换
v=np.rot90(s[1].transpose(),1)
print(s[1].transpose())
print(v)
#transpose((2,0,1))按指定轴进行转置
#array([[[ 0,  3],
#        [ 6,  9]],
#       [[ 1,  4],
#        [ 7, 10]],
#       [[ 2,  5],
#        [ 8, 11]]])
print("---------------------")
print(s)
print(s.transpose((2,0,1)))
print("---------------------")
a=np.arange(12).reshape(1,4,3)


print(a)
print("---------------------")
#fliplr
#沿纵轴左右翻转
#array([[ 8,  4,  0],
#       [ 9,  5,  1],
#       [10,  6,  2],
#       [11,  7,  3]])
v=np.fliplr(a)

#flipud沿水平轴上下翻转
#array([[ 3,  7, 11],
#       [ 2,  6, 10],
#       [ 1,  5,  9],
#       [ 0,  4,  8]])
h=np.flipud(a)
print(v)
print("---------------------")
print(h)