import pandas as pd
d = pd.read_csv("Demographic_Statistics_By_Zip_Code.csv")
# d.to_csv('test.csv')
# d = pd.read_csv("Demographic_Statistics_By_Zip_Code.csv", index_col= 0)
for index, row in d.iterrows():
    print(",".join([str(row[column]) for column in d]))
# print(d.to_string())
# Save to csv
# d.to_csv('test1.csv')