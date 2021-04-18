import pandas as pd

data=pd.read_csv("ks-projects-201801.csv")

data.sort_values(by="deadline", ascending=False)

deadline = data.sort_values('deadline')

print(data.sort_values(by="deadline", ascending=False))

print(deadline.head())