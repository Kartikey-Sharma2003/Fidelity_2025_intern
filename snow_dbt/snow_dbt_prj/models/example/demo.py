import snowflake.connector
import pandas as pd

# Snowflake connection details
conn = snowflake.connector.connect(
    user='KARTIKEY',
    password='Kartikey@20031112',
    account='al80599.ap-southeast-1',  # Example: 'abcd-xy123.snowflakecomputing.com'
    warehouse='COMPUTE_WH',
    database='FIDELITY',
    schema='FIL_SCHEMA'
)

cur = conn.cursor()
cur.execute("SELECT * FROM FIL_SCHEMA.CUSTOMERS")

# Fetch data and create DataFrame
data = cur.fetchall()
df = pd.DataFrame(data, columns=[x[0] for x in cur.description])

print(df)

# Close connection
cur.close()
conn.close()
