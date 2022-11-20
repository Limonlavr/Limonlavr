import random

life = 10
length = 3

snswer = random.randint(100, 999)
answer =str(snswer)

while life:
    is_guessed = False
    print("="* 10)

    print("Жизней:", end="")
    for i in range(life):
        print("❤", end="")
        print()

    guess = input("Предложение: ")
    if len(guess) != length or not guess.isdigit(): # если длина != 3 или не число
        print("Число от 100 до 999")
        continue #Перизопускаем цикл

    if guess == answer:
        print("Победа🏆🏆")
        is_guessed = True
        break

    if not is_guessed:
        #Проверка на begels
       for i in range(length):
           if guess[i] == answer[i]:
               print("Fermi 😎")
               is_guessed = True
               break

    if not is_guessed:
       for char in guess:
           if char in answer: #если число в ответ
               print("Pico 😉")
               is_guessed = True
               break

    if not is_guessed: #Если не отгодал
        #не было fermi, ni pico
        print("Bagels 😭")
        life -=1