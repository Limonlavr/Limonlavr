# # # множество
# # # # 1) Повторные исключены
# # # # 2) нутри только неизменяемые типы даных
# # # # 3) Неупорядоченное содержимое
# # # # 4) пустое множество - только set ()

  #слвари
 #1) Пустой словарь - либо dict(), либо {}
# 2) {Ключ: значение} В качестве ключя допускаются любые тип
# x = "Переменная"
# d = {True: 1}
#
# # Первой задачяй
# phrase = "Я всегда я, когда я есть я.".lower()
# symbols = list("!.,?") # нежелательные знаки
# phrase_cleared = ""
# for dfg in phrase:
#     if dfg not in symbols:
#             phrase_cleared += dfg
#
# l = phrase_cleared.split(" ")
# d ={}
# for element in l :
#     if element not in d:
#      d[element] = 1 # первое восхождение слова. запись в словарь
#     else: # сли запись уже есть
#         d[element] += 1
# print(d)

# Задачя вторая
# pokupki = {"Чипсы": 78,
#            "Кириешки": 13,
#            "Яйца деда мороза": 70,
#            "Правая почка": 999}
# s = 0 #  будущяя сумма нашего чека
#
# # for i in pokupki:
# for i in pokupki.values():  # Перебор по значениям
#    s += i
# print(s)

# Задачя четвёртая
phrase = "Я всегда я, когда я есть я.".lower()
symbols = list("!.,?") # нежелательные знаки
phrase_cleared = ""
for dfg in phrase:
    if dfg not in symbols:
            phrase_cleared += dfg

l = phrase_cleared.split(" ")
d ={}
for element in l :
    if element not in d:
     d[element] = 1 # первое восхождение слова. запись в словарь
    else: # сли запись уже есть
        d[element] += 1
print(d)
maxi = max(d.values)
print(maxi)
for (key, value) in d.items():
     print(key,value)
     if value == maxi:
         print(f"{key}: {value}")