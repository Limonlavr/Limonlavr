import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
is_game = True
while is_game:
    computer = [random.choice(cards)]
    player = [random.choice(cards)]
    score = 0
    get_card = "y"
    while get_card == "y":
        player.append(random.choice(cards))
        if sum(player) > 21 and 11 in player:
            """Если туз в руке и сумма > 21"""
            for i  in range(0, len(player)):
                if player[i] == 11:
                   player[i] = 1
                   break
    score = sum(player)
    print (f"Твоя рука: {player}.Очков:{score}")
    print(f"Первая компьютера:",computer[0])
    if score > 21:
        get_card = "n"
    else:
        get_card = input("y - Взять карту, n = оставить: ")
    computer.append(random.choice(cards))
    if sum(computer) > 21 and 11 in player:
        """Если туз в руке и сумма > 21"""
        for i in range(0, len(computer)):
            if computer[i] == 11:
                computer[i] = 1
                break
    score_computer = sum(computer)
    print("=" * 10)
    print(f"Твоя итоговая рука: {player}.Очков:{score_computer}")


    if score > 21 and score_computer > 21
        print("Перелёт у обоих")
    elif player > 21:
        print("Твой перилёт")
    elif score_computer > 21
        print("Компьютер проиграл")
    elif score == score_computer
        print("Ничья")
    elif score > score_computer:
        print("Победа")
    else:
        print("Проиграл")

    is_game = input("Играть дальше y - да, n - нет")
