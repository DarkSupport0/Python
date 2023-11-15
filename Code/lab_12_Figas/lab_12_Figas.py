# class Timer:
#     def __init__(self, hours=0, minutes=0, seconds=0):
#         self._hours = hours
#         self._minutes = minutes
#         self._seconds = seconds
#
#     def __str__(self):
#         return f"{self._format_time(self._hours)}:{self._format_time(self._minutes)}:{self._format_time(self._seconds)}"
#
#     def _format_time(self, time):
#         return str(time).zfill(2)
#
#     def next_second(self):
#         self._seconds += 1
#         if self._seconds == 60:
#             self._seconds = 0
#             self._minutes += 1
#             if self._minutes == 60:
#                 self._minutes = 0
#                 self._hours += 1
#                 if self._hours == 24:
#                     self._hours = 0
#
#     def prev_second(self):
#         self._seconds -= 1
#         if self._seconds == -1:
#             self._seconds = 59
#             self._minutes -= 1
#             if self._minutes == -1:
#                 self._minutes = 59
#                 self._hours -= 1
#                 if self._hours == -1:
#                     self._hours = 23
#
#
# timer = Timer(23, 59, 59)
# print(timer)
# timer.next_second()
# print(timer)
# timer.prev_second()
# print(timer)


# class WeekDayError(Exception):
#     pass
#
#
# class Weeker:
#     DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#
#     def __init__(self, day):
#         if day not in self.DAYS:
#             raise WeekDayError
#         self._day = day
#
#     def __str__(self):
#         return self._day
#
#     def add_days(self, n):
#         current_index = self.DAYS.index(self._day)
#         new_index = (current_index + n) % 7
#         self._day = self.DAYS[new_index]
#
#     def subtract_days(self, n):
#         current_index = self.DAYS.index(self._day)
#         new_index = (current_index - n) % 7
#         self._day = self.DAYS[new_index]
#
#
# try:
#     weekday = Weeker('Mon')
#     print(weekday)
#     weekday.add_days(15)
#     print(weekday)
#     weekday.subtract_days(23)
#     print(weekday)
#     weekday = Weeker('Monday')
# except WeekDayError:
#     print("Sorry, I can't serve your request.")


# import math
#
#
# class Point:
#     def __init__(self, x=0.0, y=0.0):
#         self._x = x
#         self._y = y
#
#     def getx(self):
#         return self._x
#
#     def gety(self):
#         return self._y
#
#     def distance_from_xy(self, x, y):
#         return math.hypot(self._x - x, self._y - y)
#
#     def distance_from_point(self, point):
#         return self.distance_from_xy(point.getx(), point.gety())
#
#
# point1 = Point(0, 0)
# point2 = Point(1, 1)
# print(point1.distance_from_point(point2))
# print(point2.distance_from_xy(2, 0))


# import math
#
#
# class Point:
#     def __init__(self, x=0.0, y=0.0):
#         self.__x = x
#         self.__y = y
#
#     def getx(self):
#         return self.__x
#
#     def gety(self):
#         return self.__y
#
#     def distance_from_xy(self, x, y):
#         return math.hypot(self.__x - x, self.__y - y)
#
#     def distance_from_point(self, point):
#         return self.distance_from_xy(point.getx(), point.gety())
#
#
# class Triangle:
#     def __init__(self, side1, side2, side3):
#         self.__sides = [side1, side2, side3]
#
#     def perimeter(self):
#         lenside1 = self.__sides[0].distance_from_point(self.__sides[1])
#         lenside2 = self.__sides[1].distance_from_point(self.__sides[2])
#         lenside3 = self.__sides[2].distance_from_point(self.__sides[0])
#         return lenside1 + lenside2 + lenside3
#
#
# triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
# print(triangle.perimeter())


class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1

    def __str__(self):
        return self.breed + " says: Woof!"


class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " Don't run away, Little Lamb!"


class GuardDog(Dog):
     def __str__(self):
         return super().__str__() + " Stay where you are, Mister Intruder!"

rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")


print(rocky)
print(luna)
print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))