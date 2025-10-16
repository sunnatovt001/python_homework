# Homework
# Lesson-13

# Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

from datetime import date

# Foydalanuvchidan tug‘ilgan sanani so‘rash
yil = int(input("Tug‘ilgan yilingizni kiriting: "))
oy = int(input("Tug‘ilgan oyingizni kiriting: "))
kun = int(input("Tug‘ilgan kuningizni kiriting: "))

# Bugungi sanani olish
bugun = date.today()
tugilgan_sana = date(yil, oy, kun)

# Yoshni hisoblash
yosh_yil = bugun.year - tugilgan_sana.year
yosh_oy = bugun.month - tugilgan_sana.month
yosh_kun = bugun.day - tugilgan_sana.day

# Agar oy yoki kun manfiy bo‘lsa, tuzatish
if yosh_kun < 0:
    yosh_oy -= 1
    # O‘tgan oyning kunlarini hisoblash
    oldingi_oy = bugun.month - 1 or 12
    oldingi_yil = bugun.year if bugun.month != 1 else bugun.year - 1
    kunlar_soni = (date(oldingi_yil, oldingi_oy % 12 + 1, 1) - date(oldingi_yil, oldingi_oy, 1)).days
    yosh_kun += kunlar_soni

if yosh_oy < 0:
    yosh_yil -= 1
    yosh_oy += 12

print(f"Siz {yosh_yil} yil, {yosh_oy} oy va {yosh_kun} kun yoshsiz.")



# Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

from datetime import date, datetime

# Foydalanuvchidan tug‘ilgan sanasini so‘rash
yil = int(input("Tug‘ilgan yilingizni kiriting: "))
oy = int(input("Tug‘ilgan oyingizni kiriting: "))
kun = int(input("Tug‘ilgan kuningizni kiriting: "))

# Bugungi sana
bugun = date.today()

# Shu yilgi tug‘ilgan kun sanasi
tugilgan_sana = date(bugun.year, oy, kun)

# Agar tug‘ilgan kun allaqachon o‘tgan bo‘lsa, keyingi yilga o‘tkazamiz
if tugilgan_sana < bugun:
    tugilgan_sana = date(bugun.year + 1, oy, kun)

# Farqni hisoblash
farq = tugilgan_sana - bugun

print(f"Sizning keyingi tug‘ilgan kuningizgacha {farq.days} kun qoldi")



# Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.

from datetime import datetime, timedelta

# Foydalanuvchidan hozirgi sana va vaqtni so‘rash
hozirgi_sana_vaqt = input("Hozirgi sana va vaqtni kiriting (masalan: 2025-10-16 14:30): ")

# Kiritilgan ma'lumotni datetime formatiga o‘tkazish
hozirgi_vaqt = datetime.strptime(hozirgi_sana_vaqt, "%Y-%m-%d %H:%M")

# Uchrashuv davomiyligini kiritish
soat = int(input("Uchrashuv necha soat davom etadi: "))
daqiqa = int(input("Qo‘shimcha necha daqiqa davom etadi: "))

# Tugash vaqtini hisoblash
davomiylik = timedelta(hours=soat, minutes=daqiqa)
tugash_vaqti = hozirgi_vaqt + davomiylik

# Natijani chiqarish
print(f"Uchrashuv {tugash_vaqti.strftime('%Y-%m-%d %H:%M')} da tugaydi.")



# Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.

from datetime import datetime
import pytz  # vaqt mintaqalari bilan ishlash uchun

# Foydalanuvchidan ma'lumotlarni olish
sana_vaqt_str = input("Sana va vaqtni kiriting (masalan: 2025-10-16 15:30): ")
joriy_tz = input("Joriy vaqt mintaqangizni kiriting (masalan: Asia/Tashkent): ")
maqsad_tz = input("Qaysi mintaqaga o‘tkazmoqchisiz? (masalan: Europe/London): ")

# Sana va vaqtni datetime formatiga o‘tkazish
naive_datetime = datetime.strptime(sana_vaqt_str, "%Y-%m-%d %H:%M")

# Vaqt mintaqasini belgilash
joriy_mintaqa = pytz.timezone(joriy_tz)
aware_datetime = joriy_mintaqa.localize(naive_datetime)

# Boshqa vaqt mintaqasiga o‘tkazish
maqsad_mintaqa = pytz.timezone(maqsad_tz)
converted_time = aware_datetime.astimezone(maqsad_mintaqa)

# Natijani chiqarish
print(f"{joriy_tz} vaqti bo‘yicha {sana_vaqt_str} bu {maqsad_tz} vaqti bo‘yicha {converted_time.strftime('%Y-%m-%d %H:%M')} ga to‘g‘ri keladi.")



# Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).

from datetime import datetime
import time

# Foydalanuvchidan ma'lumot olish
target_str = input("Kelajakdagi sana va vaqtni kiriting (masalan: 2025-10-17 08:00): ")

# Sana va vaqtni datetime formatiga o‘tkazish
target_time = datetime.strptime(target_str, "%Y-%m-%d %H:%M")

print("\nTaymer boshlandi... ⏳\n")

while True:
    # Hozirgi vaqt
    now = datetime.now()
    # Qolgan vaqtni hisoblash
    remaining = target_time - now

    # Agar vaqt tugagan bo‘lsa
    if remaining.total_seconds() <= 0:
        print("⏰ Vaqt tugadi!")
        break

    # Qolgan kun, soat, daqiqa, soniya
    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Ekranga chiqarish
    print(f"Qoldi: {days} kun, {hours:02d}:{minutes:02d}:{seconds:02d}", end="\r")

    # Har 1 soniyada yangilash
    time.sleep(1)



# Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.

import re  # muntazam ifodalar (regex) uchun

# Foydalanuvchidan email manzilni so‘rash
email = input("Email manzilingizni kiriting: ")

# Email uchun to‘g‘ri format andozasi
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Tekshirish
if re.match(pattern, email):
    print("✅ Email manzili to‘g‘ri formatda.")
else:
    print("❌ Email manzili noto‘g‘ri formatda.")



# Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".

# Foydalanuvchidan telefon raqamini olish
raqam = input("Telefon raqamingizni kiriting (faqat raqamlar, masalan: 1234567890): ")

# Faqat raqamlarni ajratib olish (agar foydalanuvchi bo‘sh joy yoki belgi kiritsa)
raqam = ''.join(filter(str.isdigit, raqam))

# Tekshirish — 10 ta raqam kiritilganmi
if len(raqam) == 10:
    formatlangan = f"({raqam[:3]}) {raqam[3:6]}-{raqam[6:]}"
    print("📞 Formatlangan raqam:", formatlangan)
else:
    print("❌ Iltimos, aniq 10 ta raqam kiriting (masalan: 1234567890).")



# Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

import re

# Foydalanuvchidan parolni olish
password = input("Parolni kiriting: ")

# Shartlarni tekshirish
min_length = len(password) >= 8
has_upper = re.search(r"[A-Z]", password)
has_lower = re.search(r"[a-z]", password)
has_digit = re.search(r"[0-9]", password)

# Natijani baholash
if min_length and has_upper and has_lower and has_digit:
    print("✅ Parolingiz kuchli!")
else:
    print("❌ Parolingiz zaif.")
    print("Parol quyidagi talablarga javob berishi kerak:")
    if not min_length:
        print("- Kamida 8 ta belgidan iborat bo‘lishi kerak.")
    if not has_upper:
        print("- Kamida bitta katta harf bo‘lishi kerak (A–Z).")
    if not has_lower:
        print("- Kamida bitta kichik harf bo‘lishi kerak (a–z).")
    if not has_digit:
        print("- Kamida bitta raqam bo‘lishi kerak (0–9).")



# Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

import re

# Namunaviy matn
matn = """Python is a powerful programming language. 
Many people learn Python because Python is easy to read and write."""

# Foydalanuvchidan so‘z kiritish
soz = input("Qaysi so‘zni qidirmoqchisiz? ")

# So‘zni qidirish (case-insensitive — katta/kichik harf farqsiz)
mosliklar = re.findall(rf"\b{soz}\b", matn, re.IGNORECASE)

# Natijani chiqarish
if mosliklar:
    print(f"✅ '{soz}' so‘zi matnda {len(mosliklar)} marta uchradi.")
else:
    print(f"❌ '{soz}' so‘zi matnda topilmadi.")



# Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.

import re

# Foydalanuvchidan matn kiritish
matn = input("Matn kiriting (masalan: I was born on 2005-07-21 and my brother on 12/03/2010): ")

# Sana formatlarini aniqlash uchun andoza (regex)
pattern = r"\b(?:\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})\b"

# Mosliklarni topish
sanalar = re.findall(pattern, matn)

# Natijani chiqarish
if sanalar:
    print("✅ Matnda quyidagi sanalar topildi:")
    for s in sanalar:
        print("-", s)
else:
    print("❌ Matnda sana topilmadi.")



