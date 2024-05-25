from colorama import Fore, Back, Style

def header(title, width):
    print(f'{Fore.RED}{f" {title} ":─^{width}}{Style.RESET_ALL}')


rows = 20
columns = 20
cell_size = len(str(rows * columns)) + 1


header("Таблиця множення", (columns + 1) * cell_size)
for y in range(rows + 1):
    for x in range(columns + 1):
        if x == 0 and y == 0:
            print(f'{Back.YELLOW}{Fore.LIGHTWHITE_EX}', end='')
            cell = 'X'
        elif x == 0 or y == 0:
            print(f'{Back.YELLOW}{Fore.LIGHTWHITE_EX}', end='')
            cell = x + y
        else:
            if x == y:
                print(f'{Back.RESET}{Fore.LIGHTRED_EX}', end='')
            else:
                print(f'{Back.RESET}{Fore.LIGHTWHITE_EX}', end='')
            cell = x * y
        print(f'{cell:^{cell_size}}', end='')
    print(Style.RESET_ALL)