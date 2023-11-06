# # Example 1 #
#
# def ispalindrom(text):
#     text = text.replace(" ", "").lower()
#     if text == text[::-1]:
#         print("It's a palindrom")
#     else:
#         print("It's not a palindrom")
#
# text = input("Введіть текст:")
# ispalindrom(text)
#
# text = input("Введіть текст:")
# ispalindrom(text)


# # Example 2 #
#
# text1 = input("Введіть перше слово:")
# text2 = input("Введіть друге слово:")
#
# text1 = list(text1.replace(" ", "").lower())
# text2 = list(text2.replace(" ", "").lower())
#
# if sorted(text1) == sorted(text2):
#     print("Анаграми")
# else:
#     print("Не анаграми")


# # Example 3 #
#
# date = input("Введіть дату народження у форматі YYYYMMDD:")
# while True:
#     sum = 0
#     for simbol in date:
#         sum += int(simbol)
#     date = str(sum)
#     if len(date) == 1:
#         break
# print(sum)


# Task 1 #
def are_letters_hidden(word, combination):
    word = word.lower()
    combination = combination.lower()
    for letter in word:
        index = combination.find(letter)
        if index == -1:
            return 'No'
        combination = combination[index+1:]
    return 'Yes'

word = input("Input world: ")
combination = input("Input letter combination: ")
print(are_letters_hidden(word, combination))


# # Example 4 #
# while True:
#     try:
#         number = int(input("Введіть ціле число: "))
#         print(number/2)
#         break
#     except:
#         print("Введене значення не є допустимим числом. Повторіть спробу...")


# Task 2 #
while True:
    try:
        date = int(input("Введіть дату народження у форматі YYYYMMDD:"))
        if len(str(date)) == 8:
            break
        else:
            print("У ряду має бути 8 чисел")
    except:
        print("Введений рядок не є цілим числом")
date = str(date)
while True:
    sum = 0
    for simbol in date:
        sum += int(simbol)
    date = str(sum)
    if len(date) == 1:
        break
print(sum)


# Task 3 #
while True:
    try:
        number = int(input("Input number: "))
        min = int(input("Input min value: "))
        max = int(input("Input max value: "))
        if number >= min and number <= max:
            break
        else:
            print(f"Error: the value is not within permitted range ({min}..{max})")
    except:
        print("Error: wrong input")
print("You number is " + str(number))
