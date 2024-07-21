import pandas as pd
import numpy as np
from numpy.random import randn

my_data = randn(4,3)# Rows ,Columns
my_rows = ["A" ,"B" , "C" ,"D"]
my_columns = ["Monday" ,1 , False]
my_data2 = pd.DataFrame(my_data , my_rows , my_columns)
print(my_data2)

# import csv file
df = pd.read_csv('icecream.csv')
df

#pull out rows froom csv
df.loc[0]

df.loc[[5,6,7,8,9,10,11,12,13,14,15]]

# Grab first 5 rows
df.head()

# Grab certain number of first rows
df.head(19)

# Grab the last 5 Rows
df.tail()

# Grab certain number of last rows
df.tail(10)

# Get info about the data frame
df.info()
#shape of the file
df.shape

#stats about the datas
df.describe()

#stats of a specific column
df['fat_g'].describe()

#stats of a specific column
df['flavour'].describe()

#stats of a specific column
df['protein_g'].describe()
#print specific columns
df.flavour
