import pygame
import sys
import random
import psycopg2
from tabulate import tabulate 

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Инициализация
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_speed = [10, 0]
food = {'pos': [0, 0], 'weight': 1, 'spawn_time': 0}
food_spawn = True
score = 0
level = 1
speed_increase = 10
food_counter = 0
paused = False

command = ''
start = True
back = False

fps = pygame.time.Clock()

# --- DB Connection ---
DB_PARAMS = {
    'dbname': 'lab10',
    'user': 'postgres',
    'password': 'Almaty250505',
    'host': 'localhost',
    'port': '5432'
}

def get_user_id(username):
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cur.fetchone()
    if result:
        user_id = result[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
    cur.close()
    conn.close()
    return user_id


def insert_score(user_id, score, level):
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)",
        (user_id, score, level)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_user_scores(user_id):
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute(
        "SELECT score, level, created_at FROM user_scores WHERE user_id = %s ORDER BY created_at DESC",
        (user_id,)
    )
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def delete_user_scores_for_user():
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    global command
    command = ''
    username_var = str(input('Type username which you want to delete their score: '))
    user_id = get_user_id(username_var)
    cur.execute("DELETE FROM user_scores WHERE user_id = %s", (user_id,))
    conn.commit()

def check_collision(pos):
    if pos[0] < 0 or pos[0] >= SCREEN_WIDTH or pos[1] < 0 or pos[1] >= SCREEN_HEIGHT:
        return True
    if pos in snake_pos[1:]:
        return True
    return False

def get_random_food():
    global food_counter
    while True:
        pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
        if pos not in snake_pos:
            weight = 2 if food_counter >= 2 else 1
            food_counter = 0 if weight == 2 else food_counter + 1
            return {'pos': pos, 'weight': weight, 'spawn_time': pygame.time.get_ticks()}

check = True
while check:
    if start == True or back == True:
        start = False
        print("""
        List of the commands:
        1. Type "d" or "D" in order to DELETE data from the table.
        2. Type "f" or "F" in order to close the program.
        3. Type "s" or "S" in order to see the values in the table.
        """)
        command = str(input())

        if command == "d" or command == "D":
            delete_user_scores_for_user()
            back_com = str(input('Type "back" in order to return to the list of the commands: '))
            if back_com == "back":
                back = True
                
        if command == "s" or command == "S":
            back = False
            command = ''
            conn = psycopg2.connect(**DB_PARAMS)
            cur = conn.cursor()
            cur.execute("SELECT * from user_scores;")
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "User_score", "Level", "Created_at"], tablefmt='fancy_grid'))
            back_com = str(input('Type "back" in order to return to the list of the commands: '))
            if back_com == "back":
                back = True
        #finish
        if command == "f" or command == "F":
            command = ''
            check = False

# --- Ввод имени и загрузка ---
player_name = input("Enter your username: ").strip()
user_id = get_user_id(player_name)
previous_scores = get_user_scores(user_id)

if previous_scores:
    print("\nPrevious Scores:")
    for s, lvl, time in previous_scores[:5]:
        print(f"Score: {s}, Level: {lvl}, Date: {time.strftime('%Y-%m-%d %H:%M:%S')}")

# --- Game Loop ---
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                insert_score(user_id, score, level)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_speed[1] == 0:
                    snake_speed = [0, -10]
                elif event.key == pygame.K_DOWN and snake_speed[1] == 0:
                    snake_speed = [0, 10]
                elif event.key == pygame.K_LEFT and snake_speed[0] == 0:
                    snake_speed = [-10, 0]
                elif event.key == pygame.K_RIGHT and snake_speed[0] == 0:
                    snake_speed = [10, 0]
                elif event.key == pygame.K_p:
                    paused = not paused

        if not paused:
            new_head = [snake_pos[0][0] + snake_speed[0], snake_pos[0][1] + snake_speed[1]]
            snake_pos.insert(0, new_head)

            if check_collision(snake_pos[0]):
                insert_score(user_id, score, level)
                pygame.quit()
                sys.exit()

            if snake_pos[0] == food['pos']:
                score += food['weight']
                if score % 3 == 0:
                    level += 1
                food_spawn = True
            else:
                snake_pos.pop()

            if food_spawn:
                food = get_random_food()
                food_spawn = False

            if pygame.time.get_ticks() - food['spawn_time'] > 10000:
                food_spawn = True

        screen.fill(BLACK)
        for pos in snake_pos:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

        food_color = RED if food['weight'] == 1 else (255, 165, 0)
        pygame.draw.rect(screen, food_color, pygame.Rect(food['pos'][0], food['pos'][1], 10, 10))

        font = pygame.font.SysFont('arial', 20)
        info_text = font.render(f"Score: {score}  Level: {level}  Player: {player_name}", True, WHITE)
        screen.blit(info_text, [10, 10])

        if paused:
            insert_score(user_id, score, level)
            pause_text = font.render("Paused", True, WHITE)
            screen.blit(pause_text, [SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2])

        pygame.display.flip()
        fps.tick(10 + level * speed_increase)

except SystemExit:
    pygame.quit()
