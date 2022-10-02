# x1 = "8"
# x2 = "4"
# x3 = "2"
#
# lst = {x1, x2, x3}
# print(lst)
# print(lst[
#
#
# x = input("Ведите слово:")
# temp = x[-1]
# print(temp)
# print(x.index(temp) + 1)
# print(len(x))

x = "C:/Python3/python.exe"

print("имя файла:", x[11:22])
print("Имя файла:", x[-10:])
print("Расширение:", x[-3:])
print("Имя каталога:", x[3:10])
print("Полный путь к катологу:",x[:10])

x1 = x.split("\\") # split - разделить, разрезать
print(x1)
print("Имя файла:", x1[2])



# chapter_1 = input("Глава 1:")
# # page_1 = input("Страница: ")
# # chapter_2 = input("Глава 2:")
# # page_2 = input("Страница: ")
# # chapter_3 = input("Глава 3:")
# # page_3 = input("Страница: ")
# #
# # # rjust
# # x = "Limon"
# # print(chapter_1, page_1.rjust(30))
# # # x.rjust(50)


text = "12'345'678" # -> 12345678
temp = text.split("'")
print(temp)
temp = temp[0] + temp[1] + temp[2]
print =
temp = text.replace("',")
number = int(temp)
