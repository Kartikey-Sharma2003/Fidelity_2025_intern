# def function():#default function
#     print("hello")
# function()
# def dsp(name,age):# parametrized function
#     print(name,age)
# dsp(name='kartikey',age = 21)    
# l =[10,20,40,80]
# def f(l):
#     return sum(l),min(l),max(l)
# s1,max,min = f(l)
# print(s1,max,min)
# def f(*a):#kargs function
#     print(sum(a),max(a))
# f(10,20,30)    
# def f(**a):# return dictionary keyword arguments
#     print(a)
# f(name='kartikey',age =40, salary ='21k'

# def s1(a,b):# anonymous function calling function with different name p is a variable but it treated as an object
#     return a+b
# p = s1
# print(p(10,20))
# def f1(): # nested function
#     def f2():
#         return"hello"
#     return f2()
# print(f1())
# def f1(a): # outer a function that can access variables from its outer function, even after the outer function has finished executing.
#     def f2():# inner function
#         print(a)
#     return f2()
# f1(10)    
# data = 10 # we have to global keyword  to use global variable in a function scope
# def f1():
#     global data
#     data = data+10
#     return data
# print(f1())
# l1 = [10,3,4,5,90]
# l2 = iter(l1)# iterable an object that returns an element one at a time 10
# print(next(l2)) 
# print(next(l2)) #3 no need to write a for loop you just write number of times you need that iteration
# def f1(): # generator function if you want to use memory efficiently and can be used as an iterable object
#     yield'a'
#     yield'e'
#     yield'o'
# p = f1()
# print(next(p))    
# import sys
# # l1 = [10,23,4,5,90]
# # print(sys.getsizeof(l1))
# l1 = [i for i in range(100000)]
# g = (i for i in range(1000000))
# print(sys.getsizeof(l1))
# print(sys.getsizeof(g))
# def outer(x):
#     def inner(y):
#         return x+y
#     return inner
# print(outer(20,30)())
# input1 = eval(input("enter the first number:"))
# input2 = eval(input("enter the second number:"))
# def add(x,y):
#     return x+y
# def test(a):
#     global input1
#     global input2
#     return a(input1,input2)

# print(test(add))
# def f1(fun):
#     def wrapper():
#         print("hello")
#         fun()
#         print("end")
#     return wrapper
# @f1 # decorator function
# def f2():
#     print("fidelity team")

# f2()   
# def decorator(fun):
#     def wrapper(x,y):
#         print("Adding")
#         print(fun(x,y))
#         print("end")
#     return wrapper
# @decorator
# def add(x,y):
#     return x+y
# add(10,20)  
import fidelity_ds as fd
from fidelity_ds import month  
print(month('march')) 
  
