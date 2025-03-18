import pygame
import os

# Заготовка для кэширования изображений
_image_library = {}
def get_image(path):
    image = _image_library.get(path)
    if image is None:
        # Правильный путь для всех систем
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path).convert_alpha()
        _image_library[path] = image
    return image

def play_a_different_song():
    global _currently_playing_song, _songs
    next_song = random.choice(_songs)
    while next_song == _currently_playing_song: next_song = random.choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()

pygame.init()

_songs = ["LABS/Lab_7/musics/Golden.mp3", "LABS/Lab_7/musics/Let_Me_Love_You.mp3", "LABS/Lab_7/musics/Quem Desiste.mp3", "LABS/Lab_7/musics/En-sulu.mp3", "LABS/Lab_7/musics/Hush.mp3"]
_currently_playing_song = None

screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

is_blue = True  # Начинаем с голубого
x = 30
y = 30

# Загружаем изображение через кэш
image = get_image('Testing/ball.png')

while not done:
    # Выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Условие (Нажатие на клавишу и если эта клавиша "ПРОБЕЛ")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue  # Меняем цвет при пробеле
            play_a_different_song()

    screen.fill((0, 0, 0))  # Очистка экрана

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 10
    if pressed[pygame.K_DOWN]: y += 10
    if pressed[pygame.K_LEFT]: x -= 10
    if pressed[pygame.K_RIGHT]: x += 10
    

    # Выбор цвета по флагу
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)

    # Рисуем Ректангл(Прямоугольник)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    # Рисуем изображение на экран в точке (50, 50)
    screen.blit(image, (50, 50))

    pygame.display.flip()
    clock.tick(60)


    import random