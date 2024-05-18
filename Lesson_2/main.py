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
    if player_choice == bot_choice:
        return 'd' #draw
    elif player_choice == 'к' and bot_choice == 'н':
        return 'p' #player
    elif player_choice == 'к' and bot_choice == 'п':
        return 'b' #bot
    elif player_choice == 'н' and bot_choice == 'п':
        return 'p'
    elif player_choice == 'н' and bot_choice == 'к':
        return 'b'
    elif player_choice == 'п' and bot_choice == 'к':
        return 'p'
    elif player_choice == 'п' and bot_choice == 'н':
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