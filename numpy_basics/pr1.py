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
# dates=pd.date_range('2020-10-11',periods=6,freq='ME')
# print(dates)
# df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list("ABCD"))
# print
# print(df.columns)
# data=pd.read_csv('police.csv')
# print(data.shape)
# print(data.head(3))
# print(data.tail(3))
# print(data.isnull().sum())
# data.drop(['county_name'],axis=1,inplace=True)
# print(data)
# print(data.isnull().sum())
# data.drop(['search_type'],axis=1,inplace=True)
# print(data.isnull().sum())
# data['driver_gender'].fillna(data['driver_gender'].mode,inplace=True)
# print(data.isnull().sum())
# data['driver_gender'].fillna(data['driver_gender'].mean,inplace=True)
# data=pd.read_csv('police.csv')
# print(data)
# print(data.loc[:5,['driver_gender','stop_outcome']])
# data.set_index('stop_date')
# print(data)
# print(data.duplicated())
import pandas as pd
import sqlite3

# data = pd.read_csv('police.csv')

# def get_age(driver_age_raw):
#     if pd.isna(driver_age_raw):
#         return None
#     try:
#         return 2022 - int(driver_age_raw)
#     except ValueError:
#         return None  

# data['driver_age'] = data['driver_age_raw'].apply(get_age)
# print(data)
data=pd.read_csv('tips.csv')
# print(data)


df=pd.read_csv('tips.csv')
# df=pd.DataFrame(data)
# print(df)
df=pd.read_csv('tips.csv')
# df['tip'] = pd.to_numeric(df['tip'], errors='coerce')
# tip_summary = df.groupby('sex')['tip'].mean().reset_index()
# max_tipping_gender = tip_summary.loc[tip_summary['tip'].idxmax(), 'sex']
# max_tip_value = tip_summary['tip'].max()
# print(tip_summary)
# tip_count=df.groupby('sex')['tip'].count().reset_index()
# print(tip_count
# df=pd.read_csv('tips.csv')
# df['smoker'] = df['smoker'].apply(lambda x: 1 if x.lower() == 'yes' else 0)
# print(df[['smoker']])
# import pandas as pd
# from sqlalchemy import create_engine

# # 1. Load Dataset
# data = pd.read_csv('tips.csv')

# # 2. Database Configuration
# db = {
#     'name': 'fidelity',
#     'user': 'root',
#     'password': 'kartikey@1',
#     'host': 'localhost',
#     'port': 3306
# }

# # 3. Create Engine
# engine = create_engine("mysql+pymysql://{user}:{password}@{host}:{port}/{name}".format(**db))

# # 4. Store Data in SQL Table
# data.to_sql(name="tips", con=engine, if_exists="replace", index=False)

# print("Data successfully stored in MySQL!")
# df=pd.read_csv('tips.csv')
# df['smoker'] = df['smoker'].apply(lambda x: 1 if x.lower() == 'yes' else 0)
# print(df[['smoker']])
# df.to_csv('tips.csv',index=False)
# import pandas as pd
# from sqlalchemy import create_engine
# import urllib.parse  # Import for encoding special characters in passwords

# # 1. Load Dataset
# data = pd.read_csv('tips.csv')

# # 2. Database Configuration
# db = {
#     'name': 'fidelity',
#     'user': 'root',
#     'password': urllib.parse.quote_plus('Kartikey@1'),  # Encode special characters
#     'host': 'localhost',
#     'port': 3306
# }

# # 3. Create Engine
# engine = create_engine("mysql+pymysql://{user}:{password}@{host}:{port}/{name}".format(**db))

# # 4. Store Data in SQL Table
# data.to_sql(name="tips", con=engine, if_exists="replace", index=False)

# print("Data successfully stored in MySQL!")
# import mysql.connector as mysql

# # Database Configuration
# con = {
#     'host': 'localhost',
#     'database': 'fidelity',
#     'user': 'root',
#     'password': 'Kartikey@1',
#     'port': 3306
# }

# try:
#     mydb = mysql.connect(**con)
#     print("Database connection successful!")

#     cursor = mydb.cursor()

#     query = "SELECT * FROM tips"
#     cursor.execute(query)

#     rows = cursor.fetchall()
#     print("Tips Table Data:")
#     for row in rows:
#         print(row)

#     cursor.close()
#     mydb.close()

# except mysql.Error as err:
#     print("Error:", err)

import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

# Database Configuration
db_config = {
    'host': 'localhost',
    'database': 'fidelity',
    'user': 'root',
    'password': urllib.parse.quote_plus('Kartikey@1'),
    'port': 3306
}

# ✅ Correct Connection String
engine = create_engine(
    f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
)

try:
    # ✅ Read data from 'tips' table into a DataFrame
    df = pd.read_sql("SELECT * FROM tips", con=engine)
    print(df)
    df.to_sql('tips_backup',con=engine,if_exists='replace',index=False)
    print("data Stored")
except Exception as e:
    print("error",e)    
    

   








