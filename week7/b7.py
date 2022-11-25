# b) Write a program that demonstrates the column selection, column addition, and column deletion.

import pandas as pd
  
# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
  
# select two columns
print(df[['Name', 'Qualification']])

# Declare a list that is to be converted into a column
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
  
# Using 'Address' as the column name
# and equating it to the list
df['Address'] = address
  
# Observe the result
print(df)

# dropping passed columns
df.drop(["Address"], axis = 1, inplace = True)
  
# display
print(df)