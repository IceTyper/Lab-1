#ИСУ 466799 Вариант 9, условие "Числа от 5 до 10 и числа от -5 до -10, остальные отбросить", Мусаев Фуад Кананович

def draw_line(space, color, number=0, i=0):
    if number != 0:
        if i in [6, 14]:
            print(f'\x1b[48;5;158;1m{" "*color}\x1b[0m{" "*space}{number}')
        else:
            print(f'\x1b[48;5;158;1m{" "*color}\x1b[0m{" "*space}')
    else:
        print(f'\x1b[48;5;158;1m{" "*color}\x1b[0m')



f = open('sequence.txt')
a = []
for x in f:
    if x[-1].isdigit() == 0:
        a.append(float(x[:-1]))
    else:
        a.append(float(x))

plus510 = 0
minus510 = 0

for i in a:
    if -10 <= i <= -5:
        minus510 += 1
    elif 5 <= i <= 10:
        plus510 += 1


for i in range(1, 20):
    if i in [1, 2, 3, 9, 10, 11, 17, 18, 19]:
        draw_line(0, 2)
    else:
        if i in [4, 5, 6, 7, 8]:
            draw_line(2, 2+minus510, minus510, i)
        else:
            draw_line(2, 2+plus510, plus510, i)


