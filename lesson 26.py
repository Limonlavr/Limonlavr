# #Задачя 1
# c1=input("Введите первый цвет:").lower().split()
# c2=input("Введите первый цвет:").lower().split()
# c=("красный", "синий", "жёлтый")
# if (c2 not in c) or (c1 not in c):
#     print("Один из основных цветов ввудён неверно!")
#
#
# elif (c1 ==c[0] and c2 == c[2]) or (c1 == c[2] and c2 == c[0]):
#     print("Оранжевый")
# elif (c1 ==c[1] and c2 == c[2]) or (c1 == c[2] and c2 == c[1]):
#     print("Зелёный")
# elif (c1 ==c[0] and c2 == c[1]) or (c1 == c[1] and c2 == c[0]):
#     print("Фиолетовый")
#
# else:
#    print(c1)


#Задачя 2
nach = input("Начало первого урока (чч:мм): ")
diur = int(input("Длительность урока (мин): "))
dip = int(input("Длительность перемен (мин): "))
n = int(input("На сколько уроков нужно расписание: "))
# split = nach.split(":")
# h = split[0]
# m = split[1]
h, m = nach.split(":")
h,m = int(h), int(m)
time = h * 60 + m
for i in range(n):
    print(f"Урок {i+1}:", end="")
    h = time // 60
    m = time % 60
    print(f"{str(h).rjust(2,'0')}:{str(m).rjust(2,'0')}")
    time = time + diur
    print(f"{str(h).rjust(2, '0')}:{str(m).rjust(2, '0')})




