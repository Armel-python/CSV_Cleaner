import pandas as pd 
data=pd.read_csv("dirty_data.csv")
initial_rows=len(data)
data["Name"]=data["Name"].str.strip()
data=data.dropna()
data=data.drop_duplicates()
data.to_csv("clean_data.csv",index=False)
print(data)
print("cleaning complete")
final_rows=len(data)
removed_rows=initial_rows-final_rows
print("removed rows:",removed_rows)