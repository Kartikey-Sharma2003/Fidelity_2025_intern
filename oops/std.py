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
class Customer:
    """contains name and balance and number of methods are deposit and withdraw"""
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,money):
        self.money=money
        self.balance=self.balance+money
        return self.balance





    def withdraw(self,money):
        if(money>self.balance):
            return("insufficient balance")
        else:
            self.balance=self.balance-money
            return self.balance
c=Customer('kartikey',10000000)
print(c.deposit(24000))
print(c.withdraw(35000))              