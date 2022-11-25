"""7) Pandas Library: Selection
a) Write a program that converts Pandas DataFrame and Series into numpy.array.
b) Write a program that demonstrates the column selection, column addition, and
column deletion.
c) Write a program that demonstrates the row selection, row addition, and row
deletion.
d) Get n-largest and n-smallest values from a particular column in Pandas dataFrame
"""


import pandas as pd
import numpy as np

#initialize a dataframe
df = pd.DataFrame(
	[[21, 72, 67],
	[23, 78, 69],
	[32, 74, 56],
	[52, 54, 76]],
	columns=['a', 'b', 'c'])

print('DataFrame\n----------\n', df)

#convert dataframe to numpy array
arr = df.to_numpy()

print('\nNumpy Array\n----------\n', arr)
print('DataFrame\n----------\n', df)
print('\nDataFrame datatypes :\n', df.dtypes)

#convert pandas dataframe to numpy array
arr = df.to_numpy()

print('\nNumpy Array\n----------\n', arr)
print('\nNumpy Array Datatype :', arr.dtype)

#define series
x = pd.Series([1, 2, 5, 6, 9, 12, 15])

#convert series to NumPy array
new_array = x.to_numpy() 
print(new_array)
#view NumPy array
# new_array = array([ 1,  2,  5,  6,  9, 12, 15])

#confirm data type
print(type(new_array))

# numpy.ndarray