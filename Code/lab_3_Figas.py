# Task #1 #
x = float(input("Enter value for x: "))
sigma = 0.5
mu = 0.8
f_y = (1 / (sigma * (2*3.14)**0.5))*2.7**(-((x-mu)**2)/(2*sigma**2))
print(f_y)


# Task #2 #
john_apples = 3
mary_apples = 5
adam_apples = 6
print(john_apples, mary_apples, adam_apples, sep=",")
totalApple = john_apples+mary_apples+adam_apples
print(totalApple)
print("Загальна кількість яблук: "+str(totalApple))


# Task 3 #
kilometers = 12.25
miles = 7.38
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers/1.61
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")


# Task #4 #
x = input("Вставте своє значення: ")
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)


# Task #5 #
# this program computes the number of seconds in a given number of hours
hours = 2  # number of hours
seconds = 3600  # number of seconds in 1 hour
print("Hours: ", hours)  # printing the number of hours
print("Seconds in Hours: ", hours * seconds)  # printing the number of seconds in a given number of hours
hours = 3
print("Hours: ", hours)  # printing the number of hours
print("Seconds in Hours: ", hours * seconds)
# this is the end of the program that computes the number of seconds in 3 hour
print("Goodbye")
# here we should also print "Goodbye", but a programmer didn't have time to write any code


# Task #6 #
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
if b == 0:  # If division impossiple
    print(str(a) + "+" + str(b) + "=" + str(a + b), str(a) + "-" + str(b) + "=" + str(a - b),
          str(a) + "*" + str(b) + "=" + str(a * b), "Error", sep="\n")
else:
    print(str(a) + "+" + str(b) + "=" + str(a + b), str(a) + "-" + str(b) + "=" + str(a - b),
          str(a) + "*" + str(b) + "=" + str(a * b), str(a) + "/" + str(b) + "=" + str(a / b), sep="\n")
print("\nThat's all, folks!")


# Task #7 #
x = float(input("Enter value for x: "))
y = 1 / (x + (1/(x+(1/(x+(1/(x+(1/x))))))))
print("y = ", str(y))


# Task #8 #
hour = int(input("Starting time (hours): "))  # Create hour
mins = int(input("Starting time (minutes): "))  # Create minute
duration = int(input("Event duration (minutes): "))  # Add time
currentday = (hour*60+mins+duration) % 1440  # Add limit in time
currenthour = currentday / 60  # Found hour
currentmin = currentday % 60  # Found minutes
print("Current time: " + str(int(currenthour))+":" + str(int(currentmin)))


x = int(input("Enter a number: "))
print(x*"5")

x = int(input("Enter a number: "))
print(type(x))
