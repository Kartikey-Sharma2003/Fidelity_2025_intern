import numpy as np
# l=[2,3,4,5]
# a=np.array(l)
# # print(type(a))
# b=10
# print(a+b)
# ar1=np.array([10,30,4.6])
# print(ar1)
# print(ar1.dtype)
# ar2=np.array([[10,20,30],[40,50,60]],dtype=np.int64)
# print(ar2)

# ones_array=np.ones((3,4))
# print(ones_array)
# y=np.random.rand(5,1,5)
# print(y)
# ar1=np.array([[10,20,30],[40,50,60]])
# print(ar1.shape)
# d=np.arange(10)
# print(d)
a=np.array([[10,20],[40,50]])
c=np.array([10,50])
print(np.linalg.solve(a,c))