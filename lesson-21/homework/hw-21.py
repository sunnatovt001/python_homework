# Homework
lesson-21


#DataFrame 1: Student Grades
#import pandas as pd

#data1 = {
#    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
#    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
#    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
#}

#df1 = pd.DataFrame(data1)
#Exercise 1: Calculate the average grade for each student.

#Exercise 2: Find the student with the highest average grade.

#Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.

#Exercise 4: Plot a bar chart to visualize the average grades in each subject.


import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

df1["Average"] = df1[["Math", "English", "Science"]].mean(axis=1)

df1




max_avg = df1["Average"].max()

top_student = df1[df1["Average"] == max_avg]

top_student




df1["Total"] = df1[["Math", "English", "Science"]].sum(axis=1)

df1




import matplotlib.pyplot as plt

subject_averages = df1[["Math", "English", "Science"]].mean()

plt.bar(subject_averages.index, subject_averages.values)

plt.title("Average Grades by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Grade")

plt.show()





#DataFrame 2: Sales Data
#import pandas as pd

#data2 = {
#    'Date': pd.date_range(start='2023-01-01', periods=10),
#    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
#    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
#    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
#}

#df2 = pd.DataFrame(data2)
#Exercise 1: Calculate the total sales for each product.

#Exercise 2: Find the date with the highest total sales.

#Exercise 3: Calculate the percentage change in sales for each product from the previous day.

#Exercise 4: Plot a line chart to visualize the sales trends for each product over time.


import pandas as pd
import matplotlib.pyplot as plt

# Given data
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

# ---------------------------
# Exercise 1: Total sales for each product
# ---------------------------
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print("Exercise 1: Total sales for each product:")
print(total_sales)
print()

# ---------------------------
# Exercise 2: Date with the highest total sales
# ---------------------------
df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
max_sales_date = df2.loc[df2['Total_Sales'].idxmax(), 'Date']
print("Exercise 2: Date with the highest total sales:")
print(max_sales_date)
print()

# ---------------------------
# Exercise 3: Percentage change in sales for each product
# ---------------------------
percent_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
print("Exercise 3: Percentage change in sales for each product (in %):")
print(percent_change.round(2))
print()

# ---------------------------
# Exercise 4: Line chart to visualize the sales trends
# ---------------------------
plt.figure(figsize=(10, 6))
plt.plot(df2['Date'], df2['Product_A'], marker='o', label='Product A')
plt.plot(df2['Date'], df2['Product_B'], marker='o', label='Product B')
plt.plot(df2['Date'], df2['Product_C'], marker='o', label='Product C')

plt.title('Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()





#DataFrame 3: Employee Information
#import pandas as pd

#data3 = {
#    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
#    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
#    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
#    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
#    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
#}

#df3 = pd.DataFrame(data3)
#Exercise 1: Calculate the average salary for each department.

#Exercise 2: Find the employee with the most experience.

#Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe.

#Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments.


import pandas as pd
import matplotlib.pyplot as plt

# Given data
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# ---------------------------
# Exercise 1: Average salary for each department
# ---------------------------
avg_salary = df3.groupby('Department')['Salary'].mean()
print("Exercise 1: Average salary for each department:")
print(avg_salary)
print()

# ---------------------------
# Exercise 2: Employee with the most experience
# ---------------------------
most_experienced = df3.loc[df3['Experience (Years)'].idxmax()]
print("Exercise 2: Employee with the most experience:")
print(most_experienced)
print()

# ---------------------------
# Exercise 3: Salary increase percentage from the minimum salary
# ---------------------------
min_salary = df3['Salary'].min()
df3['Salary Increase (%)'] = ((df3['Salary'] - min_salary) / min_salary) * 100
print("Exercise 3: DataFrame with 'Salary Increase (%)' column:")
print(df3)
print()

# ---------------------------
# Exercise 4: Bar chart - Employee count per department
# ---------------------------
dept_counts = df3['Department'].value_counts()

plt.figure(figsize=(8, 5))
dept_counts.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Employee Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()





import pandas as pd
import matplotlib.pyplot as plt

# Given data
data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

# ---------------------------
# Exercise 1: Total revenue from all orders
# ---------------------------
total_revenue = df4['Total_Price'].sum()
print("Exercise 1: Total revenue from all orders:")
print(total_revenue)
print()

# ---------------------------
# Exercise 2: Most ordered product
# ---------------------------
most_ordered_product = df4['Product'].value_counts().idxmax()
print("Exercise 2: Most ordered product:")
print(most_ordered_product)
print()

# ---------------------------
# Exercise 3: Average quantity of products ordered
# ---------------------------
average_quantity = df4['Quantity'].mean()
print("Exercise 3: Average quantity of products ordered:")
print(round(average_quantity, 2))
print()

# ---------------------------
# Exercise 4: Pie chart - Sales distribution by product
# ---------------------------
sales_by_product = df4.groupby('Product')['Total_Price'].sum()

plt.figure(figsize=(7, 7))
plt.pie(
    sales_by_product,
    labels=sales_by_product.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=['#66b3ff', '#99ff99', '#ffcc99']
)
plt.title('Sales Distribution by Product')
plt.tight_layout()
plt.show()





