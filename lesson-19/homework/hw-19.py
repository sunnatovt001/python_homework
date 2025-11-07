# Homework
lesson-19

#Homework Assignment 1: Analyzing Sales Data

#You are given a dataset containing sales data for an e-commerce website. The dataset (task\sales_data.csv) has the following columns:

#Date: Date of the sale.
#Product: Name of the product sold.
#Category: Category to which the product belongs.
#Quantity: Number of units sold.
#Price: Price per unit.



#Group the data by the Category column and calculate the following aggregate statistics for each category:
#Total quantity sold.
#Average price per unit.
#Maximum quantity sold in a single transaction.

import pandas as pd

df = pd.read_csv('sales_data.csv')
df.head()

result = df.groupby("Category").agg({
    "Quantity":["sum","max"],
    "Price":"mean"
})

result




# Identify the top-selling product in each category based on the total quantity sold.

sales_data = pd.read_csv('sales_data.csv')

total_quantity = sales_data.groupby(['Category','Product'])['Quantity'].sum().reset_index()
top_selling = total_quantity.loc[total_quantity.groupby('Category')["Quantity"].idxmax()]
top_selling




#Find the date on which the highest total sales (quantity * price) occurred.

sales_data['Total_Sales'] = sales_data['Quantity'] * sales_data['Price']
daily_sales = sales_data.groupby('Date')['Total_Sales'].sum()
max_sales_date = daily_sales.idxmax()
max_sales_value = daily_sales.max()

max_sales_value




#Homework Assignment 2: Examining Customer Orders

#You have a dataset (task\customer_orders.csv) containing information about customer orders. The dataset has the following columns:

#OrderID: Unique identifier for each order.
#CustomerID: Unique identifier for each customer.
#Product: Name of the product ordered.
#Quantity: Number of units ordered.
#Price: Price per unit.

import pandas as pd
df = pd.read_csv('customer_orders.csv')
df




#Group the data by CustomerID and filter out customers who have made less than 20 orders.

sales_data=pd.read_csv('customer_orders.csv')

customer_orders = sales_data.groupby('CustomerID').size().reset_index(name='order_count')

filtered_customers = customer_orders[customer_orders['order_count']>=20]
filtered_customers




#Identify customers who have ordered products with an average price per unit greater than $120.

avg_price_per_customer = sales_data.groupby('CustomerID')['Price'].mean().reset_index()
high_value_customers = avg_price_per_customer[avg_price_per_customer['Price']>120]
high_value_customers




#Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.

product_summary = sales_data.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_price=('Price', lambda x: (x * sales_data.loc[x.index, 'Quantity']).sum())
).reset_index()

filtered_products = product_summary[product_summary['total_quantity'] >= 5]
filtered_products




#Homework Assignment 3: Population Salary Analysis

#"task\population.db" sqlite database has population table.
#"task\population salary analysis.xlsx" file defines Salary Band categories.
#Read the data from population table and calculate following measures:
#Percentage of population for each salary category;
#Average salary in each salary category;
#Median salary in each salary category;
#Number of population in each salary category;
#Calculate the same measures in each State

import pandas as pd
import sqlite3

# 1. SQLite bazasiga ulanib, population jadvalini o‘qish
conn = sqlite3.connect('population.db')
population = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

# 2. Excel fayldan salary band ma'lumotlarini o‘qish
salary_bands = pd.read_excel('population_salary_analysis.xlsx')

# 3. Population jadvalidagi maoshni tegishli salary bandga joylashtirish
# Faraz qilamiz: salary_bands faylida "Min_Salary", "Max_Salary", "Category" ustunlari mavjud
def categorize_salary(salary):
    for _, row in salary_bands.iterrows():
        if row['Min_Salary'] <= salary <= row['Max_Salary']:
            return row['Category']
    return 'Unknown'

population['Salary_Category'] = population['Salary'].apply(categorize_salary)

# 4. Har bir salary category bo‘yicha statistikalarni hisoblash
category_stats = population.groupby('Salary_Category').agg(
    population_count=('Salary', 'count'),
    average_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median')
).reset_index()

# 5. Har bir kategoriya uchun aholi foizini hisoblash
total_population = population.shape[0]
category_stats['population_percentage'] = (
    category_stats['population_count'] / total_population * 100
)

print("Overall Salary Category Statistics:")
print(category_stats)

# 6. Har bir shtat (State) bo‘yicha ham xuddi shu statistikalarni hisoblash
state_stats = population.groupby(['State', 'Salary_Category']).agg(
    population_count=('Salary', 'count'),
    average_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median')
).reset_index()

# Har bir shtat bo‘yicha foiz hisoblash
state_total = population.groupby('State')['Salary'].count().reset_index(name='state_total')
state_stats = state_stats.merge(state_total, on='State')
state_stats['population_percentage'] = (
    state_stats['population_count'] / state_stats['state_total'] * 100
)

print("\nSalary Category Statistics by State:")
print(state_stats)





