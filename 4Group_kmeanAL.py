import tensorflow as tf

vectors = tf.constant(vectors_set)
k=4
centroides = tf.Variable(tf.slice(tf.random_shuffle(vectors),[0,0],[k,-1]))

expanded_vectors = tf.expand_dims(vectors, 0)
expanded_cetroides = tf.expand_dims(centroides, 1)

assignments = tf.argmin(tf.reduce_sum(tf.sub(expanded_vectors, expanded_cetroides),2),0)

means = tf.concat(0, [tf.reduce_mean(tf.gather(vectors, tf.reshape(tf.where(tf.equal(assignments,c)), [1,-1])),) reduction_indices = [1] for c in xrange(k)])

update_centroides = tf.assign(centroides, means)

init_op = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init_op)

for step in xrange(100):
    _, centroid_values, assignment_values = sess.run([update_centroides, centroides, assignments])


#확인을 위해 그림을 그린다.

data = {"x": [],"y":[],"cluster":[]}

for i in xrange(len(assignment_values)):
    data["x"].append(vectors_set[i][0])
    data["y"].append(vectors_set[i][1])
    data["cluster"].append(assignment_values[i])

df = pd.DataFrame(data)
sns.lmplot("x","y",data=df, fit_reg = False, size =6, hue = "cluster", legend=False)
plt.show()
