import numpy as np 

a = np.array([1,2,3,4])
b = np.array([[1,2,3],[4,5,6]])
#print(b[:,1])

v1 = np.array([1,2,3])
v2 = np.array([4,5,6])
dot = np.dot(v1,v2)
#print(dot) #dot product
#print(v1*v2) #elemment vise multiplication 


#basic neural network
W = np.array([[0,1],[1,0],[0,1]]) #weight
x = np.array([2,3])
dotp = np.dot(W,x)
#print(dotp)
#print(dotp.shape)

#slicing

A = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

#print(A[:,0])

B = np.array([1, 2, 3])
#print(A + B)


AB = np.array([[1,2],[2,3],[3,4]])
mean = AB.mean(axis = 0)
#print(mean)
AB_normalized = AB - mean
#print(AB_normalized)