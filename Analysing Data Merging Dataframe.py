import pandas as pd
data1 = pd.read_csv("ks-projects-201612.csv")
data2 = pd.read_csv("ks-projects-201801.csv")

lst1 = list(data1)
lst2 = list(data2)

data1[lst1] = data1[lst1].astype(str)
data2[lst2] = data2[lst2].astype(str)

data1.head()
data2.head()

data1.columns = ['ID','name','category' ,'main_category' ,'currency','deadline','goal','launched','pledged','state','backer','country','usd pledged']
data2.columns = ['ID','name','category' ,'main_category' ,'currency','deadline','goal','launched','pledged','state','backer','country','usd pledged','usd_pledged_real','usd_goal_real']

result = pd.merge(pd.DataFrame(data1), pd.DataFrame(data2),how = 'inner' , on='ID')

print(result.head())

