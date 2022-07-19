import turtle as t
import random

# 사용 할 변수들
n_icon = 11
width = 1200
height = 1200
icon_size = 80
font_size = 20
start_x = width // 2 * -1 + icon_size
start_y = height // 2 - icon_size * 2
ans_index = 0


def draw_line(x1, y1, x2, y2):
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.penup()


def draw_borad():
    x = start_x - (icon_size // 2)
    y = start_y + (icon_size // 2)
    x_step = icon_size
    y_step = icon_size + font_size
    lines = 100 // n_icon

    # 세로 선
    for i in range(x, x + x_step * (n_icon+1), x_step):
        draw_line(i, y, i, y - y_step * lines)

    # 가로 선
    for i in range(y, y-y_step*(lines+1), -1*y_step):
        draw_line(x, i, x + icon_size * n_icon, i)


def start_game():
    t.reset()
    t.hideturtle()
    t.penup()

    global ans_index
    ans_index = random.randint(0, n_icon-1)
    lines = 100 // n_icon

    for line in range(lines):
        posX = start_x
        posY = start_y - line * (icon_size + font_size)

        for i in range(n_icon):
            total_index = line * n_icon + i + 1
            if total_index % 9 == 0:
                draw_ans(posX, posY, total_index)
            else:
                rand_stamp(posX, posY, total_index)
            posX += icon_size

    draw_borad()


def show_ans():
    t.reset()
    t.hideturtle()
    t.shape("icon/icon" + str(ans_index) + ".gif")
    t.stamp()


def rand_stamp(posX, posY, num):
    t.goto(posX, posY)
    rand_icon = random.randint(0, n_icon-1)
    t.shape("icon/icon" + str(rand_icon)+".gif")
    t.stamp()
    t.goto(posX, posY - (icon_size/2) - font_size)
    t.write(num, move=False, align="center", font=("Arial", font_size))

def draw_ans(posX, posY, num):
    t.goto(posX, posY)
    t.shape("icon/icon" + str(ans_index)+".gif")
    t.stamp()
    t.goto(posX, posY - (icon_size / 2) - font_size)
    t.write(num, move=False, align="center", font=("Arial", font_size))


if __name__ == '__main__':
    t.setup(width=width, height=height, startx=0, starty=0)
    t.hideturtle()

    # 아이콘 등록
    for i in range(n_icon):
        t.register_shape("icon/icon" + str(i) + ".gif")
    t.shape("icon/icon2.gif")


    t.onkey(start_game, "space")
    t.listen()

    t.onkey(show_ans, "a")
    t.listen()

    t.done()
