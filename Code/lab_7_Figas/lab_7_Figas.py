# Task 1 #
korteg = ()
count = int(input("Кількість чисел у масиві: "))
for i in range(0, count):
    element = int(input(str(i + 1) + "й елемент масиву = "))
    korteg += (element,)
min = int(input("Введіть мінімальне число для сортування: "))
result = ()
for i in korteg:
    if i < min:
        result += (i,)
print("Числа, які меньше числа "+str(min)+": "+str(result))


# Task 2 #
line1 = "Hello"
line2 = "dear friend"
line3 = "are you ok"
line4 = "you look not good"
line = (line1,line2,line3,line4)
print(line[0],line[1],line[2],line[3],sep=", ",end="?")


# Task 3 #
books = {
    "Гордість і упередження":("Джейн Остен","1813 рік","322 сторінок"),
    "1984":("Джордж Оруэлл","1949 рік","312 сторінок"),
    "Великий Гетсбі":("Ф. С. Фицджеральд","1925 рік","397 сторінок"),
    "Маленькі жінки":("Луиза Мэй Олкотт","1868/1869 роки","382 сторінок"),
    "451 по Фаренгейту":("Рэй Брэдбери","1953 рік","224 сторінки"),
    "Джейн Ейр":("Шарлотта Бронте","1847 рік","511 сторінок"),
    "Унесені вітром":("Маргарет Митчелл","1936 рік","1056 сторінок(дві глави)"),
    "Скотний двір":("Джордж Оруэлл","1945 рік","363 сторінок"),
}
while True:
    book = input("Про яку книгу потрібна інформація?/Натисніть Enter, якщо нічого не треба ")
    if book == "":
        break
    if book in books:
        print(books[book])
    else:
        print("Цієї книги нема в архіві")

# Task 4 #
students = {
    "Батюк": ("Батюк Даніїл Сергійович", "КН-21-1"),
    "Деряга": ("Деряга Анатолій Сергійович", "КН-21-1"),
    "Єфімов": ("Єфімов Данило Вячеславович", "КН-21-2"),
    "Зеленіна": ("Зеленіна Поліна Сергіївна", "КН-21-1"),
    "Ілющенко": ("Ілющенко Данило Богданович", "КН-21-2"),
    "Кондратюк": ("Кондратюк Марія Олександрівна", "КН-21-1"),
    "Масляник": ("Масляник Олександр Олександрович", "КН-21-2"),
    "Роменський": ("Роменський В'ячеслав Олегович", "КН-21-1"),
    "Рябоконь": ("Рябоконь Олександр Володимирович", "КН-21-2"),
    "Сідєльніков": ("Сідєльніков Даніїл Сергійович", "КН-21-1"),
    "Старченко": ("Старченко Денис Вячеславович", "КН-21-2"),
    "Стойко": ("Стойко Севастян Дмитрович", "КН-21-1"),
    "Темченко": ("Темченко Олег Віталійович", "КН-21-1"),
    "Фігас": ("Фігас Ярослав Олексійович", "КН-21-2"),
    "Яловець":("Яловець Ілля Вадимович", "КН-21-1"),
}
while True:
    info = input("Про якого студента потрібна інформація?/Натисніть Enter, якщо нічого не треба ")
    if info == "":
        break
    if info in students:
        print(students[info])
    else:
        print("Цього студента немає в групі пайтона КН-21")


# Task 5 #
numbers_library = {}
while True:
    name = input("Напишіть ім'я контакту, щоб створити/додати номер телефону: ")
    if name == '':
        break
    number = input("Введіть номер телефону: ")
    if name in numbers_library:
        numbers_library[name] += (number,)
    else:
        numbers_library[name] = (number,)
while True:
    show = input("Введіть контакт, щоб вивести номера телефону/Натисніть Enter, якщо нічого не треба :")
    if show == "":
        break
    if show in numbers_library:
        print(numbers_library[show])
    else:
        print("В телефоній книзі нема цього контакту")
