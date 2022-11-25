# d) Get n-largest and n-smallest values from a particular column in Pandas dataFrame

import pandas as pd
  
# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)

print(df.nlargest(2, ['Age']))
print(df.nsmallest(1, ['Age']))