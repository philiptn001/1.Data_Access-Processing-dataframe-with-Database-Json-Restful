import pandas as pd
import sqlite3
from pandas.io import sql

# d = pd.read_csv("Demographic_Statistics_By_Zip_Code.csv")
# d.to_csv('test.csv')
d = pd.read_csv("Demographic_Statistics_By_Zip_Code.csv", index_col= 0)
database = "database"
table = "mytable"
connection = sqlite3.connect(database)
sql.to_sql(d, table, connection)
d2 = sql.read_sql('select * from ' + table, connection)
print(d2.to_string())

# Dropping data from database
# sql.execute('DROP TABLE ' + table, connection)
# d.to_csv('test1.csv')