import pygame

pygame.init()

pygame.mixer.music.load('LABS/Lab_7/musics/En-sulu.mp3')
pygame.mixer.music.play(0)

screen = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()
done = False

# Загружаем одну и ту же картинку ДВАЖДЫ
# Предположим, 'ball.png' — это PNG с прозрачным фоном
image_raw = pygame.image.load('ball.png')  # без convert
image_alpha = pygame.image.load('ball.png').convert_alpha()  # с прозрачностью

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((30, 30, 30))  # тёмный фон

    # Отрисуем обе картинки рядом
    screen.blit(image_raw, (50, 100))       # Слева — БЕЗ convert_alpha()
    screen.blit(image_alpha, (250, 100))    # Справа — С convert_alpha()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
