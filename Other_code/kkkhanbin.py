import pygame as pg
import random

pg.init()

w, h = 600, 400
borders = pg.Rect(50, 50, w - 100, h - 100)
dis = pg.display.set_mode((w, h))
pg.display.set_caption('Snake Game')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pg.time.Clock()
snake_block = 10
snake_speed = 10
font_style = pg.font.SysFont(None, 30)


def Your_score(score, level):
    value = font_style.render(f"Score: {score}  Level: {level}", True, WHITE)
    dis.blit(value, [5, 5])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pg.draw.rect(dis, GREEN, [x[0], x[1], snake_block, snake_block])


def generate_food(snake_list):
    food_x, food_y = None, None
    while food_x is None or [food_x, food_y] in snake_list:
        food_x = round(random.randrange(50, w - 50 - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(50, h - 50 - snake_block) / 10.0) * 10.0
    return food_x, food_y


def gameLoop():
    global snake_speed

    game_over = False
    game_close = False

    x, y = w // 2, h // 2
    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1
    food_x, food_y = generate_food(snake_list)
    food_timer = 0

    flicker = 0

    FOOD_TIMER_LIVE = 100

    score, level = 0, 1

    while not game_over:
        food_timer += 1

        if food_timer >= FOOD_TIMER_LIVE:
            food_x, food_y = generate_food(snake_list)
            food_timer = 0

        while game_close == True:
            dis.fill(BLACK)
            message = font_style.render("Q-Quit | R-Play again", True, RED)
            dis.blit(message, [w / 6, h / 3])
            Your_score(score, level)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pg.K_r:
                        gameLoop()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pg.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pg.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pg.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x >= w - 55 or x < 45 or y >= h - 55 or y < 45:
            game_close = True

        x += x_change
        y += y_change
        dis.fill(BLACK)

        pg.draw.rect(dis, WHITE, borders)

        if food_timer >= FOOD_TIMER_LIVE - 30 and flicker > 3:
            pg.draw.rect(dis, RED, [food_x, food_y, snake_block, snake_block])
        elif food_timer < FOOD_TIMER_LIVE - 30:
            pg.draw.rect(dis, RED, [food_x, food_y, snake_block, snake_block])
        
        flicker = (flicker + 1) % 6

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for z in snake_list[:-1]:
            if z == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        Your_score(score, level)

        pg.display.update()

        if x == food_x and y == food_y:
            food_x, food_y = generate_food(snake_list)

            weight = random.randint(1, 3)

            length_of_snake += weight
            score += weight

            if score % 3 == 0:
                level += 1
                snake_speed += 2

        clock.tick(snake_speed)

    pg.quit()
    quit()

gameLoop()