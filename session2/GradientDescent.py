optimizer = tf.train.GradienDescentOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost) #cost를 줄이는 것
