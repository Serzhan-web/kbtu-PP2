import pygame
import random

pygame.init()
w, h = 600, 400
s = 10
l = 1
sco = 0
snake = [(100, 100), (80, 100), (60, 100)]
d = (20, 0)
def food():
    while True:
        a = (random.randrange(1, w//20 - 1) * 20, random.randrange(1, h//20 - 1) * 20)
        if a not in snake:
            return {'pos': a, 'va': random.randrange(1, 3), 't': pygame.time.get_ticks()}
            
f = food()
screen = pygame.display.set_mode((w, h))
cl = pygame.time.Clock()
k = pygame.font.Font(None, 30)
t = True
while t:
    screen.fill((0, 0, 0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            t = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP and d != (0, 20):
                d = (0, -20)
            elif i.key == pygame.K_DOWN and d != (0, -20):
                d = (0, 20)
            elif i.key == pygame.K_LEFT and d != (20, 0):
                d = (-20, 0)
            elif i.key == pygame.K_RIGHT and d != (-20, 0):
                d = (20, 0)
    head = (snake[0][0] + d[0], snake[0][1] + d[1])
    if head[0] <= 0 or head[0] >= w or head[1] <= 0  or head[1] >= h or head in snake:
        t = False
    if head == f['pos']:
        sco += f['va']
        f = food()
        if sco / 4 > 1:  
            l += 1
            s += 2
            sco %= 4
    else:
        snake.pop()
        
    if pygame.time.get_ticks() - f['t'] > 5000:
        f = food()
    
    snake.insert(0, head)
    for i in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*i, 20, 20))
    pygame.draw.rect(screen, (255, 0, 0), (*f['pos'], 20, 20))
    sc = k.render(str(l), True, (255, 255, 255))
    screen.blit(sc, (10, 10))
    pygame.display.flip()
    cl.tick(s)
pygame.quit()