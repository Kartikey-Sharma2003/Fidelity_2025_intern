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
# a=np.array([[10,20],[40,50]])
# c=np.array([10,50])
# print(np.linalg.solve(a,c))
import pandas as pd
# s=pd.Series([10,2,3,'Data',5.5])
# print(s)
# data={
#     'names':['kartikey','sharma'],
#     'score':[100,200]
# }
# df=pd.DataFrame(data)
# print(df)
dates=pd.date_range('2020-10-11',periods=6,freq='ME')
# print(dates)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list("ABCD"))
# print
# print(df.columns)
data=pd.read_csv('police.csv')
# print(data.shape)
# print(data.head(3))
# print(data.tail(3))
# print(data.isnull().sum())
data.drop(['county_name'],axis=1,inplace=True)
# print(data)
# print(data.isnull().sum())
data.drop(['search_type'],axis=1,inplace=True)
# print(data.isnull().sum())
data['driver_gender'].fillna(data['driver_gender'].mode,inplace=True)
# print(data.isnull().sum())
data['driver_gender'].fillna(data['driver_gender'].mean,inplace=True)
print(data)

