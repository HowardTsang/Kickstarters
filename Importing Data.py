import pandas as pd

data1 =pd.read_csv("ks-projects-201801.csv")
data2 =pd.read_csv("ks-projects-201612.csv")

type("ks-projects-201801.csv")
type("ks-projects-201612.csv")

print(data1.info())
print(data1)
print(data1.head())

print(data2.info())
print(data2)
print(data2.head())