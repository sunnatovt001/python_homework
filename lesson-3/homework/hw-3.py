#Homework: List and Tuple Exercises

#1. Create and Access List Elements
#Create a list containing five different fruits and print the third fruit.
mevalar = ['olma', 'anor', 'shaftoli', 'behi', 'nok']
print(mevalar[2])  # shaftoli

#2. Concatenate Two Lists
#Create two lists of numbers and concatenate them into a single list.
sonlar1 = [1,2,3]
sonlar2 = [4,5,6]
sonlar3 = sonlar1 + sonlar2
print(sonlar3)  # [1, 2, 3, 4, 5, 6]

#3. Extract Elements from a List
#Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
sonlar = [10,20,30,40,50]
print(sonlar[0])  # 10
print(sonlar[len(sonlar)//2])  # 30
print(sonlar[-1])  # 50

#4. Convert List to Tuple
#Create a list of your five favorite movies and convert it into a tuple.
kinolar = ['Inception', 'Interstellar', 'The Dark Knight', 'Pulp Fiction', 'The Matrix']
kinolar_tupple = tuple(kinolar)
print(kinolar_tupple)  # ('Inception', 'Interstellar', 'The Dark Knight', 'Pulp Fiction', 'The Matrix')

#5. Check Element in a List
#Given a list of cities, check if "Paris" is in the list and print the result.
shaharlar = ["London", "New York", "Tokyo", "Paris", "Berlin"]
if "London" in shaharlar:
    print("London ro'yxatda bor")
else:
    print("London ro'yxatda yo'q")

#6. Duplicate a List Without Using Loops
#Create a list of numbers and duplicate it without using loops.
raqamlar = [1,2,3]
duplikat_raqamlar = raqamlar * 2
print(duplikat_raqamlar)  # [1, 2, 3, 1, 2, 3]

#7. Swap First and Last Elements of a List
#Given a list of numbers, swap the first and last elements.
# sonlar roʻyxati
sonlar_royhati = [10, 20, 30, 40, 50]

# birinchi va oxirgi elementlarni almashtirish
sonlar_royhati[0], sonlar_royhati[-1] = sonlar_royhati[-1], sonlar_royhati[0]

print(sonlar_royhati)

#8. Slice a Tuple
#Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sonlar_3_7 = sonlar[3:7]
print(sonlar_3_7)  # [4, 5, 6, 7]

#9. Count Occurrences in a List
#Create a list of colors and count how many times "blue" appears in the list.
ranglar = ["red", "blue", "green", "blue", "yellow", "blue"]
print(ranglar.count("blue"))  # 3

#10. Find the Index of an Element in a Tuple
#Given a tuple of animals, find the index of "lion".
animals = ("tiger", "elephant", "lion", "giraffe")
print(animals.index("lion"))  # 2
