# import re
# str="kartikey1234 sharma111"
# # l=re.findall("\d",str)
# l=re.findall(r"\kartikey\d{4}$",str)
# print(l)
# create a pattern allowed character are a-z,A-Z,0-9 first character is from a-z and the remaining are no divisible by 3 and has atleast 2 length
# pattern = re.compile(r"^[a-z][0369][a-zA-Z0-9]*")
# str = [
#     "7376563478",
#     "b6",
#     "c9",
#     "d0",
#     "e4",
#     "a3"
# ]
# for string in str:
#     match = pattern.match(string)
#     if match:
#         print(f"{string}:matched")
#     else:
#         print(f"{string}not matched") 

# start with letter folowed by any digit and by any signal except $ and @ in thst atleast contain 2 digits    

# pattern = re.compile(r"^[a-zA-Z][0-9]{2,}[^$#@]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$") 
# strings = [
#     "a123b@example.com", 
#     "b456c@example.net",  
#     "c789d@example.org",  
#     "A1x@example.com",    
#     "12x@example.com",    
#     "ax@example.com",     
#     "a1$b@example.com",   
#     "a1#x@example.com",   
#     "a1@x@example.com",   
#     "a1x@example",        
#     "a1x@example.",
#     "Abc21@gmail.com"
# ]  
# for string in strings:
#     if pattern.match(string):
#         print(f"'{string}' matches the pattern.")
#     else:
#         print(f"'{string}' does not match the pattern.") 
# import urllib
# import urllib.request
# u =urllib.request.urlopen("https://www.redbus.in/info/contactus")
# text =u.read()
# # print(text)
# pattern = r'\b\d{10}\b' 
# contact_numbers = re.findall(pattern, text)
# if contact_numbers:
#         print("Contact Numbers Found:")
#         for number in contact_numbers:
#             print(number)
# else:
#         print("No contact numbers found.")
# import urllib
# import urllib.request

# url = "https://www.redbus.in/info/contactus"
# u = urllib.request.urlopen(url)
# try:
#     u = urllib.request.urlopen(url)
#     text = u.read().decode('utf-8')  

#     pattern = r'\b\d{10}\b'
#     contact_numbers = re.findall(pattern, text)

#     if contact_numbers:
#         print("Contact Numbers Found:")
#         for number in contact_numbers:
#             print(number)
#     else:
#         print("No contact numbers found.")
        
# except Exception as e:
#     print("Error occurred:", e)
# text=u.read().decode('utf-8')
# pattern = re.compiler(r'\+?\d{1,3}?\d{10}')
# phone_numbers = pattern.findall(data)
# for phone_number in phone_number:
#     print(phone_number)
# number = re.findall("[0-9]{12}",text=str(text))
# for n in n (function):
#     print(def findall(
        




import re

with open("text.txt", "r") as file:
    data = file.read()

pattern = r"https://fidelity//rest//v\d+\.\d+\.\d+"

valid_endpoints = re.findall(pattern, data)

with open("regex.txt", "w") as output_file:
    if valid_endpoints:
        output_file.write("\n".join(valid_endpoints))
        print("Valid endpoints written to regex.txt")
    else:
        print("No valid endpoints found.")
