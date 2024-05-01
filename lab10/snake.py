import psycopg2
import pygame
import sys
import copy
import random
import time
import psycopg2
from color_palette import *
conn = psycopg2.connect(host="localhost", dbname="lab10", user="postgres",
                        password="Almaty250505", port=5433)   
 
cur = conn.cursor()
 
conn.set_session(autocommit=True)
name = input("Enter your username: ")


cur.execute("""
    SELECT level, score FROM snake WHERE username = %s ORDER BY score DESC LIMIT 1
""", (name,))

result = cur.fetchone()
if result:
    level, high_score = result
    print(f"Welcome back, {name}! Your current level is {level} and your high score is {high_score}.")
else:
    level = 1
    high_score = 0
    print(f"Welcome, {name}! You are starting at level 1.")


pygame.init()


WIDTH = 600
HEIGHT = 600
CELL = 30
FPS = 5 + level - 1  


screen = pygame.display.set_mode((HEIGHT, WIDTH))

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))

class Food:
    def __init__(self, snake):
        self.snake = snake
        self.pos = self.generate_position()
        self.timer_start = time.time()  
        self.timer_duration = random.randint(3, 6)  
        self.score = random.choice([1, 2, 5])  

    def generate_position(self):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            if Point(x, y) not in  self.snake.body:
                return Point(x, y)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def is_expired(self):
        return time.time() - self.timer_start > self.timer_duration

snake = Snake()
food = None

score = 0
is_paused = False

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Pause the game with 'P'
                is_paused = not is_paused
                if is_paused:
                    print("Game Paused")
                   
                    cur.execute("""
                        INSERT INTO snake_scores (username, level, score)
                        VALUES (%s, %s, %s)
                    """, (name, level, score))
                    conn.commit()
                else:
                    print("Game Resumed")

            if not is_paused:
                if event.key == pygame.K_RIGHT:
                    snake.dx = 1
                    snake.dy = 0
                elif event.key == pygame.K_LEFT:
                    snake.dx = -1
                    snake.dy = 0
                elif event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 1
                elif event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -1

    if is_paused:
        continue

    head = snake.body[0]
    if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
        print("Game Over!")
        done = True

    draw_grid_chess()

    snake.move()

    if food is None or food.is_expired():
        food = Food(snake)

    snake.check_collision(food)

    if snake.body[0].x == food.pos.x and snake.body[0].y == food.pos.y:
        score += food.score  
        food = Food(snake)  
        if score % 3 == 0:
            FPS += 1
            level += 1  

    snake.draw()
    food.draw()

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 100, 0))
    level_text = font.render(f"Level: {level}", True, (255, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))

    pygame.display.flip()
    clock.tick(FPS)


cur.execute("""
    INSERT INTO snake (username, level, score)
    VALUES (%s, %s, %s)
""", (name, level, score))

conn.commit()  
cur.execute("""DELETE FROM snake
           WHERE score = 3
""")
conn.commit()
cur.close()
conn.close()

pygame.quit()