# importing pandas as pd
import pandas as pd

# making data frame from csv file
data=pd.read_csv("ks-projects-201801.csv")

# dictionary of lists
dict = {'main_category': ["Poetry", "Film & Video", "Music"],
        'country': ["GB", "US", "US"],
        'backers': [0, 15, 1]}

# creating a dataframe from a dictionary
df = pd.DataFrame(dict)

# iterating over rows using iterrows() function
for x, y in df.iterrows():
    print(x, y)
    print()


#My results created a dictionary of lists and also used the iterrows function