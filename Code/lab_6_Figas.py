# # Task 1 #
# def checkyear(year):
#     if year >= 1582:
#         if year % 4 == 0:
#             return True
#         else: return False
#     else: return False
#
#
# print(checkyear(2023))
# print(checkyear(2024))
#
#
# # Task 2 #
# def daysinmonth(year, month):
#     if year < 1:
#         return None
#     if month < 1 or month > 12:
#         return None
#     daymonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     daymonthfull = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if year % 4 == 0:
#         return daymonthfull[month - 1]
#     else:
#         return daymonth[month - 1]
#
#
# print(daysinmonth(4, 11))
#
# # Task 3 #
# def whatsday(year,month,day):
#     if year < 1:
#         return None
#     if month < 1 or month > 12:
#         return None
#     if day < 1 or day > 31:
#         return None
#     daymonth =     [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     daymonthfull = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if year % 4 == 0:
#         if day > daymonthfull[month-1]:
#             return None
#     else:
#         if day > daymonth[month-1]:
#             return None
#     sum = 0
#     if year % 4 == 0:
#         for i in range(0, month - 1):
#             sum += daymonthfull[i]
#     else:
#         for i in range(0, month - 1):
#             sum += daymonth[i]
#     sum += day
#     return sum
#
# print(whatsday(2024,12,31))
#
#
# # Task 4 #
# def is_prime(num):
#     count = 0
#     if num % num == 0:
#         count += 1
#     for i in range(1, num):
#         if num % i == 0:
#             count += 1
#     if count < 3:
#         return num
# for i in range(1, 200):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
#
# # Task 5 #
# def liters_100km_to_miles_gallon(liters):
#     gallon = liters / 3.785411784
#     miles = 100/1.609344
#     return miles/gallon
# def miles_gallon_to_liters_100km(miles):
#     km = miles * 1.609344 / 100
#     liters = 3.785411784
#     return liters/km
#
# print(liters_100km_to_miles_gallon(3.9))
# print(liters_100km_to_miles_gallon(7.5))
# print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))
#
# # Task 6 #
# def is_a_triangle(a, b, c):
#     if a+b>c and a+c>b and b+c>a:
#         return True
#     else: return False
#
# print(is_a_triangle(11,2,3))
# print(is_a_triangle(3,4,5))
#
# # Task 7 #
# def is_a_triangle(a, b, c):
#     if a+b>c and a+c>b and b+c>a:
#         return is_a_right_triangle(a, b, c)
#     else: return False
# def is_a_right_triangle(a, b, c):
#     if a^2+b^2==c^2 or a^2+c^2==b^2 or c^2+b^2==a^2:
#         return "It`s right triangle"
#     else: return "It`s default triangle"
#
# print(is_a_triangle(11,2,3))
# print(is_a_triangle(3,4,5))
# print(is_a_triangle(3,4,6))

