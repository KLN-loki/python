# c) Write a program that demonstrates the row selection, row addition, and row
# deletion.

import pandas as pd
  
# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
print(df)

print(df.loc[0], "\n", df.loc[1])

new_row = pd.DataFrame({'Name':'Geeks', 'Age':33, 'Address': 'kakinada', 'Qualification': 'btech'},index =[0])
# simply concatenate both dataframes
df = pd.concat([df, new_row]).reset_index(drop = True)

print(df)

df.drop([0, 1], inplace = True)
  
# display
print(df)