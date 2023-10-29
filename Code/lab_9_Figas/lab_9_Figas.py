# alphabet = "abcdefghijklmnopqrstuvwxyz"
# ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
# line = input("Enter message: ")
# move = ""
# while type(move) != int or move < 1 or move > 25:
#     while type(move) != int:
#         try:
#             move = int(input("Enter number of moves: "))
#         except:
#             print("Error: Wrong data")
#     if move < 1 or move > 25:
#         print("Error: Number of moves less then 1 or more then 25")
#         move = ""
#     else:
#         break
# print("You message: " + line)
#
# cryptogram = ""
# for char in line:
#     if not char.isalpha():
#         cryptogram += char
#         continue
#     if char.isupper():
#         index = ALPHABET.find(char)
#         index = (index+move) % 26
#         cryptogram += ALPHABET[index]
#     elif char.islower():
#         index = alphabet.find(char)
#         index = (index+move) % 26
#         cryptogram += alphabet[index]
# print("You cryptogram: " + cryptogram)
print('smith' > 'Smith')
print('Smiths' < 'Smith')
print('Smith' > '1000')
print('11' < '8')

s1 = '12.8'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)