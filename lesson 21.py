# try:
#     x = int(input("Ведите число: "))
#     print(10 / x)
# except (ValueError, ZeroDivisionError):
#     print("бла бла бла бал")
# except Exception:
#     pass


# x = input("имя друга:")
# try:
#     if x == "Антон":
#         raise

# Задачя 1 ---------------------------------------------------------------------------------------
# def skladivanie():
#     s = 0
#     k = 0
#     for number in content:
#         s += int(number)
#         k += 1
#     return round(s / k, 2)
#
#
# try:
#     f = open("file.txt", "r")
# except FileNotFoundError:
#     print("файла нет")
# content = f.read().split()
# print(content)
#
# print(skladivanie())
#

# Задачя 2
try:
    f = open("file.txt", "r", encoding="utf - 8")
except FileNotFoundError:
    print("файла нет")
    exit()
content = f.readlines()
print(content)


for i, student in enumerate(content):
    content[i] = student.split()

print(content)

maxi = - 1
imya = ""
familya = ""
for student in content:
    if student[3] > maxi:
        maxi = student[3]
print(maxi)





















