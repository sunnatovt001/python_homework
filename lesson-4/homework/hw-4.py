#GitHub  HOMEWORK  Lesson-3
#Python Dictionary and Set Exercises
#Dictionary Exercises

#1. Sort a Dictionary by Value
#Write a Python script to sort (ascending and descending) a dictionary by value.



my_dict = {"a": 3, "b": 1, "c": 4, "d": 2}
# Ascending (o‘sish tartibida)
asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))

# Descending (kamayish tartibida)
desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

asc
desc


#2. Add a Key to a Dictionary
#Write a Python script to add a key to a dictionary.

#Sample Dictionary:
raqamlar = {0: 10, 1: 20}
# Yangi kalit va qiymat qo'shamiz
raqamlar[2] = 30

raqamlar


#3. Concatenate Multiple Dictionaries
#Write a Python script to concatenate the following dictionaries to create a new one.

#Sample Dictionaries:
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

umumiy = {**dic1, **dic2, **dic3}
umumiy


#4. Generate a Dictionary with Squares
#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

#Sample Dictionary (n = 5):
raqamlar = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n = 5
raqamlar = {x: x*x for x in range(1, n+1)}
raqamlar


#5. Dictionary of Squares (1 to 15)
#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

#Expected Output:
#raqamlar = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

raqamlar = {i: i*i for i in range(1, 16)}
print(raqamlar)





#Set Exercises

#1. Create a Set
#Write a Python program to create a set.

my_set = {1, 2, 3, 4, 5}
print(my_set)


#2. Iterate Over a Set
#Write a Python program to iterate over sets.

my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item)


#3. Add Member(s) to a Set
#Write a Python program to add member(s) to a set.

my_set = {1, 2, 3}
my_set.add(4)         # Bitta element qo'shish
my_set.update([5, 6]) # Bir nechta element qo'shish

print(my_set)


#4. Remove Item(s) from a Set
#Write a Python program to remove item(s) from a given set.

my_set = {1, 2, 3, 4, 5}
my_set.remove(3)      # 3 ni o'chirish
my_set.discard(6)     # 6 yo'q bo'lsa ham xatolik chiqarmaydi
my_set.pop()          # Tasodifiy elementni o'chiradi

print(my_set)


#5. Remove an Item if Present in the Set
#Write a Python program to remove an item from a set if it is present in the set.

my_set = {1, 2, 3, 4, 5}
item = 3

if item in my_set:
    my_set.remove(item)

print(my_set)
