#GRAPIC BUILD

node1 = tf.constant( 3.0 , tf.float32 )
node2 = tf.constant( 4.0 )
node3 = tf.add(nod1,node2)
# node 1,2 가 node3에서 만나는 형태

print("node1:",node1,"node2:",node2)
print("node3: node3")


# node1 : Tensor("Const_1:0",shape = (), dtype = float32)
# node2 : Tensor("Const_2:0",shape = (). dtype = float32)
# node3 : Tensor("Add:0",shape = (), dtype = float32)

#그저 생성 된 것 뿐



 #결과값을 나오게 하는 것은
 sess = tf.Session()
 print("sess.run(node1,node2):", sess.run([node1, node2]))
 print("sess.run(node3):",sess.run(node3))

 # sess.run( node1,node2) : [3.0,4.0]
 # sess.run(node3) : 7.0