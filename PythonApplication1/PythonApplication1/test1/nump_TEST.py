import tensorflow as tf  

w=tf.constant([[1,2,3],[4,5,6]])
print(w)

se = tf.Session()  
a = tf.constant(10)  
b = tf.constant(22)  
print(se.run(a + b))  


#Creates a graph.
a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)
#Creates a session with log_device_placement set to True.
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
#Runs the op.
print(sess.run(c))