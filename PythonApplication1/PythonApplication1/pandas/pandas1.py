import numpy as np
import pandas as pd
obj = pd.Series([4,7,-5,3])
obj.index=['Bob','Steve','Jeff','Ryan']
#print(obj[2])
#print(obj[['a','d']])

sdata = {'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
states = ['California','Ohio','Oregon','Texas']
obj1 = pd.Series(sdata)
obj2 = pd.Series(sdata,index=states)

data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],'year':[2000,2001,2002,2001,2002],'pop':[1.5,1.7,3.6,2.4,2.9]}
frame = pd.DataFrame(data,columns=['year','state','pop','de'],index=['one','two','three','four','five'])
#print(frame.ix['three'])
#print(frame['year'][1])
frame['de']=1

frame2 = pd.DataFrame(np.arange(15).reshape(5,3),columns=['1---','2---','3---'],
                      index=['one','two','three','four','five'])
frame['new']=frame['state']=='Ohio'
#print(frame2)
#print(frame2['1---']['two'])
#print(frame2.ix['two','1---'])

pop = {'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2002:3.6}}
frame3 = pd.DataFrame(pop)
pdata = {'Ohio':frame3['Ohio'][:-1],'Nevada':frame3['Nevada'][:2]}
print(pd.DataFrame(pdata))

obj3=obj.reindex(['Ryan','Bob','Steve','Jeff','Chris'],fill_value=0)
#print(obj3.drop('Chris',axis=1))

frame = pd.DataFrame(np.arange(8).reshape(2,4),index=['two','one'],columns=['d','b','c','a'])
print(frame)
print(frame.sort_index(axis=1),ascending=False)