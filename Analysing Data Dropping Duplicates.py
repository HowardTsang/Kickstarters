import pandas as pd

data=pd.read_csv("ks-projects-201801.csv")

new_data = data.drop_duplicates(subset=['main_category'])

print(data.shape,new_data.shape)
