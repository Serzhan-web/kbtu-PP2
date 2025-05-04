'''snake game'''
import pygame
import random
import time

pygame.init()

#screen 
width = 600
heght = 600
screen = pygame.display.set_mode((width,heght))

#constant
CELL = 30 
FOOD_LIFETIME = 5000 #5000 ms = 5s
#FOOD_TIME = pygame.time.set_timer(food.spawn(snake), FOOD_LIFETIME)
FOOD_COLORS = [(255,150,150), (200,255,000),(000,000,255)]

#variables
done = False
score = 0
level = 1
FPS = 5
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()


#background
def draw_grid():
    for i in range(heght//CELL):
        for j in range(width//CELL):
            pygame.draw.rect(screen, (100,100,100), (i * CELL, j * CELL, CELL, CELL))
    
def draw_grid_chess():
    colors = [(255,255,255), (100,100,100)]

    for i in range(heght//CELL):
        for j in range(width//CELL):
            pygame.draw.rect(screen, colors[(i+j)%2],(i*CELL, j*CELL, CELL, CELL))

#variables
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y= y

    
class Snake:
    def __init__(self):
        self.body = [Point(10,11),Point(10,12),Point(10,13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)
        
        #Перемецение змеки на границе
        new_head.x %= width // CELL
        new_head.y %= heght // CELL

        #chek for body and head столкновения
        for segment in self.body:
            if new_head.x == segment.x and new_head.y == segment.y:
                global done
                done = True
                return

        self.body.insert(0,new_head)
        self.body.pop()

    def draw(self):
        '''draw snake'''
        head = self.body[0] #head part
        pygame.draw.rect(screen, (255,0,0), (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]: #adding the tail
            pygame.draw.rect(screen, (0,255,0), (segment.x * CELL, segment.y * CELL, CELL, CELL))
   
    def check_collision(self, food):
        '''collrction food'''
        global score, level, FPS
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            score += food.weight #increase score based on food weight
            self.body.append(Point(head.x, head.y))
            food.spawn(self)
            if score % 4 == 0 and score > 0:
                level += 1
                FPS += 1 #increase speed

class Food:
    def __init__(self):
        self.spawn_time = pygame.time.get_ticks() #food spawn time
        self.spawn(None)

    def spawn(self, snake):
        '''spawn food at random position'''
        self.weight = random.randint(1, 3)
        self.color = FOOD_COLORS[self.weight-1]
        while True:
            new_x = random.randint(0, (width // CELL) - 1)
            new_y = random.randint(0, (heght // CELL) - 1)
            if snake is None or all(segment.x != new_x or segment.y != new_y for segment in snake.body):
                self.pos = Point(new_x, new_y)
                break

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL ,CELL))

    def is_expired(self, FOOD_LIFETIME):
        return pygame.time.get_ticks() - self.spawn_time > FOOD_LIFETIME


food = Food()
snake = Snake()
food.spawn(snake)

#gameplay loop
while not done:
    #gameplay conditions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key  == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            if event.key  == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            if event.key  == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            if event.key  == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    
    #draw background
    draw_grid_chess()

    # Move snake and check collision
    snake.move()
    snake.check_collision(food)

    #check food life time
    if food.is_expired(FOOD_LIFETIME):
        food = Food()

    #draw objects
    snake.draw()
    food.draw()


    #Score and lvl
    score_txt = font.render(f"Score: {score}  Level: {level}", True, (0,0,0))
    screen.blit(score_txt, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)    

pygame.quit()