# name = input('Введіть своє ім\'я: ')
#
# print('Привіт, ' + name + '!')
# print('Привіт, ', name, '!', sep='')
# print(f'Привіт, {name}!')
# print('Привіт, {}!'.format(name))

'''

    Написати програму, яка запитує у користувача 2 числа і виводить
    їх суму. Приклад:

    Введіть перше число: 4
    Введіть друге число: 3

    4 + 3 = 7

'''

a = int(input('Введіть перше число: '))
b = int(input('Введіть друге число: '))

sum = a + b

print(f'{a} + {b} = {sum}')

'''

    Зробити функцію draw_square, яка має малювати квадрати. Викликати
    цю функцію в програмі.
    
    Переписати функцію draw_square.
    
    Змінити функцію draw_rectangle таким чином, щоб у параметри цієї функції
    можна було вказувати розміри і колір майбутнього прямокутника.

'''

import turtle as t

# СЮДИ вставити функцію draw_square

t.reset()
screen = t.Screen()

# СЮДИ вставити виклик цієї функції

screen.exitonclick()
























