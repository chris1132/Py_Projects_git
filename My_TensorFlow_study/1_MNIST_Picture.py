import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
print("start")
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#定义session，注册为默认的session，之后的运算默认到这个session
sess = tf.InteractiveSession()
#创建placeholder ，输入数据的地方  第一个参数数据类型，第二个参数代表了数据尺寸，
# none 不限制输入，784 输入784维的向量
x = tf.placeholder(tf.float32, [None, 784])

#variable 持久化存储数据， 把权重w和bias 初始化为0
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

#softmax 函数  tf.matmul 计算矩阵乘积和
#多项分类里用softmax，所有输出值得概率不为0或负数，且和为1，满足概率分布
y = tf.nn.softmax(tf.matmul(x, W) + b)

#识别图片数字0-9  分为10类
y_ = tf.placeholder(tf.float32, [None, 10])
# #定义损失函数来描述问题分类的精度  值越小，越精确
# cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
#
# #随机梯度下降算法 SGD(Stochastic Gradient Descent)  优化算法
# train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
#
# #全局参数初始化 运行
# tf.global_variables_initializer().run()
#
# for i in range(1000):
#     batch_xs, batch_ys = mnist.train.next_batch(100)
#     train_step.run({x: batch_xs, y_: batch_ys})
#
# '''
# 训练完成
# '''
# #模型准确率验证  arfmax 求预测的数字中概率最大的一个  equal 判断类别是否正确
# #return boolean
# correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
#
# #转换成 32 位 再求平均
# accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# #将测试数据特征和label输入评测流程accuracy计算测试准确率
# print(accuracy.eval({x: mnist.test.images, y_: mnist.test.labels}))


'''
卷积
'''
def weight_variable(shape):
    initial = tf.truncated_normal(shape,stddev = 0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1,shape=shape)
    return tf.Variable(initial)

def conv2d(x,w):
    return tf.nn.conv2d(x,w,strides=[1,1,1,1],padding="SAME")
def max_pool_2x2(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
'''first con'''
def first_con():
    w_conv1 = weight_variable([5, 5, 1, 32])
    b_conv1 = bias_variable([32])
    x_image = tf.reshape(x, [-1, 28, 28, 1])
    h_conv1 = tf.nn.relu(conv2d(x_image, w_conv1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)
    return h_pool1
'''second_con'''
def second_con(con1_out):
    w_conv2 = weight_variable([5, 5, 32, 64])
    b_conv2 = bias_variable([64])
    h_conv2 = tf.nn.relu(conv2d(con1_out, w_conv2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)
    return h_pool2
'''miji'''
keep_prob = tf.placeholder(tf.float32)
def con(con2_out):
    W_fc1 = weight_variable([7 * 7 * 64, 1024])
    b_fc1 = bias_variable([1024])
    h_pool2_flat = tf.reshape(con2_out, [-1, 7 * 7 * 64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
    return h_fc1_drop

'''output'''
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y_conv=tf.nn.softmax(tf.matmul(con(second_con(first_con())), W_fc2) + b_fc2)

cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
tf.global_variables_initializer().run()

show_arr = []
im = Image.open('image/number_2.png')
im = im.resize((28, 28))
im = np.array(im).astype(np.float32)
im = np.reshape(im, [-1, 28 * 28])
img_gray = (im - (255 / 2.0)) / 255
x_img = np.reshape(img_gray, [-1, 784])

for i in range(20000):
  batch = mnist.train.next_batch(50)
  if i%100 == 0:
      print("training.....",i)

      # img_x = tf.cast(tf.reshape(img_arr,[-1,784]),tf.float32).eval()
      # output = sess.run(y_conv, feed_dict={x: img_x})
      # print(np.argmax(output))

      # img_x = tf.reshape(tf.cast(img_arr,tf.float32),[-1,784]).eval()
      # img_y = tf.constant([[ 0,0,1, 0,0, 0,0,0, 0,0]]).eval()
      # output = sess.run(y_conv, feed_dict={x: img_x})
      # print(np.argmax(output))
      # res = accuracy.eval({x:img_x, y_: img_y, keep_prob: 1.0})

      test_batch = mnist.test.next_batch(50)
      res = accuracy.eval({x:test_batch[0],y_:test_batch[1],keep_prob: 1.0})
      show_arr.append(res)
      print('%.2f%%' % (res * 100))
      output = sess.run(y_conv, feed_dict={x: x_img,keep_prob:1.0})
      print('the predict is : ', np.argmax(output))
  train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

# print("test accuracy %g"%accuracy.eval(feed_dict={
#     x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))

saver = tf.train.Saver()
saver.save(sess, "model_data/model.ckpt")

x = np.linspace(0,20000,200)
print(np.mean(show_arr))
plt.plot(x,show_arr)
plt.show()



