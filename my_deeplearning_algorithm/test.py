# -- coding: utf-8 --
from functools import reduce
class percept(object):

    def __init__(self,inp_num,activator):
        self.activator = activator
        self.weights = [0.0 for _ in range(inp_num)]
        self.bias = 0.0


    def __str__(self):
        return 'weight: {}, bias:{}'.format(self.weights,self.bias)


    def train(self,input_vecs,labels,iteration,rate):
        for i in range(iteration):
            sample = zip(input_vecs,labels)
            for(input_vec,label) in sample:
                output = self.predict(input_vec)
                print(output)
                #delta = output*(1-output)*(label-output)
                delta = label-output
                self.weights=map(lambda x: x[1]+ rate * delta * x[0],zip(input_vec, self.weights))
                self.bias += delta+rate

    def predict(self,input_vec):
        return self.activator(
            reduce(lambda a, b: a + b,
                   map(lambda x : x[0] * x[1],
                       zip(input_vec, self.weights))
                   , 0.0) + self.bias)



def sigmoid(x):
    return 1/(1+exp(-x))

def f(x):
    return 1 if x>0 else 0

if __name__=='__main__':
    h = [0.0 for _ in range(8)]
    input_vecs = [[1,1], [0,0], [1,0], [0,1]]
    labels = [1,0,0,0]
    p = percept(2,f)
    p.train(input_vecs,labels,10,0.1)
    print(p.weights)
    print(p.predict([0,1]))
    print(p.predict([1,1]))
    print(p.predict([0,0]))
    print(p.predict([1,0]))
    

    #var = 1
    #while var == 1: 
    #    s=input('please input£º')
    #    if len(s):
    #        k,v = s.split(",")
    #        print(p.predict([int(k),int(v)]))
    #    else:
    #        v=2
            
