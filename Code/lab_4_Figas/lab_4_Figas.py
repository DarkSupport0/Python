# Task 1 #
n = int(input("Введіть ціле число: "))
print(n >= 100)


# Task 2 #
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
if a>b:
    print("Перше число більше ніж друге")
else:
    print("Друге число більше першого чи дорівнює йому")


# Task 3 #
flover = input("Give me Spathiphyllum ^^\n")
if flover == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever! *_*")
elif flover == "spathiphyllum":
    print("No, I want a big Spathiphyllum! ^^")
else: print("Spathiphyllum! Not "+flover+"! :(")


# Task 4 #
stonks = round(float(input("Скажи мені свій дохід роковий: ")), 2)
if stonks <= 85528:
    rent = round((stonks * 0.18 - 556), 2)
else:
    rent = round((14839.02 + (stonks - 85528) * 0.32), 2)
if rent > 0:
    print("Податки від доходу дорівнюють: "+str(rent)+" талерів")
else:
    print("Податки від доходу дорівнюють: 0.0 талерів")


# Task 5 #
year = int(input("Введіть свій рік: "))
if year < 1582:
    print("Not within the Gregorian calendar period.")
elif year % 4 != 0:
    print("Common year")
else:
    print("Leap year")


# Task 6 #
secret_number = 8
number = int(input("Спробуй вгадати число:) : "))
while number != secret_number:
    print("Ха-ха! Ви застрягли у моїй петлі!")
    number = int(input("Спробуй вгадати число:) : "))
print("Молодець, магле! Тепер ти вільний")


# Task 7 #
import time
for i in range (1, 11):
    print(str(i)+" Mississippi")
    time.sleep(1)
print("Ready or not, I`m coming!")


# Task 8 #
while True:
    secret_code = input("Введіть слово: ")
    if secret_code == "chupacabra":
        break
print("You've successfully left the loop.")


# Task 9 #
user_word = (input("Input english word: ")).upper()
for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I"\
            or letter == "O" or letter == "U":
        continue
    print(letter)


# Task 10 #
user_word = (input("Input english word: ")).upper()
word_without_vowers = ""
for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I"\
            or letter == "O" or letter == "U":
        continue
    word_without_vowers += letter
print(word_without_vowers)


# Task 11 #
blocks = int(input("Введіть кількість блоків: "))
levels = 0
for i in range(1,blocks):
    if blocks - i >= 0:
        levels += 1
        blocks -= i
    else: break
print("The height of the pyramid: "+str(levels))


# Task 12 #
c0 = int(input("Введіть ціле додатнє число: "))
while c0 <= 0:
    c0 = int(input("Введіть ціле додатнє число: "))
i = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 /= 2
    else:
        c0 = 3*c0+1
    i += 1
    print(str(i) + " iteration:\t" + str(c0))
    time.sleep(0.2)
