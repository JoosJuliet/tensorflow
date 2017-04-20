#hyphothesis function

 # x and y data
 x_train = [1,2,3]
 y_train = [1,2,3]

 W = tf.Variable(tf.random_normal([1]), name = 'weight')
 b = tf.Variable(tf.random_normal([1]), name = 'bias')

 # W,b는 variable or trainable variable이다
 # tensorflow shape도 신경쓴다.
#tf.random_normal([1]) 값이 하나인 1차원 array


 #Our hypothesis XW+b
 hypothesis = x_train * W + b
