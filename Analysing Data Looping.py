import pandas as pd
data=pd.read_csv("ks-projects-201801.csv")

#Creating Lists for Potential Categories
potential_category1 = {'main_category': 'Food', 'state': 'successful'}
potential_category2 = {'main_category': 'Music', 'state': 'successful'}
potential_category3 = {'main_category': 'Fashion', 'state': 'successful'}
potential_category = [potential_category1, potential_category2, potential_category3]

#Iterate the rows using looping
for i in potential_category:
    print(i)

#iterate the rows by the main_category variable
for i in potential_category:
    print(i['main_category'])

#loop and specify condition
potential_main_category = {}
main_category_lookup = 'Food'
for i in potential_category:
    if ',main_category' in i:
        if i['main_category'] == main_category_lookup:
            potential_main_category = i

print(potential_main_category)