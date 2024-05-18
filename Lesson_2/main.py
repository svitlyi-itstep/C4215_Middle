import random

def choose_item(message):
    while True:
        choice = input(message)
        if choice not in "кнп":
            print('Некоректне значення!')
        else:
            return choice


def full_name(short_name):
    if short_name == 'к':
        return "Каміння"
    elif short_name == 'н':
        return "Ножиці"
    elif short_name == 'п':
        return "Папір"
    return "Невідомо"


def check_victory(player, bot):
    if player == bot:
        return 'd' #draw
    elif player == 'к' and bot == 'н':
        return 'p' #player
    elif player == 'к' and bot == 'п':
        return 'b' #bot
    elif player == 'н' and bot == 'п':
        return 'p'
    elif player == 'н' and bot == 'к':
        return 'b'
    elif player == 'п' and bot == 'к':
        return 'p'
    elif player == 'п' and bot == 'н':
        return 'b'
    else:
        return None


print(" - ГРА \"КАМІННЯ. НОЖИЦІ. ПАПІР.\" -")
print("\n\tк - каміння ")
print("\tн - ножиці ")
print("\tп - папір\n")


player_choice = choose_item('Оберіть предмет (к, н, п): ')
bot_choice = random.choice("кнп")

print(f'{full_name(player_choice)} проти {full_name(bot_choice)}')
game_result = check_victory(player_choice, bot_choice)
if game_result == 'd':
    print('Нічия')
elif game_result == 'p':
    print('Ви перемогли!')
elif game_result == 'b':
    print('Переміг комп\'ютер')
else:
    print('Визначити результат не вдалося.')