def  munusF(f):
  global beans
  beans=beans - f


print("у вас есть кучя .фасоли из 20 фасолей")
beans=20

while True:
# ход первого игрока
  while True:   # буск. цикл
      f1=int(input("колько фасоли уберём первый игрок?(от 1 до 3 )"))
      if f1 > 0 and f1 < 3:     # Валидация (проверка значения)
        break  # Выход из цикла
  munusF(f1)
  if beans < 1:
      break
  print(beans)
  #ход втарово игрока
  while True:   # буск. цикл
      f2=int(input("солько фасоли уберём второй игрок?(от 1 до 3 )"))
      if f2 > 0 and f2 < 3:     # Валидация (проверка значения)
        break
  munusF(f2)
  if beans < 1:
      break
  print(beans)
