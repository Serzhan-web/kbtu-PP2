import pygame

pygame.init()
WIDTH = 750
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
radius = 25
x = radius
y = radius
speed = 20
color = (255, 0, 0)
keys = [(pygame.K_UP, (0, -1)), (pygame.K_DOWN, (0, 1)), (pygame.K_LEFT, (-1, 0)), (pygame.K_RIGHT, (1, 0))]
clock = pygame.time.Clock()
pygame.display.set_caption("Circle")

def leaves_screen(x, y):
	return x - radius < 0 or x + radius > WIDTH or y - radius < 0 or y + radius > HEIGHT

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	pressed = pygame.key.get_pressed()
	for key in keys:
		if pressed[key[0]]:
			x += key[1][0] * speed
			y += key[1][1] * speed
			if leaves_screen(x, y):
				x -= key[1][0] * speed
				y -= key[1][1] * speed

	screen.fill((255, 255, 255))
	pygame.draw.circle(screen, color, (x, y), radius)
	
	pygame.display.flip()
	clock.tick(60)