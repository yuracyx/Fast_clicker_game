import time

import pygame as pg
pg.init()
import random

class Area():
    def __init__(self, x = 0, y = 0, width = 10, height = 10, color = False):
        self.rect = pg.Rect(x, y, width, height)
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pg.draw.rect(mw, self.fill_color, self.rect)
    def outline(self, frame_color, thickness):
        pg.draw.rect(mw, frame_color, self.rect, thickness)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x,y)

class Lable(Area):
    def set_text(self, text, size, text_color):
        self.image = pg.font.SysFont('verdana', size).render(text, True, text_color)
    def draw(self, shift_x, shift_y):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


# кортежи: цвета и тп
resolution = (500, 500)
color_rect = (100, 0, 255)
yellow_color = (255, 255, 0)
black_color =(0, 0, 0)
back_color = (255, 239, 213)
blue_color = (0, 0, 255)
green_color = (0, 255, 00)
red_color = (139, 0, 0)

# основное для окна
mw = pg.display.set_mode(resolution)
mw.fill(back_color)

# переменные для основного цикла
running_game = True
clock = pg.time.Clock()


cards_list = list() # список с карточками
x = 70
num_cards = 4

for i in range(num_cards):
    card = Lable(x, 200, 70, 90, yellow_color)
    card.outline(blue_color, 20)
    card.set_text('Click', 22, black_color)
    cards_list.append(card)
    x += 100 # промежуток между картами

count = 0

timer = Lable(320, 30, 50, 50, back_color)
timer.set_text('Время:', 22, black_color)
timer.draw(20,20)

time_digits = Lable(430, 50, 50, 50, back_color)
time_digits.set_text('0', 22, black_color)
time_digits.draw(0,0)

score = Lable(50, 50, 50, 50, back_color)
score.set_text('Счет:', 22, black_color)
score.draw(0, 0)

points = 0
score_points = Lable(130, 50, 50, 50, back_color)
score_points.set_text(str(points), 22, black_color)
score_points.draw(0, 0)


start_time = time.time()
cur_time = start_time
# основной цикл
while running_game == True:
    if count == 0:
        count = 20
        rand_num = random.randint(1, num_cards)
        for i in range(num_cards):
            cards_list[i].color(yellow_color)
            if i+1 == rand_num:
                cards_list[i].draw(10, 30)
            else:
                cards_list[i].fill()
    else:
        count -= 1
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(num_cards):
                if cards_list[i].collidepoint(x, y):
                    if i + 1 == rand_num:
                        cards_list[i].color(green_color)
                        points += 1
                    else:
                        cards_list[i].color(red_color)
                        points -= 1
                        if points < 0:
                            points = 0
                    cards_list[i].fill()
                    score_points.set_text(str(points), 22,black_color)
                    score_points.draw(0,0)

    stop_time = time.time()
    new_time = time.time()

    if new_time - cur_time >= 1:
        time_digits.set_text(str(int(new_time - cur_time)), 22, black_color)
        time_digits.draw(0,0)
        new_time = cur_time

    if points >= 5:
        mw_win = Lable(0, 0, 500, 500, green_color)
        mw_win.set_text('ПОБЕДА!!!', 50, black_color)
        mw_win.draw(120,200)
        pg.display.update()
        time.sleep(3)
        running_game = False

    if stop_time - start_time >= 11:
        mw_win = Lable(0, 0, 500, 500, red_color)
        mw_win.set_text('ВРЕМЯ ВЫШЛО!!!', 40, black_color)
        mw_win.draw(80, 200)
        pg.display.update()
        time.sleep(3)
        running_game = False

    pg.display.update()
    clock.tick(40)

pg.display.update()
