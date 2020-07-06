import tensorflow as tf
from PIL import Image
import numpy as np


image = "image/cat.jpg"

jpg = tf.read_file(image)
img_arr = tf.image.decode_jpeg(jpg,channels=3)
img_4d = tf.cast(tf.reshape(img_arr,[1,640,1136,3]),tf.float32)
pool = tf.nn.max_pool(img_4d, [1, 1, 1, 1], [1, 1, 1, 1], 'SAME')
with tf.Session() as sess:
 img, pool = sess.run([img_arr, pool])
 print(img.shape)
 print(pool.shape)
 Image.fromarray(np.uint8(pool.reshape(pool.shape[1:4]))).save('image/maxpool2.jpg')
# a = tf.constant([
#     [[1.0, 2.0, 3.0, 4.0],
#      [9.0, 6.0, 7.0, 8.0],
#      [8.0, 12.0, 6.0, 5.0],
#      [4.0, 3.0, 2.0, 1.0]],
#      [[4.0, 3.0, 2.0, 1.0],
#      [11.0, 7.0, 6.0, 5.0],
#      [1.0, 2.0, 3.0, 4.0],
#      [14.0, 6.0, 13.0, 8.0]]
# ])
# session = tf.InteractiveSession()
# a = tf.reshape(a, [1,2,4, 4])
#
# pooling = tf.nn.max_pool(a, [1, 1,2, 1], [1, 1, 1, 1], padding='VALID')
# # initial = tf.truncated_normal([2,2,1,3],stddev = 0.1)
# # initial2 = tf.truncated_normal([2,3,4,5],stddev = 0.1)
# print("image:",session.run(tf.shape(a)))
# image = session.run(a)
# print(image)
# print("reslut:",session.run(tf.shape(pooling)))
# result = session.run(pooling)
# print(result)
