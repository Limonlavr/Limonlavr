# print(5/0)
#
# x = 15/ 0

# x = 15 + "a"

# lst = [10, 5, 3]
# print(lst[3])
# #Коды завершения
# # 0 всё хорошо
# # 1 ошибка
# ша 5 > 0

# assert
def summa(number: list[int])
    return sum(number)

assert summa ([1,3,5,18]) == 27
assert summa ([1,3]) == 4 # ошибки не будет
assert summa ([1,3]) == 5 # ошибка AssertionError

try:
x = 5/0
   print("шибка")
print