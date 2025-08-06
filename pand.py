
import pandas as pd


data = {
    "Name": ['Ram', 'sham', 'Raju', 'mino', 'tina', 'sono'],
    "Age": [25, 26, 27, 28, 29, 30],
    "salary": [20000, 10000, 30000, 40000, 50000, 60000],
    "performance score": [90, 85, 78, 95, 99, 50]
}
# print all data : 
df = pd.DataFrame(data)
print(df)

# print starting rows : 
print(df.head(3))
# print last rows : 
print(df.tail(3))

# TO know number of rows ,column and what type of data store : 
print(df.info())

# TO know quick statistical summary of data set : 
print(df.describe())

# To know shape or column : 
print(df.shape)
print(df.columns)

# To filter column (series) :
name =df['Name']
print(name)

# To print multiple column : 
filtered = df[['Age' ,'Name','salary']]
print(filtered)

# To apply conditions : 
high_salary = df[(df['salary'] > 30000) & (df['Age'] > 27)]
print(high_salary)


