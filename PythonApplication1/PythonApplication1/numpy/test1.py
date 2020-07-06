#from functools import reduce
#h=map(lambda x:x**2,[1,2,3,4])
#r=reduce(lambda x,y:x+y,[1,2,3])
#f=filter(lambda x:x%2,[1,2,3,4,5])
#for i in h:
#    print(i)
#print("---------")
#print(r)
#print("---------")
#for i in f:
#    print(i)


#ary=[sum(x) for x in zip([1,2,3],[4,5,7,8])]
#iter_odd = (x for x in [1, 2, 3, 4, 5] if x % 2)

#with open("D:/VS_Projects/PythonApplication1/PythonApplication1/numpy/name_age.txt",'r') as read,open("D:/VS_Projects/PythonApplication1/PythonApplication1/numpy/age_name.txt",'w') as write:
#    lines = read.readlines()
#    for line in lines:
#        name,age=line.rstrip().split(',')
#        write.write("{},{}\n".format(age,name))


s=input("please input:")
k,v=s.split(",")
print([int(k),int(v)])
