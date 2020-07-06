import matplotlib.pyplot as plt
from functools import reduce
plt.figure('test')

dog=plt.imread("D:/VS_Projects/VS_Projects_git/PythonApplication1/PythonApplication1/dog.png")

plt.imshow(dog)

# Z是上小节生成的随机图案，img0就是Z，img1是Z做了个简单的变换
img0 = dog 
img1 = 2*dog + reduce(lambda x,y:x+y,[0.1,0.2,0.1,0.25])

# cmap指定为'gray'用来显示灰度图
fig = plt.figure('Auto Normalized Visualization')
ax0 = fig.add_subplot(121)
ax0.imshow(img0, cmap='gray')

ax1 = fig.add_subplot(122)
ax1.imshow(img1, cmap='gray')

plt.show()