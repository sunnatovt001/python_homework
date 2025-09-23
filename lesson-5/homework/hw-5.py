#Homework
#Lesson-5
#A year is a leap year if:
#- It is divisible by 4, and
#- It is NOT divisible by 100, unless it is also divisible by 400.

#Parameters:
#year (int): The year to be checked.

#Returns:
#bool: True if the year is a leap year, False otherwise.
#"""
#if not isinstance(year, int):
#    raise ValueError("Year must be an integer.")

#return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def is_leap(year: int) -> bool:
    """
    Yil kabisa yili bo‘ladi agar:
    - 4 ga bo‘linsa, va
    - 100 ga bo‘linmasa, faqat 400 ga ham bo‘linishi bundan mustasno.

    Parametrlar:
        year (int): Tekshiriladigan yil.

    Qaytaradi:
        bool: Agar yil kabisa yili bo‘lsa True, aks holda False.
    """
    if not isinstance(year, int):
        raise ValueError("Yil butun son bo‘lishi kerak.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Sinov
print(is_leap(2020))  # True
print(is_leap(1900))  # False
print(is_leap(2000))  # True
print(is_leap(2023))  # False



#2. Conditional Statements Exercise
def check_number(n: int):
    if n % 2 == 1:
        print("Toq")
    elif 2 <= n <= 5:
        print("Juft")
    elif 6 <= n <= 20:
        print("Toq")
    else:  # n > 20 va juft
        print("Juft")


# Namuna sinov
n = int(input("Istalgan son kiriting. Men sizga uni toq yoki juft ekanligini aniqlayman:").strip())
check_number(n)



#Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
#Give two solutions.

#Solution 1 with if-else statement.

#Solution 2 without if-else statement.

def  even_numbers_if_else(a: int, b: int):
    if a % 2 != 0:   # agar a toq bo‘lsa, keyingi juftdan boshlanadi
        a += 1
    if b % 2 != 0:   # agar b toq bo‘lsa, oldingi juftda tugaydi
        b -= 1
    if a > b:        # agar oraliqda juft son bo‘lmasa
        return []
    return list(range(a, b + 1, 2))


# Sinov
print(even_numbers_if_else(3, 10))  # [4, 6, 8, 10]
print(even_numbers_if_else(2, 5))   # [2, 4]






def even_numbers_no_if(a: int, b: int):
    start = a + (a % 2)   # a juft bo‘lsa o‘zi, toq bo‘lsa keyingisi
    end = b - (b % 2)     # b juft bo‘lsa o‘zi, toq bo‘lsa oldingisi
    return list(range(start, end + 1, 2)) if start <= end else []


# Sinov
print(even_numbers_no_if(3, 10))  # [4, 6, 8, 10]
print(even_numbers_no_if(2, 5))   # [2, 4]
