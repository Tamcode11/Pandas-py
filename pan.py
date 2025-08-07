








import pandas as pd


data = {
    "Name": ['Ram','Sham', 'Raju', 'mino', 'tina', 'sono'],
    "Age": [25, 26, 27, 28, 29, 30],
    "salary": [20000, 10000, 30000, 40000, 50000, 60000],
    "performance score": [90, 85, 78, 95, 99, 50]
}
# print all data : 
df = pd.DataFrame(data)
print(df)

# TO add column : 
df['Bonus'] = df['salary'] * 0.1 # increment salary 10 % 
print(df) # new Bonus column added 

# to add new column with new values : 
df['work'] = [
    'SW engineer',
    'ML engineer',
    'Data Scientist',
    'Data Analytics',
    'Data engineer',
    'AI tool expert'
]
print(df)

# To insert column at specific position : 
df.insert(0 ,'employ_id',(101,102,103,104,105,106))
print(df)

# TO access row ,column and modify : 
df.loc[1 ,'salary'] = 80000 # at 1st index change salary(10000 to 80000)
print(df)

# Increasing salary by 5% :
df['salary'] = df['salary'] * 1.05  
print(df)

# To remove columns : 
df.drop(columns=["performance score"] , inplace = True)
print(df)

# TO know missing data : 
print(df.isnull()) # False -> value present ,True -> value missing 
print(df.isnull().sum()) # count sum of missing values 

# To handle missing data : 
df.dropna(inplace = True)
print(df)  # it clean missing values  

# by default value if missing : 
df.fillna(0 ,inplace = True)
print(df)

# mean
df['Age'].fillna(df['Age'].mean() ,inplace = True)
print(df)
