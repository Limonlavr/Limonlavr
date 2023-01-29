print("Добро пожаловать в игру быстрый стрелок")
print("Правила игры: когда пишет стреляь то вы должны нажать entr это означяент что вы выстрельнули а если вы не успели")
print(" за 0.3 сек то тогда ты проиграл")
import random, time
input("нажми Enter, чтобы продолжить")
print("готовся к выстрелу")
sekynd = random.randint(2, 5)
time.sleep(sekynd)
start = time.time()
input("Стреляй")
end = time.time() - start

print(end)
if end > 0.5:
    print("😴😴😴😴😴😴 далеко до стмпла")