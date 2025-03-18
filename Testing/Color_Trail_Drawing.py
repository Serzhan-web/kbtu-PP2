import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Color Trail Drawing")
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []

    running = True
    while running:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            # Проверка выхода
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_w and ctrl_held) or \
                   (event.key == pygame.K_F4 and alt_held) or \
                   (event.key == pygame.K_ESCAPE):
                    running = False
                elif event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ — увеличить радиус
                    radius = min(200, radius + 1)
                elif event.button == 3:  # ПКМ — уменьшить радиус
                    radius = max(1, radius - 1)

            elif event.type == pygame.MOUSEMOTION:
                position = event.pos
                points.append(position)
                points = points[-256:]  # храним только последние 256 точек

        screen.fill((0, 0, 0))  # очистка экрана

        # Рисуем линии между точками
        for i in range(len(points) - 1):
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def drawLineBetween(screen, index, start, end, width, color_mode):
    # Градиент цвета на основе позиции в списке точек
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    else:
        color = (255, 255, 255)

    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))

    if distance == 0:
        pygame.draw.circle(screen, color, start, width)
        return

    for i in range(distance):
        progress = i / distance
        x = int(start[0] + dx * progress)
        y = int(start[1] + dy * progress)
        pygame.draw.circle(screen, color, (x, y), width)

main()
