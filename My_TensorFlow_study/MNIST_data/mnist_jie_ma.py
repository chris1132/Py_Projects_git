# -*- coding: utf-8 -*-
from PIL import Image
import struct
import numpy as np

def read_image(filename):
  f = open(filename, 'rb')
  index = 0
  buf = f.read()
  f.close()
  magic, images, rows, columns = struct.unpack_from('>IIII' , buf , index)
  index += struct.calcsize('>IIII')
  for i in range(images):
      image = Image.new('L', (columns, rows))

      for x in range(rows):
          for y in range(columns):
              if i>9486:
                  image.putpixel((y, x), int(struct.unpack_from('>B', buf, index)[0]))
                  index += struct.calcsize('>B')
                  print('save ' + str(i) + 'image')
                  image.save('D:/Python_Resource/MNIST_data/test/' + str(i) + '.png')

def read_label(filename, saveFilename):
  f = open(filename, 'rb')
  index = 0
  buf = f.read()
  f.close()
  magic, labels = struct.unpack_from('>II' , buf , index)
  index += struct.calcsize('>II')
  labelArr = [0] * labels
  #labelArr = [0] * 200
  for x in range(labels):
      for x in range(2000):
          labelArr[x] = int(struct.unpack_from('>B', buf, index)[0])
          index += struct.calcsize('>B')
          save = open(saveFilename, 'w')
          save.write(','.join(map(lambda x: str(x), labelArr)))
          save.write('\n')
  save.close()
  print('save labels success')

def loadLabelSet(filename):
    f=open(filename,'rb')
    buffer=f.read()
    head=struct.unpack_from('>II',buffer,0)
    lableNum =head[1]
    offset = struct.calcsize('>II')

    numString = '>'+str(lableNum)+'B'
    labels=struct.unpack_from(numString,buffer,offset)
    f.close()
    labels=np.reshape(labels,[lableNum])
    print(labels,head)


def dlmwrite(Filename, X, fmt='%16.8e',delimiter=' ', newline='\n',header=''):  
    """ 
    #~ Save Data To Txt-File. 
    #~ >>> dlmwrite(Filename, X, fmt='%16.8e',delimiter=' ', newline='\n',header=''): 
    """  
    import numpy  
    numpy.savetxt(Filename, X, fmt=fmt, delimiter=delimiter, newline=newline,header=header)  
    return 

if __name__ == '__main__':
  #read_image('D:/Python_Resource/MNIST_data/t10k-images.idx3-ubyte')
  read_label('D:/Python_Resource/MNIST_data/t10k-labels.idx1-ubyte', 'D:/Python_Resource/MNIST_data/test/label.txt')
  loadLabelSet('D:/Python_Resource/MNIST_data/t10k-labels.idx1-ubyte')
# X=numpy.random.randn(3,4)
# dlmwrite('D:/Python_Resource/MNIST_data/test/label.txt',X,header='look at this file')