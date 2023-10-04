# Task 1 #
hat_list = [1, 2, 3, 4, 5]
print(hat_list)
place = int(input("Введіть елемент масиву, який хочете змінити(1-5): "))
while(place < 1 or place > 5):
    print("Число не у введеному проміжку, напишіть ще раз")
    place = int(input("Введіть елемент масиву, який хочете змінити(1-5): "))
value = int(input("Введіть значення елементу, на який хочете змінити: "))
hat_list[place-1] = value
print("Значення зміненого масиву: "+str(hat_list))

del hat_list[-1]
print("Значення зменшеного масиву: "+str(hat_list))

print("Розмір зменшеного масиву: "+str(len(hat_list)))


# Task 2 #
list = []
count = int(input("Кількість чисел у масиві: "))
for i in range(0, count):
    element = int(input(str(i + 1) + "й елемент масиву = "))
    list.append(element)
for i in range(0, len(list)):
    for j in range(0, len(list) - i - 1):
        if list[j] > list[j + 1]:
            soft = list[j]
            list[j] = list[j + 1]
            list[j + 1] = soft
        print(list)
print("Відсортовані числа: " + str(list))


# Task 3 #
list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique = [-999]
print("Список до змінення: " + str(list))
for i in range(0, len(list)):
    check = 0
    for j in range(0, len(unique)):
        if list[i] != unique[j]:
            check += 1
        if check == len(unique):
            unique.append(list[i])
del unique[0]
print("Список унікальних чисел: "+str(unique))


# Task 4 #
chessboard = [["_" for i in range(8)] for j in range(8)]
for i in range (0, len(chessboard)):
    for j in range (0, len(chessboard)):
        if (((i == 0 or i == 7) and (j == 0 or j == 7))):
            chessboard[i][j] = "R"
        if (((i == 0 or i == 7) and (j == 1 or j == 6))):
            chessboard[i][j] = "N"
        if (((i == 0 or i == 7) and (j == 2 or j == 5))):
            chessboard[i][j] = "B"
        if (((i == 0 or i == 7) and j == 3)):
            chessboard[i][j] = "Q"
        if (((i == 0 or i == 7) and j == 4)):
            chessboard[i][j] = "K"
        if (i == 1 or i == 6):
            chessboard[i][j] = "p"
for i in range (0, 8):
        print(chessboard[i])

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]
print(list_3)


list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2
print(list_3)


list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]
print(list_3)


list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]
print(list_3)