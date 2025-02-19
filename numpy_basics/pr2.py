# import openpyxl

# path = r"C:\Users\KARTIKEY\OneDrive\Desktop\fidelity\numpy_basics\tips.xlsx"

# wb_obj = openpyxl.load_workbook(path)

# sh_obj = wb_obj.active

# rows = sh_obj.max_row
# cols = sh_obj.max_column

# for i in range(1, rows + 1):  
#     print(sh_obj.cell(row=i, column=1).value) 
# import openpyxl

# path = r"C:\Users\KARTIKEY\OneDrive\Desktop\fidelity\numpy_basics\tips.xlsx"

# wb_obj = openpyxl.load_workbook(path)

# sh_obj = wb_obj.active

# headers = [sh_obj.cell(row=1, column=j).value for j in range(1, sh_obj.max_column + 1)]

# data_dict = {header: [] for header in headers}

# for i in range(2, min(12, sh_obj.max_row + 1)):  
#     for j, header in enumerate(headers, start=1):
#         data_dict[header].append(sh_obj.cell(row=i, column=j).value)

# print(data_dict)
# from openpyxl import Workbook  

# wb = Workbook()  
# sh = wb.active  

# sh["A1"] = 10
# sh["A2"] = 20
# sh["A3"] = 30
# sh["A4"]='=sum(A1:A3)'

# wb.save(r"C:\Users\KARTIKEY\OneDrive\Desktop\fidelity\numpy_basics\tips.xlsx")  
# from openpyxl import Workbook
# from openpyxl.chart import BarChart, Reference
# data = [["Year", "Sales"],
#         [2020, 100],
#         [2021, 120],
#         [2022, 150],
#         [2023, 180],
#         [2024, 200]]

# wb = Workbook()
# sh = wb.active
# for s in data:
#     sh.append(s)
# bar = BarChart()
# data = Reference(sh, min_col=1, min_row=2, max_row=5, max_col=2)
# categories = Reference(sh, min_col=1, min_row=2, max_row=5)
# sh.add_chart(bar, "E2")
# bar.set_categories(categories)
# bar.add_data(data, "E3")

# wb.save(r"C:\Users\KARTIKEY\OneDrive\Desktop\fidelity\numpy_basics\tips.xlsx")    

# wb = Workbook()  
# data=[10,23,34]
# sh = wb.active  

# sh["A1"] = 10
# sh["A2"] = 20
# sh["A3"] = 30
# for i in data:
#     sh.append([i])

# wb.save(r"C:\Users\KARTIKEY\OneDrive\Desktop\fidelity\numpy_basics\tips.xlsx") 
from collections import namedtuple
Student=namedtuple("Student",['name','age'])
s=(Student('Kartikey',45))
print(s)

