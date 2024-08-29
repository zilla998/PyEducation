import random

bot = random.randint(1, 3)
player = input("Введи 1 - Камень, 2 - Бумага, 3 - Ножницы: ")

if bot == 1 and player == 1:
    result = "Ничья"

if bot == 1 and player == 2:
    result = "Ты выйграл"

if bot == 1 and player == 3:
    result = "Ты проиграл"

if bot == 2 and player == 1:
    result = "Ты проиграл"

if bot == 2 and player == 2:
    result = "Ничья"

if bot == 2 and player == 3:
    result = "Ты выйграл"

if bot == 3 and player == 1:
    result = "Ты выйграл"

if bot == 3 and player == 2:
    result = "Ты проиграл"

if bot == 3 and player == 3:
    result = "Ничья"
