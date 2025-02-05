# file=open("py_filehandling.txt","r")
# print(file.tell())
# data=file.read(50)
# file.seek(5)

# print(len(file.readlines()))
# lines=file.readlines()
# for l in file.read():
# for l in file:
#     print(l)
# count=0
# wcount=0
# lcount=0
# lines=file.readlines()
# print(lines)
# for l in file:
#     print(l)
#     count=count+len(l)
# print(count)    
# file.close()
# import os
# print(os.listdir("."))
# for dirpath,dir,path in os.walk("."):
#     print(dirpath,dir,file)
# import os
# root_dir = "D:\kartikey"
# for root,dirs,files in os.walk(root_dir):
#     print(f"Root directory:{root}")
#     print(f"subdirectory:{dirs}")
#     print(f"files:{files}")
#     print()
# print(os.listdir("."))
# for dirpath,dir,file in os.walk("."):
#     for i in file:
#         if i.endswith(".py"):
#             print(i)
# import csv
# with open("data.csv","w",newline="") as f:
#     w=csv.writer(f)
#     w.writerow(["Eno","Ename","Salary"])
#     w.writerow(["111","kartikey","1.5"])
# f=open("data.csv","r")
# r=csv.reader(f)
# data=list(r)
# print(data)    
# import pickle
# d=[10,30,56]
# file=open("list.dat","wb")
# # pickle.dump(d,file)
# l=pickle.load(file)
# file.close()
# print(l)
import pickle

data = {
    "list1": [10, 20, 30],
    "dict1": {"a": 10, "b": 20},
    "list2": [20, 30, 40],
    "dict2": {"x": 20, "y": 30},
}

with open("data.txt", "wb") as file:
    pickle.dump(data, file)

print("Data has been saved in data.txt")



with open("data.txt", "rb") as file:
    data = pickle.load(file)

dicts_only = {key: value for key, value in data.items() if isinstance(value, dict)}
print("Dictionaries from the file:")
print(dicts_only)



