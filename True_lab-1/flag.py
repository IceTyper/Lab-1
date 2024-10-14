#Номер ИСУ 466799, поэтому вариант 9, а там флаг Финляндии ;) Мусаев Фуад Кананович
Blue = 62
White = 255
ldown = 6       #ширина цветов
length = 30     #длина флага



for i in range(6):
    if i not in [2, 3]:     #Если не настала полностью синяя часть флага
        print(f'\x1b[48;5;{White};1m{" "*ldown}\x1b[48;5; \
        {Blue};1m{" "*ldown}\x1b[48;5;{White};1m{" "*(length-ldown*2)}\x1b[0m')
    else:
        print(f'\x1b[48;5;{Blue};1m{" "*length}\x1b[0m')



