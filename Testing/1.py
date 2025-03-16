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

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

is_blue = True  # Начинаем с голубого
x = 30
y = 30

# Загружаем изображение через кэш
image = get_image('ball.png')

while not done:
    # Выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Условие (Нажатие на клавишу и если эта клавиша "ПРОБЕЛ")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue  # Меняем цвет при пробеле

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