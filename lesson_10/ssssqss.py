import random
import datetime

while True:
    number = input("Сколько дней рождения мы генерируем? (до 65)")
    if not number.isdigit() or int(number) > 65 or int(number) < 2:
        print("Это по твоему смешно?Нормально введи, пожалуйста ☺")
        print("--------")
    else: #Правильно ввели
        number = int(number) #Переоброзование в число
        break
birhdeys = []
start0fYear = datetime.date(2022,1,1) # 2022 год, 1 месяц, 1 день
for _ in range(number): #отробатывает number раз
    randomNumberOfDays =  datetime.timedelta(random.randint(0, 364)) #Случяйеый сдвиг
    birhdey = start0fYear + randomNumberOfDays #Случайный др = старт года + свиг
    birhdeys.append(birhdey)

for i in range(number):
    print(f"{i + 1}){birhdeys[i]}")


 print("=" * 10)
 for i in set(birhdey)
     if birhdey.count(i) > 1:
         print(f"- {i.strftim('%d.%m.%y')}Встречяется{birhdeys.count(i)}")

