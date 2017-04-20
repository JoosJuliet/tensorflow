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


a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b

#placeholder은 프로그램 실행 중에 데이터를 변경할 수 있게 해주는 것이며 이것은 심벌릭 변수를 선언할 때 쓰인다.

print(sess.run(adder_node , feed_dict = { a:3 , b:4.5 })) #7.5
# feed_dict란 placeholder에 있는 것 가져오기

print(sess.run(adder_node , feed_dict = {a: [1,3], b:[2,4]})) #[3,7]
