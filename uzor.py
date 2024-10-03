#ИСУ 466799 Вариант 9, узор i, Мусаев Фуад Кананович




def draw_line(space, color):
    print(f'{" "*space}\x1b[48;5;255;1m{" "*color}\x1b[0m{" "*(space*2)}\x1b[48;5;255;1m{" "*color}\x1b[0m')


width = 54
space = (width-4)//2
color = 4
circler = [16, 4, 8, 4, 4, 0, 4, 4, 0, 0, 0, 4, 0, 0]
for i in range(len(circler)):
    draw_line(space, color)
    space -= circler[i]//2
    color += circler[i]

for i in range(len(circler)-1, -1, -1):
    draw_line(space, color)
    space += circler[i]//2
    color -= circler[i]



