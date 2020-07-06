import numpy as np
import pandas as pd


f=pd.DataFrame({'key1':['a','a','b','b','a'],'key2':['one','two','one','two','one'],'data1':np.arange(5),'data2':np.random.randn(5)})
group=f['data1'].groupby([f['key1'],f['key2']])
group.size()
mean = group.mean()
mean.unstack()
#for (name1,name2),group1 in group:
#    print("name1:",name1)
#    print("name2:",name2)
#    print("group:",group)
lists = list(group)
pieces = dict(lists)


people = pd.DataFrame(np.random.randn(5,5),columns=['a','b','c','d','e'],
                   index=['Joe','Steve','Wes','Jim','Travis'])
people.ix[2:3,['b','c']]
mapping = {'a':'red','b':'red','c':'blue','d':'blue','e':'red','f':'orange'}
#print(people)
#print('-------------------------')
by_column = people.groupby(mapping,axis=1)
#print(by_column.sum())
#print('-------------------------')
mapping2 = {'Joe':'one','Steve':'two','Wes':'one','Jim':'three','Travis':'two'}
by_row = people.groupby(mapping2,axis=0)
#by_row.sum())
by_len = people.groupby(len).sum()

tips = pd.read_csv("../csv-data/tips.csv")
tips['tip_pct']=tips['tip']/tips['total_bill']
grouped = tips.groupby(['sex','smoker'])
print(grouped)
print('-------------------------')
frouped_pct = grouped['tip_pct']
print(frouped_pct)
print('-------------------------')
print(group_pct.agg('mean'))