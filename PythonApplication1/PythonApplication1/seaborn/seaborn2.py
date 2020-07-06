import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns

#sns.set_style("dark")
#x = np.random.normal(size=100)
##sns.distplot(x,bins=20,kde=True,hist=False,rug=True)
#sns.kdeplot(x,bw=1,label='ss',shade=True)



'''
hexbin
'''
#mean,cov=[0,1],[(1,0.5),(0.5,1)]
#x,y = np.random.multivariate_normal(mean,cov,1000).T
#sns.jointplot(x=x,y=y,kind='hex')
#plt.show()


'''
核密度估计
'''
#mean,cov=[0,1],[(1,0.5),(0.5,1)]
#data = np.random.multivariate_normal(mean,cov,200)
#df = pd.DataFrame(data,columns=['x','y'])
#sns.jointplot(x='x',y='y',data=df,kind='kde')
#plt.show()
'''
_____
'''
#mean,cov=[0,1],[(1,0.5),(0.5,1)]
#data = np.random.multivariate_normal(mean,cov,200)
#df = pd.DataFrame(data,columns=['x','y'])
#f,ax=plt.subplots(figsize=(6,6))
#sns.kdeplot(df.x,df.y,ax=ax)
#sns.rugplot(df.x,color='g',ax=ax)
#sns.rugplot(df.y,vertical=True,ax=ax)
#plt.show()
'''
_____
'''
#mean,cov=[0,1],[(1,0.5),(0.5,1)]
#data = np.random.multivariate_normal(mean,cov,200)
#df = pd.DataFrame(data,columns=['x','y'])
#f,ax=plt.subplots(figsize=(6,6))
#cmap = sns.cubehelix_palette(as_cmap=True,dark=0,light=1,reverse=True)
#sns.kdeplot(df.x,df.y,cmap=cmap,n_levels=60,shade=60)
#plt.show()
'''
_____
'''
#iris = sns.load_dataset('iris')
#sns.pairplot(iris)
#plt.show()
'''
_____
'''
#iris = sns.load_dataset('iris')
#g = sns.PairGrid(iris)
#g.map_diag(sns.kdeplot)
#g.map_offdiag(sns.kdeplot, cmap="Blues_d", n_levels=6)
#plt.show()