from functools import reduce
import numpy as np

class Perceptron(object):
    def __init__(self,activator,num):
        self.weights = [0.0 for _ in range(num)]
        self.bias = 0.0
        self.activator = activator

    def __str__(self):
        return 'weights\t:%s\nbias\t:%f\n' % (list(self.weights), self.bias)

    def train(self,input_values,labels,train_num,rate):
        for i in range(train_num):
            data = zip(input_values,labels)
            for input_val,label in data:
                #input_vals [x1,x2]
                #weights [w1,w2]
                #outpt = x1*w1+x2*w2+b
                output =self.predict(input_val)
                delt = label - output
                #Wi=Wi+seta*(label - output)*input_val
                self.weights = list(map(lambda x:x[1]+rate*delt*x[0],
                                        zip(input_val,self.weights)))
                self.bias = self.bias + rate*delt

    def predict(self,input_val):
        return self.activator(
            reduce(lambda x,y:x+y, 
                   map(lambda x: x[0]*x[1],
                       zip(input_val,self.weights)))+self.bias)

def f(x):
    return 1 if x>0 else 0

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoidDao(x):
    return (-x)/(np.exp(-2*x))

if __name__ == '__main__':
    input_values = [[1,1],[1,0],[0,1],[0,0]]
    labels = [1,0,0,0]
    percep = Perceptron(f,len(input_values[0]))
    percep.train(input_values,labels,10,0.1)

    print(percep)
    print(percep.predict([1,1]))
    print(percep.predict([1,0]))
    print(percep.predict([1,0]))
    print(percep.predict([0,0]))
    print(percep.predict([0,1]))

if __name__=='perceptron':
    print("import")
