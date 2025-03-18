import pygame
import os

# Словарь для хранения уже загруженных картинок
_image_library = {}

def get_image(file_name):
    # Приводим путь к правильному виду под операционку (Windows/Linux)
    full_path = os.path.join('images', file_name)

    # Если уже загружено → вернуть
    if full_path in _image_library:
        return _image_library[full_path]
    
    # Иначе загрузить и сохранить в кэш
    image = pygame.image.load(full_path).convert_alpha()
    _image_library[full_path] = image
    return image

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

is_blue = True  # Начинаем с голубого
x = 30
y = 30

# Загружаем изображение → создаём surface
image = pygame.image.load('Testing/ball.png')

while not done:
    # Выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Условие (Нажатие на клавишу и эта клавиша "ПРОБЕЛ")
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
    pygame.draw.circle(screen, color, (x, y), 30, 10)

    # Рисуем изображение на экран в точке (50, 50)
    screen.blit(image, (50, 50))

    pygame.display.flip()
    clock.tick(60)