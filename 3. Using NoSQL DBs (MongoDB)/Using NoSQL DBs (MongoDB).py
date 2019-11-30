import json
import pandas as pd
from pymongo import MongoClient

d = pd.read_csv("Demographic_Statistics_By_Zip_Code.csv")
Client = MongoClient(host = "localhost", port = 27017)
database = "mydb"
db = Client['demographic']
c = db['Demographic_Statistics']
records = json.loads(d.T.to_json()).values()
c.insert(records)

c = db['Demographic_Statistics']
df = pd.DataFrame(list(c.find()))
print(df.to_string())
# print_dataframe(df)