import pygame

pygame.init()

SONG_END = pygame.USEREVENT + 1  # 1️⃣ Создание пользовательского события

pygame.mixer.music.set_endevent(SONG_END)  # 2️⃣ Связываем событие с окончанием песни
pygame.mixer.music.load('LABS/Lab_7/musics/Golden.mp3')
pygame.mixer.music.play(0)

screen = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()
done = False

# Загружаем одну и ту же картинку ДВАЖДЫ
# Предположим, 'ball.png' — это PNG с прозрачным фоном
image_raw = pygame.image.load('Testing/ball.png')  # без convert
image_alpha = pygame.image.load('Testing/ball.png').convert_alpha()  # с прозрачностью

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == SONG_END:
            print("the song ended!")

    screen.fill((30, 30, 30))  # тёмный фон

    # Отрисуем обе картинки рядом
    screen.blit(image_raw, (50, 100))       # Слева — БЕЗ convert_alpha()
    screen.blit(image_alpha, (250, 100))    # Справа — С convert_alpha()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
