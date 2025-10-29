# Homework
17-lesson

#Homework 1:

#import pandas as pd

#data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} df = pd.DataFrame(data)

#Rename column names using function. "First Name" --> "first_name", "Age" --> "age
#Print the first 3 rows of the DataFrame
#Find the mean age of the individuals
#Select and print only the 'Name' and 'City' columns
#Add a new column 'Salary' with random salary values
#Display summary statistics of the DataFrame


import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)

df = df.rename(columns={"First Name":"first_name","Age":"age"})
print(df)

###############################################
print(df.head(3))

###############################################
avg = df["age"]
print(avg.mean())

###############################################
print(df[['first_name', 'City']])


###############################################
import numpy as np
df['Salary'] = np.random.randint(50000, 100000, size=len(df))
print(df)

##############################################
print("\nSummary Statistics:")
print(df.describe())





#Homework 2:

#Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.
#Month	Sales	Expenses
#Jan	5000	3000
#Feb	6000	3500
#Mar	7500	4000
#Apr	8000	4500
#Calculate and display the maximum sales and expenses.
#Calculate and display the minimum sales and expenses.
#Calculate and display the average sales and expenses.

import pandas as pd

data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'], 
        'Sales': [5000, 6000, 7500, 8000], 
        'Expenses': [3000,3500,4000,4500]} 
df = pd.DataFrame(data)


#####
print("Max Sales:", df['Sales'].max())
print("Max Expenses:", df['Expenses'].max())

#####
print("Min Sales:", df['Sales'].min())
print("Min Expenses:", df['Expenses'].min())

#####
print("Average Sales:", df['Sales'].mean())
print("Average Expenses:", df['Expenses'].mean())




#Homework 3:

#Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.
#Category	January	February	March	April
#Rent	1200	1300	1400	1500
#Utilities	200	220	240	250
#Groceries	300	320	330	350
#Entertainment	150	160	170	180
#Calculate and display the maximum expense for each category.
#Calculate and display the minimum expense for each category.
#Calculate and display the average expense for each category.

import pandas as pd

data = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'], 
        'January': [1200,200,300,150], 
        'February': [1300,220,320,160],
        'March':[1400,240,330,170],
        'April':[1500,250,350,180]} 
df = pd.DataFrame(data)


###
print("\nMaximum Expenses by Category:")
for index, row in df.iterrows():
    category = row['Category']
    max_expense = max(row['January'], row['February'], row['March'], row['April'])
    print(f"{category}: ${max_expense}")

###
print("\nMinimum Expenses by Category:")
for index, row in df.iterrows():
    category = row['Category']
    min_expense = min(row['January'], row['February'], row['March'], row['April'])
    print(f"{category}: ${min_expense}")

###
print("\nAverage Expenses by Category:")
for index, row in df.iterrows():
    category = row['Category']
    avg_expense = sum([row['January'], row['February'], row['March'], row['April']]) / 4
    print(f"{category}: ${avg_expense:.2f}")



