import time
#Номер ИСУ 466799, поэтому вариант 9, а там флаг Финляндии ;)



Blue = 62
White = 255
length = len('                              ')
ldown = 6


for i in range(6):
    if i not in [2, 3]:
        print(f'\x1b[48;5;{White};1m{" "*ldown}\x1b[48;5;{Blue};1m{" "*ldown}\x1b[48;5;{White};1m{" "*(length-ldown*2)}\x1b[0m')
    else:
        print(f'\x1b[48;5;{Blue};1m{" "*length}\x1b[0m')



