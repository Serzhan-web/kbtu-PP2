import pygame
import random

pygame.init()

# Константы
WINDOW_SIZE = 500  # Размер окна
BLOCK_SIZE = 20  # Размер блока
GRID_SIZE = WINDOW_SIZE // BLOCK_SIZE  # Размер сетки
INFO_PANEL_WIDTH = 150  # Ширина информационной панели
FPS = 6  # Количество кадров в секунду

# Цвета
WHITE = (255, 255, 255)  # Белый
GREEN = (0, 150, 0)  # Зеленый
RED = (150, 0, 0)  # Красный
BLUE = (0, 0, 200)  # Синий
BLACK = (0, 0, 0)  # Черный

# Экран и таймер
screen = pygame.display.set_mode((WINDOW_SIZE + INFO_PANEL_WIDTH, WINDOW_SIZE))  # Создание окна игры
clock = pygame.time.Clock()  # Таймер

# Классы
class Snake:
  def __init__(self):
    self.body = [[10, 10]]  # Начальное положение змейки
    self.dx, self.dy = 1, 0  # Направление движения змейки
    self.score = 0  # Очки игрока
    self.level = 1  # Уровень игры

  def move(self):
    head = [self.body[0][0] + self.dx, self.body[0][1] + self.dy]  # Новая позиция головы змейки

    # Проверка выхода за границы
    if head[0] < 0 or head[0] >= GRID_SIZE or head[1] < 0 or head[1] >= GRID_SIZE:
      return False

    # Проверка столкновения с самим собой
    if head in self.body:
      return False

    self.body.insert(0, head)

    # Проверка, съела ли змейка еду
    if head == food.pos:
      self.score += food.weight  # Увеличение очков в зависимости от веса еды
      food.respawn(self.body)

      # Увеличение уровня каждые 4 очка
      if self.score % 4 == 0:
        self.level += 1
        global FPS
        FPS += 2
    else:
      self.body.pop()
    return True

  def draw(self):
    for segment in self.body:
      pygame.draw.rect(
        screen, GREEN, (segment[0] * BLOCK_SIZE, segment[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))  # Отрисовка сегмента змейки


class Food:
  def __init__(self):
    self.respawn()  # Создание новой еды
    self.timer = 0  # Таймер

  def respawn(self, snake_body=[]):
    while True:
      self.pos = [random.randint(0, GRID_SIZE - 1),  # Позиция еды
            random.randint(0, GRID_SIZE - 1)]
      if self.pos not in snake_body:
        break
    self.weight = random.randint(1, 3)  # Вес еды
    self.timer = 50  # Таймер на 50 циклов

  def update_timer(self):
    if self.timer > 0:
      self.timer -= 1  # Уменьшение таймера
    else:
      self.respawn(snake.body)  # Перемещение еды при окончании таймера

  def draw(self):
    pygame.draw.rect(
      screen, BLUE, (self.pos[0] * BLOCK_SIZE, self.pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))  # Отрисовка еды


# Инициализация
snake = Snake()
food = Food()
running = True

# Игровой цикл
while running:
  screen.fill(WHITE)  # Очистка экрана

  for event in pygame.event.get():
    if event.type == pygame.QUIT:  # Выход из игры
      running = False
    if event.type == pygame.KEYDOWN:  # Обработка ввода клавиатуры
      if event.key == pygame.K_RIGHT and snake.dx == 0:  # Движение вправо
        snake.dx, snake.dy = 1, 0
      if event.key == pygame.K_LEFT and snake.dx == 0:  # Движение влево
        snake.dx, snake.dy = -1, 0
      if event.key == pygame.K_UP and snake.dy == 0:  # Движение вверх
        snake.dx, snake.dy = 0, -1
      if event.key == pygame.K_DOWN and snake.dy == 0:  # Движение вниз
        snake.dx, snake.dy = 0, 1

  running = snake.move()  # Движение змейки
  food.update_timer()  # Обновление таймера еды

  # Отрисовка сетки
  for x in range(0, WINDOW_SIZE, BLOCK_SIZE):
    for y in range(0, WINDOW_SIZE, BLOCK_SIZE):
      pygame.draw.rect(screen, BLACK, (x, y, BLOCK_SIZE, BLOCK_SIZE), 1)  # Отрисовка клеток сетки

  snake.draw()  # Отрисовка змейки
  food.draw()  # Отрисовка еды

  # Информационная панель
  pygame.draw.rect(screen, WHITE, (WINDOW_SIZE, 0,
           INFO_PANEL_WIDTH, WINDOW_SIZE))  # Область панели
  font = pygame.font.Font(None, 30)
  score_text = font.render(f'Score: {snake.score}', True, RED)  # Текст очков
  level_text = font.render(f'Level: {snake.level}', True, RED)  # Текст уровня
  screen.blit(score_text, (WINDOW_SIZE + 20, 20))
  screen.blit(level_text, (WINDOW_SIZE + 20, 50))

  pygame.display.update()  # Обновление экрана
  clock.tick(FPS)  # Задержка в зависимости от FPS

pygame.quit()  # Завершение игры