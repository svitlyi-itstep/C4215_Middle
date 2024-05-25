import random

health = 100
mana = 300
speed = 200

print(f'Health:\t{health}')
print(f'Mana:\t{mana}')
print(f'Speed:\t{speed}')

print('\n')

for i in range(10):
    a = random.randint(1, 999)
    b = random.randint(1, 999)
    print(f'{a}\t* {b}\t= {a * b}')

print('\n')