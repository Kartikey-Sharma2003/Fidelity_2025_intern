#ques 1,2,5,7,4

# name-kartikey sharma , email-kartikeytrench47@gmail.com
#answer 1:
import json
employess = {
     "employee": [
        {"id": 1, "name": "kartikey", "role": "developer", "basic": 50000, "hra": 10000, "da": 5000},
        {"id": 1, "name": "kris", "role": "tester", "basic": 60000, "hra": 1000, "da": 6000},
        {"id": 1, "name": "aman", "role": "hr", "basic": 5000, "hra": 1000, "da": 500},
        {"id": 1, "name": "ankit", "role": "developer", "basic": 40000, "hra": 30000, "da": 6000},
        {"id": 1, "name": "drakster", "role": "manager", "basic": 45000, "hra": 9000, "da": 7000},
       
    ]
}
for employee in employess["employee"]:
    employee["total_salary"] = employee["basic"] + employee["hra"] + employee["da"]
with open("employees.txt", "w") as file:
    json.dump(employess, file, indent=4)

print("data has been written in employees.txt file")


# answer 2:
import re

def extract_valid_emails(text):
    pattern = r"\b[a-zA-Z][a-zA-Z0-9]*@[a-zA-Z]+\.(com|in|net|uk)\b"
    emails = [match.group() for match in re.finditer(pattern, text)]
    return emails

txt = " abc.df@somecompany.co.uk, abc@gmail.com, xyz.ab@tpa.com, dfg.gh@dp.cp.net . But what about 11.234.abc.ghy@tp.edu"

valid_emails = extract_valid_emails(txt)
print(valid_emails)


#answer 4:
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def printing(self, text):
        pass

class HP(Printer):
    def printing(self, text):
        return "hp printing"

class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")

    @abstractmethod
    def interest(self):
        pass

class HDFC(Bank):
    def interest(self):
        return "HDFC interest rate is 15%"

class IOB(Bank):
    def interest(self):
        return "IOB interest rate is 10%"

bank_a = HDFC()
bank_b = IOB()

bank_a.bank_info()
print(bank_a.interest())

bank_b.bank_info()
print(bank_b.interest())

#answer 7:
class Employee:
    def __init__(self, name, emp_id, ):
        self.name = name
        self.emp_id = emp_id
        

class Department(Employee):
    def __init__(self, name, emp_id, dept_name, dept_id):
        super().__init__(name, emp_id,)
        self.dept_name = dept_name
        self.dept_id = dept_id

    def dsp(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Department Name: {self.dept_name}")

if __name__ == "__main__":
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    
    dept_name = input("Enter department name: ")
    dept_id = input("Enter department ID: ")

    department = Department(name, emp_id, dept_name, dept_id)
    department.dsp()







