#ИСУ 466799 Вариант 9б узор i




def draw_line(space, color):
    print(f'{" "*space}\x1b[48;5;255;1m{" "*color}\x1b[0m{" "*(space*2)}\x1b[48;5;255;1m{" "*color}\x1b[0m')


width = 50
space = (width-2)//2
color = 1
circler = 3
while color < width:
    draw_line(space, color)
    space -= 2
    color += 4

space, color = 1, width-3

while color > 1:
    draw_line(space, color)
    space += 2
    color -= 4



