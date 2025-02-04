# class Student:
#     """this is student class"""
#     def __init__(self,name,age) -> None:
#         self.name=name
#         self.age=age
#     def dsp(self):
#         print(self.name,self.age)
# s=Student("kartikey",21)
# s.dsp()
# class Student:
#     a=10
#     def dsp(self):
#         pass
# s=Student()
# print(s.a) 
# class Student:
#     a=10
#     def dsp(self):
#         print(self.a)
#     @classmethod    
#     def m1(cls): 
#         print(cls.a)
# s=Student()
# Student.m1()  
# class Customer:
#     """contains name and balance and number of methods are deposit and withdraw"""
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposit(self,money):
#         self.money=money
#         self.balance=self.balance+money
#         return self.balance





#     def withdraw(self,money):
#         if(money>self.balance):
#             return("insufficient balance")
#         else:
#             self.balance=self.balance-money
#             return self.balance
# c=Customer('kartikey',10000000)
# print(c.deposit(24000))
# print(c.withdraw(35000))
# class Engine:
#     a=10
#     def __init__(self):
#         self.b=20
        
#     def m1(self):
#         print(self.a)
# class Car:
#     def __init__(self):
#         self.engine=Engine()
#     def m2(self):
#         print(self.engine.a)
#         print(self.engine.b)
#         self.engine.m1()
# c=Car()
# c.m2()  
# class Car:
#     """attributs- name,model,color and ,display method it will display name,model ,color"""
#     """employee - name,id,car is object and pass it"""
#     def __init__(self,name,model,color):
#         self.name=name
#         self.model=model
#         self.color=color
#     def display(self):
#         print(self.name)
#         print(self.model)
#         print(self.color)  
# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#         self.car=Car('mustang',1969,'black')
#         self.car.display()
#     def display(self):
#         print(self.name)
#         print(self.id)    
# c=Employee('kartikey','A785690') 
# print(c.display()) 
# class P:
#     a=10
#     def __init__(self):
#         self.b=20
#     def m1(self):
#         print("parent instance method")
#     @classmethod
#     def m2(cls):
#         print("class method")
#     @staticmethod
#     def m3():
#         print("static method")
# class C(P):
#     pass
# c=C()
# print(c.a)
# c.m1()
# P.m2()
# c.m3()
# class Person: 
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id
#     def getinfo(self):
#         return(self.name,self.age,self.id)
# class Employee(Person):
#     def __init__(self, name, age, id,sal):
#         self.salary=sal
#         super().__init__(name, age, id)
#     def dsp(self):
#         print(super().getinfo(),self.salary)
# p=Person('kartikey',21,'A785690')
# print(p.getinfo())
# e=Employee('kartikey',21,'A785690',70000000) 
# e.dsp() 
# class Employee:
#     def __init__(self,a=None,b=None):
#         self.a=a
#         self.b=b
#     def __str__(self):
#         return str(self.a)
# e1=Employee()
# e2=Employee(10)
# print(e2)
# class P1:
#     def m1():
#         print('m1')

# class C(P1):
#     def m1():
#         print('m2')

# class C(P1, P2):
#     pass

# print(C.mro()) 
# class P1:
#     def m1(self):
#         print('parent class')

# class P2(P1):
#     def m1(self):
#         super().m1() 
# class C(P1):
#     def m1(self):
#         super().m1()
# class D(P2,C):
#     def m1(self):
#         return super().m1()        

# d=D()
# d.m1()
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        # return ("name is{0} and age is{1}".format(self.name,self.age))
        msg = f"{self.name} age is {self.age}"
        
        return msg
s1=Student("kartikey",21)
print(s1)
       
                                                                       
                  

        
