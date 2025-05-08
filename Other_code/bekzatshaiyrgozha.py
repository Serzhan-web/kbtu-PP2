import pygame  
import sys  # Импортируем модуль sys для взаимодействия с системой
import copy  # Импортируем модуль copy для создания копий объектов
import random  # Импортируем модуль random для работы с случайными числами
import time  # Импортируем модуль time для работы со временем

pygame.init()  # Инициализируем Pygame

# Устанавливаем параметры игры
scale = 15  # Масштаб объектов
score = 0  # Счет игрока
level = 0  # Уровень игры
SPEED = 10  # Скорость движения змейки

food_x = 10  # Координата x для еды
food_y = 10  # Координата y для еды

# Создаем окно для отображения игры
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")  # Устанавливаем заголовок окна
clock = pygame.time.Clock()  # Создаем объект Clock для управления временем в игре

# Определяем цвета в формате RGB
background_top = (0, 0, 50)  # Цвет верхнего уровня фона
background_bottom = (0, 0, 0)  # Цвет нижнего уровня фона
snake_colour = (255, 137, 0)  # Цвет змейки
food_colour = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))  # Цвет еды (случайный)
snake_head = (255, 247, 0)  # Цвет головы змейки
font_colour = (255, 255, 255)  # Цвет шрифта
defeat_colour = (255, 0, 0)  # Цвет при проигрыше

# Определяем класс Snake для создания объекта змейки
class Snake:
    def __init__(self, x_start, y_start):
        self.x = x_start  # Координата x начального положения змейки
        self.y = y_start  # Координата y начального положения змейки
        self.w = 15  # Ширина змейки
        self.h = 15  # Высота змейки
        self.x_dir = 1  # Направление движения по оси x (1 - вправо, -1 - влево)
        self.y_dir = 0  # Направление движения по оси y (1 - вниз, -1 - вверх)
        self.history = [[self.x, self.y]]  # История перемещений змейки
        self.length = 1  # Длина змейки

    # Метод для сброса состояния змейки
    def reset(self):
        self.x = 500 / 2 - scale  # Возвращаем змейку в центр по оси x
        self.y = 500 / 2 - scale  # Возвращаем змейку в центр по оси y
        self.w = 15  # Сбрасываем ширину змейки
        self.h = 15  # Сбрасываем высоту змейки
        self.x_dir = 1  # Сбрасываем направление по оси x
        self.y_dir = 0  # Сбрасываем направление по оси y
        self.history = [[self.x, self.y]]  # Сбрасываем историю перемещений
        self.length = 1  # Сбрасываем длину змейки

    # Метод для отображения змейки на экране
    def show(self):
        for i in range(self.length):
            if not i == 0:
                pygame.draw.rect(display, snake_colour, (self.history[i][0], self.history[i][1], self.w, self.h))
            else:
                pygame.draw.rect(display, snake_head, (self.history[i][0], self.history[i][1], self.w, self.h))

    # Метод для проверки съедения еды
    def check_eaten(self):
        if abs(self.history[0][0] - food_x) < scale and abs(self.history[0][1] - food_y) < scale:
            return True

    # Метод для проверки достижения нового уровня
    def check_level(self):
        global level
        if self.length % 5 == 0:
            return True

    # Метод для увеличения длины змейки
    def grow(self):
        self.length += 1
        self.history.append(self.history[self.length - 2])

    # Метод для проверки столкновения с собственным хвостом
    def death(self):
        i = self.length - 1
        while i > 0:
            if abs(self.history[0][0] - self.history[i][0]) < self.w and abs(self.history[0][1] - self.history[i][1]) < self.h and self.length > 2:
                return True
            i -= 1

    # Метод для обновления координат змейки
    def update(self):
        i = self.length - 1
        while i > 0:
            self.history[i] = copy.deepcopy(self.history[i - 1])
            i -= 1
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale

# Определяем класс Food для создания объекта еды
class Food:
    # Метод для установки новой позиции еды на экране
    def new_location(self):
        global food_x, food_y
        food_x = random.randrange(1, int(500 / scale) - 1) * scale
        food_y = random.randrange(1, int(500 / scale) - 1) * scale

    # Метод для отображения еды на экране
    def show(self):
        pygame.draw.rect(display, food_colour, (food_x, food_y, scale))


class Food:
    def new_location(self):
        global food_x, food_y
        food_x = random.randrange(1, int(500 / scale) - 1) * scale
        food_y = random.randrange(1, int(500 / scale) - 1) * scale

    def show(self):
        pygame.draw.rect(display, food_colour, (food_x, food_y, scale, scale))

# Функция для отображения счета игрока
def show_score():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: " + str(score), True, font_colour)
    display.blit(text, (scale, scale))

# Функция для отображения уровня игры
def show_level():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Level: " + str(level), True, font_colour)
    display.blit(text, (90 - scale, scale))

# Основной цикл игры
def gameLoop():
    global score
    global level
    global SPEED

    snake = Snake(500 / 2, 500 / 2)  # Создаем объект змейки
    food = Food()  # Создаем объект еды
    food.new_location()  # Устанавливаем начальное положение еды

    while True:  # Бесконечный цикл игры
        for event in pygame.event.get():  # Обработка событий
            if event.type == pygame.QUIT:  # Если пользователь закрывает окно
                pygame.quit()  # Завершаем работу Pygame
                sys.exit()  # Завершаем выполнение программы
            if event.type == pygame.KEYDOWN:  # Если пользователь нажимает клавишу
                if event.key == pygame.K_q:  # Если нажата клавиша Q
                    pygame.quit()  # Завершаем работу Pygame
                    sys.exit()  # Завершаем выполнение программы
                if snake.y_dir == 0:  # Если змейка движется по горизонтали
                    if event.key == pygame.K_UP:  # Если нажата клавиша Вверх
                        snake.x_dir = 0  # Устанавливаем направление движения по горизонтали в 0
                        snake.y_dir = -1  # Устанавливаем направление движения по вертикали вверх
                    if event.key == pygame.K_DOWN:  # Если нажата клавиша Вниз
                        snake.x_dir = 0  # Устанавливаем направление движения по горизонтали в 0
                        snake.y_dir = 1  # Устанавливаем направление движения по вертикали вниз

                if snake.x_dir == 0:  # Если змейка движется по вертикали
                    if event.key == pygame.K_LEFT:  # Если нажата клавиша Влево
                        snake.x_dir = -1  # Устанавливаем направление движения по горизонтали влево
                        snake.y_dir = 0  # Устанавливаем направление движения по вертикали в 0
                    if event.key == pygame.K_RIGHT:  # Если нажата клавиша Вправо
                        snake.x_dir = 1  # Устанавливаем направление движения по горизонтали вправо
                        snake.y_dir = 0  # Устанавливаем направление движения по вертикали в 0

        # Заполнение фона градиентом
        for y in range(500):
            color = (
                background_top[0] + (background_bottom[0] - background_top[0]) * y / 500,
                background_top[1] + (background_bottom[1] - background_top[1]) * y / 500,
                background_top[2] + (background_bottom[2] - background_top[2]) * y / 500
            )
            pygame.draw.line(display, color, (0, y), (500, y))

        snake.show()  # Отображаем змейку на экране
        snake.update()  # Обновляем положение змейки
        food.show()  # Отображаем еду на экране
        show_score()  # Отображаем счет игрока
        show_level()  # Отображаем уровень игры

        if snake.check_eaten():  # Если змейка съела еду
            food.new_location()  # Устанавливаем новую позицию еды
            score += random.randint(1, 5)  # Увеличиваем счет на случайное значение
            snake.grow()  # Увеличиваем длину змейки

        if snake.check_level():  # Если достигнут новый уровень
            food.new_location()  # Устанавливаем новую позицию еды
            level += 1  # Увеличиваем уровень
            SPEED += 1  # Увеличиваем скорость змейки
            snake.grow()  # Увеличиваем длину змейки

        if snake.death():  # Если змейка столкнулась с собственным хвостом
            score = 0  # Сбрасываем счет
            level = 0  # Сбрасываем уровень
            font = pygame.font.SysFont(None, 100)  # Устанавливаем шрифт для отображения текста
            text = font.render("Game Over!", True, defeat_colour)  # Создаем текст "Game Over!"
            display.blit(text, (50, 200))  # Отображаем текст на экране
            pygame.display.update()  # Обновляем экран
            time.sleep(3)  # Задержка перед сбросом игры
            snake.reset()  # Сбрасываем состояние змейки

        if snake.history[0][0] > 500:  # Если змейка вышла за пределы правой границы
            snake.history[0][0] = 0  # Перемещаем змейку на левую границу

        if snake.history[0][0] < 0:  # Если змейка вышла за пределы левой границы
            snake.history[0][0] = 500  # Перемещаем змейку на правую границу
            
        if snake.history[0][1] > 500:
            snake.history[0][1] = 0
        if snake.history[0][1] < 0:
            snake.history[0][1] = 500

        pygame.display.update()
        clock.tick(SPEED)

gameLoop()