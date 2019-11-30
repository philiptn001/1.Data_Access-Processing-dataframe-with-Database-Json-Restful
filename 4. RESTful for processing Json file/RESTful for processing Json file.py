import requests
import pandas as pd

obj = requests.get("https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.json").json()
data = obj['data']
column = obj['meta']['view']['columns']
column_name = []
for c in column:
    column_name.append(c['name'])

df = pd.DataFrame(data = data, columns= column_name)
print(df.to_string())

# print column names
# print(",".join([column for column in df]))

# print rows one by one
# for index, row in df.iterrows():
#     print(",".join([str(row[column]) for column in df]))