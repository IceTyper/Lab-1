#ИСУ 466799 Вариант 9, функция y = x/2, Мусаев Фуад Кананович

def draw_line(space, color, secspace=0, line=0):
    if secspace >= 0:
        secspace = secspace*4-2
        print(f'{" "*space}\x1b[48;5;255;1m{" "*color}\x1b[0m{" "*secspace}\x1b[48;5;255;1m{" "*line}\x1b[0m')
    else:
        secspace = abs(secspace)
        space = secspace*4-2
        secspace = 42 - (secspace*4+2)
        print(f'{" "*secspace}\x1b[48;5;255;1m{" "*line}\x1b[0m{" "*space}\x1b[48;5;255;1m{" "*color}\x1b[0m')




for i in range(10, -11, -1):
    if i == 0:
        draw_line(0, 86)
    else:
        draw_line(42, 2, i, 4)


