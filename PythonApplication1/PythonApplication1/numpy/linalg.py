#线性代数模块
import numpy as np
import numpy.random as random
a = np.array(np.arange(4))
np.linalg.norm(a)

b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
c = np.array([1, 0, 1])

np.dot(b,c)
d=np.dot(c,b.T)

#求矩阵的迹
print(np.trace(b))

#求矩阵的行列式值
print(np.linalg.det(b))

## 求矩阵的秩，2，不满秩，因为行与行之间等差
print(np.linalg.matrix_rank(b))

print(random.rand(1,3))