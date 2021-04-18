import pandas as pd

data=pd.read_csv("ks-projects-201801.csv")

missing_values_count = data.isnull().sum()

print(missing_values_count[0:15])