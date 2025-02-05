# try:
#     x=int(input("enter the number:"))
#     y=int(input("enter the number:"))
#     print(x/y)
# except ZeroDivisionError:
#     print('Error')
# except ValueError:
#     print("Value Error")    
#except Exception as msg:
    #print(msg.with_traceback) 
# class TooyoungException(Exception):
#     def __init__(self, msg):
#         self.msg = msg

        
     

# age =10
# if age<18:
#     raise TooyoungException("please wait") 
# """name,role,id is less than 4 raise an error to enter valid number of 4 digits"""
class InvalidEmployeeIDError(Exception):
    """Custom exception for invalid employee IDs."""
    pass

class Employee:
    def __init__(self, name, role, emp_id):
        self.name = name
        self.role = role
        self.id = str(emp_id)  

    def valid_id(self):
        if not self.id.isdigit():
            raise InvalidEmployeeIDError("ID should only contain digits.")
        elif len(self.id) != 4:
            raise InvalidEmployeeIDError("ID should be exactly 4 digits.")
        else:
            print(f"Welcome {self.name}, your role is {self.role}.")

try:
    name = input("Enter the employee's name: ")
    role = input("Enter the employee's role: ")
    emp_id = input("Enter a 4-digit employee ID: ")

    e = Employee(name, role, emp_id)
    e.valid_id()

except InvalidEmployeeIDError as error:
    print(f"Error: {error}")

                