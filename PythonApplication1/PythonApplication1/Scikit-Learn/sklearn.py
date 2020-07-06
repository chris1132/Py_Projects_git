from urllib import request
import numpy as np

'''
study url http://python.jobbole.com/81721/
'''

url='http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data'
data=request.urlopen(url)
dataset = np.loadtxt(data,delimiter=',')
X = dataset[:,0:7]
y = dataset[:,8]
#print("x: {xvalue}".format(xvalue=X))
#print("y: {yvalue}".format(yvalue=y))

'''
数据标准化
from sklearn import preprocessing
'''
#nor_x=sklearn.preprocessing.normalize(X)
#stand_x=sklearn.preprocessing.scale(X)
#print(nor_x)
#print("___________")
#print(stand_x)

'''
特征的选取
from sklearn import metrics
from sklearn.ensemle import ExtraTreesClassifier
'''
#model = ExtraTreeClassifier()
#model.fit(X,y)
#print(model.feaure_importances)

#from sklearn.feature_selection import RFE
#from sklearn.linear_model import LogisticRegression
#model = LogisticRegression()
#rfe = RFE(model, 3)
#rfe = rfe.fit(X, y)
#print(rfe.support_)
#print(rfe.ranking_)

'''
逻辑回归
'''
#from sklearn import metrics
#from sklearn.linear_model import LogisticRegression
#model = LogisticRegression()
#model.fit(X, y)
#print(model)
#expected = y
#predicted = model.predict(X)
#print(metrics.classification_report(expected, predicted))
#print(metrics.confusion_matrix(expected, predicted))

'''
朴素贝叶斯
'''
#from sklearn import metrics
#from sklearn.naive_bayes import GaussianNB
#model = GaussianNB()
#model.fit(X, y)
#print(model)
#expected = y
#predicted = model.predict(X)
#print(metrics.classification_report(expected, predicted))
#print(metrics.confusion_matrix(expected, predicted))
'''
k-最近邻
'''
#from sklearn import metrics
#from sklearn.neighbors import KNeighborsClassifier
## fit a k-nearest neighbor model to the data
#model = KNeighborsClassifier()
#model.fit(X, y)
#print(model)
## make predictions
#expected = y
#predicted = model.predict(X)
## summarize the fit of the model
#print(metrics.classification_report(expected, predicted))
#print(metrics.confusion_matrix(expected, predicted))

'''
决策树
'''
#from sklearn import metrics
#from sklearn.tree import DecisionTreeClassifier
#model = DecisionTreeClassifier()
#model.fit(X, y)
#print(model)
#expected = y
#predicted = model.predict(X)
#print(metrics.classification_report(expected, predicted))
#print(metrics.confusion_matrix(expected, predicted))
'''
支持向量机
'''
#from sklearn import metrics
#from sklearn.svm import SVC
#model = SVC()
#model.fit(X, y)
#print(model)
#expected = y
#predicted = model.predict(X)
#print(metrics.classification_report(expected, predicted))
#print(metrics.confusion_matrix(expected, predicted))


#from sklearn.linear_model import Ridge
#from sklearn.grid_search import GridSearchCV
#alphas = np.array([1,0.1,0.01,0.001,0.0001,0])
#model = Ridge()
#grid = GridSearchCV(estimator=model, param_grid=dict(alpha=alphas))
#grid.fit(X, y)
#print(grid)
#print(grid.best_score_)
#print(grid.best_estimator_.alpha)

#from scipy.stats import uniform as sp_rand
#from sklearn.linear_model import Ridge
#from sklearn.grid_search import RandomizedSearchCV
#param_grid = {'alpha': sp_rand()}
#model = Ridge()
#rsearch = RandomizedSearchCV(estimator=model, param_distributions=param_grid, n_iter=100)
#rsearch.fit(X, y)
#print(rsearch)
#print(rsearch.best_score_)
#print(rsearch.best_estimator_.alpha)