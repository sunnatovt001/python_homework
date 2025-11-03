# Homework
#Lesson-18


# Homework 2:


import pandas as pd

df = pd.read_csv('tackoverflow_qa.csv')
df.head()



#Find all questions that were created before 2014
before = df[df['creationdate'] < '2014-01-01']
before


#Find all questions with a score more than 50
more_than = df[df['score'] > 50]

more_than


# Find all questions with a score between 50 and 100
between = df[(df['score'] > 50) & (df['score'] < 100)]
between


# Find all questions answered by Scott Boston
answered_by_scott = df[df['ans_name'] == 'Scott Boston']

answered_by_scott


# Find all questions answered by the following 5 users

users = ['Scott Boston', 'Jon Skeet', 'Martijn Pieters', 'Chris Pratt', 'Alex Martelli']

# Shu foydalanuvchilar javob bergan savollarni topish
answered_by_5 = df[df['ans_rep'].isin(users)]

answered_by_5


# Find all questions answered by the following 5 users

users = ['Scott Boston', 'Jon Skeet', 'Martijn Pieters', 'Chris Pratt', 'Alex Martelli']

# Shu foydalanuvchilar javob bergan savollarni topish
answered_by_5 = df[df['ans_rep'].isin(users)]

answered_by_5


# Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.

df['creationdate'] = pd.to_datetime(df['creationdate'])

filtered = df[
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'] == 'unutbu') &
    (df['score'] <5)
]

filtered



# Find all questions that have score between 5 and 10 or have a view count of greater than 10,000

filtered = df[
    ((df['score'] >= 5) & (df['score'] <= 10)) |
    (df['viewcount'] > 10000)
]

filtered


# Find all questions that are not answered by Scott Boston

not_scott = df[df['ans_name'] != 'Scott Boston']

not_scott


#Homework 3:

#Titanic data set, stored as CSV. The data consists of the following data columns:

#PassengerId: Id of every passenger.
#Survived: Indication whether passenger survived. 0 for yes and 1 for no.
#Pclass: One out of the 3 ticket classes: Class 1, Class 2 and Class 3.
#Name: Name of passenger.
#Sex: Gender of passenger.
#Age: Age of passenger in years.
#SibSp: Number of siblings or spouses aboard.
#Parch: Number of parents or children aboard.
#Ticket: Ticket number of passenger.
#Fare: Indicating the fare.
#Cabin: Cabin number of passenger.
#Embarked: Port of embarkation.

titanic_df = pd.read_csv("titanic.csv")
titanic_df.head()


# Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.

df = pd.read_csv('titanic.csv')

female_class1_20_30 = df[
    (df['Sex'] == 'female') &
    (df['Pclass'] == 1) &
    (df['Age'] >= 20) &
    (df['Age'] <= 30)
]

female_class1_20_30


# Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.

paid_over_100 = df[df['Fare'] > 100]

paid_over_100


# Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).

alone_survivors = df[
    (df['Survived'] == 1) &
    (df['SibSp'] == 0) &
    (df['Parch'] == 0)
]

alone_survivors


# Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.

filtered = df[(df['Embarked'] == 'C') & (df['Fare'] > 50)]

filtered


# Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.
filtered = df[(df['SibSp'] >0) & (df['Parch'] >0)]

filtered



# Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.

filtered = df[(df['Age'] <= 15) & (df['Survived'] == 0)]

filtered


# Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.

filtered = df[(df['Cabin'].notnull()) & (df['Fare'] > 200)]

filtered


# Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.

filtered = df[df['PassengerId'] % 2 != 0]

filtered


# Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.

filtered = df[df['Ticket'].duplicated(keep=False) == False]

filtered


# Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.

filtered = df[(df['Name'].str.contains('Miss')) & (df['Pclass'] == 1) & (df['Sex'] == 'female')]

filtered


