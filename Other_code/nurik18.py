import pygame
import sys
import random

# initializi
pygame.init()

# variabl
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# rgbs
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# scren
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# font
font = pygame.font.SysFont("Verdana", 20)

# points scores
score = 0
level = 1
level_goal = 5
speed = 10

# walls
walls = [(0, y) for y in range(GRID_HEIGHT)] + \
        [(GRID_WIDTH - 1, y) for y in range(GRID_HEIGHT)] + \
        [(x, 0) for x in range(GRID_WIDTH)] + \
        [(x, GRID_HEIGHT - 1) for x in range(GRID_WIDTH)]


# class snake
class Snake:
    def __init__(self):
        self.body = [(5, 5)]  # Начальная позиция
        self.direction = (1, 0)  # Направление змейки (вправо)

    def move(self):
        head = self.body[-1]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.append(new_head)
        self.body.pop(0)  # Удаляем хвост

    def grow(self):
        self.body.insert(0, self.body[0])  # Копируем хвост, чтобы змейка росла

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))


# food generatin
def random_food_position(snake):
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake.body and pos not in walls:
            return pos


# objects
snake = Snake()
food = random_food_position(snake)

# time
clock = pygame.time.Clock()


# game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # movement 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake.direction != (0, 1):
        snake.direction = (0, -1)
    if keys[pygame.K_DOWN] and snake.direction != (0, -1):
        snake.direction = (0, 1)
    if keys[pygame.K_LEFT] and snake.direction != (1, 0):
        snake.direction = (-1, 0)
    if keys[pygame.K_RIGHT] and snake.direction != (-1, 0):
        snake.direction = (1, 0)

    snake.move()

    # collision check
    head_x, head_y = snake.body[-1]
    if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
        pygame.quit()
        sys.exit()

    # food check
    if snake.body[-1] == food:
        snake.grow()
        score += 1
        food = random_food_position(snake)

        # levelup
        if score % level_goal == 0:
            level += 1
            speed += 1

    # drawing on screen
    screen.fill(BLACK)
    snake.draw()
    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # scores points
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(level_text, (WIDTH - 100, 10))

    # walls draw
    pygame.draw.rect(screen, (100, 100, 100), (0, 0, WIDTH, HEIGHT), 4)

    # obnova ekrana
    pygame.display.flip()

    # game speed
    clock.tick(speed)