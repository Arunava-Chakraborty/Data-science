import pandas as pd
import numpy as np

#Pandas series is like a Table Column - 1D Array holding any type
#of data

list = [1,2,3,4]
P_Series = pd.Series(list)
print(P_Series)
#changing the index value the index value length and the list length should match.
# Also the series accept "index" as an argument nothisng else it value could be anything but the argument name should 
#not be change

Index = ["A", "B" ,"C" , "D"]
P_Series = pd.Series(list , index = Index)
print(P_Series)

print(P_Series["B"])
#printing the value from index

#key value dictionary
cprint(P_Series["B"])
#printing the value from index

print(car_series["Tesla"])
