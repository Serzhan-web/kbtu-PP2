import pygame
import math

# Utility: Create checkered background

def create_background(width, height):
    colors = [(255, 255, 255), (212, 212, 212)]
    background = pygame.Surface((width, height))
    tile_width = 20
    y = 0
    while y < height:
        x = 0
        while x < width:
            row = y // tile_width
            col = x // tile_width
            pygame.draw.rect(
                background,
                colors[(row + col) % 2],
                pygame.Rect(x, y, tile_width, tile_width))
            x += tile_width
        y += tile_width
    return background


# Utility: Detect quit events

def is_trying_to_quit(event):
    pressed_keys = pygame.key.get_pressed()
    alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
    x_button = event.type == pygame.QUIT
    altF4 = alt_pressed and event.type == pygame.KEYDOWN and event.key == pygame.K_F4
    escape = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
    return x_button or altF4 or escape


# Rectangle demo

def do_rectangle_demo(surface, counter):
    left = (counter // 2) % surface.get_width()
    top = (counter // 3) % surface.get_height()
    width = 30
    height = 30
    color = (128, 0, 128)  # purple
    pygame.draw.rect(surface, color, pygame.Rect(left, top, width, height))


# Circle demo

def do_circle_demo(surface, counter):
    x = surface.get_width() // 2
    y = surface.get_height() // 2
    max_radius = min(x, y) * 4 // 5
    radius = abs(int(math.sin(counter * math.pi * 2 / 200) * max_radius)) + 1
    color = (0, 140, 255)  # aquamarine
    pygame.draw.circle(surface, color, (x, y), radius)


# Bad outlines demo

def do_horrible_outlines(surface, counter):
    color = (255, 0, 0)  # red
    pygame.draw.rect(surface, color, pygame.Rect(10, 10, 100, 100), 10)
    pygame.draw.circle(surface, color, (300, 60), 50, 10)


# Good outlines demo

def do_nice_outlines(surface, counter):
    color = (0, 128, 0)  # green
    pygame.draw.rect(surface, color, pygame.Rect(10, 10, 100, 10))
    pygame.draw.rect(surface, color, pygame.Rect(10, 10, 10, 100))
    pygame.draw.rect(surface, color, pygame.Rect(100, 10, 10, 100))
    pygame.draw.rect(surface, color, pygame.Rect(10, 100, 100, 10))

    center_x = 300
    center_y = 60
    radius = 45
    iterations = 150
    for i in range(iterations):
        ang = i * math.pi * 2 / iterations
        dx = int(math.cos(ang) * radius)
        dy = int(math.sin(ang) * radius)
        x = center_x + dx
        y = center_y + dy
        pygame.draw.circle(surface, color, (x, y), 5)


# Polygon (star) demo

def do_polygon_demo(surface, counter):
    color = (255, 255, 0)  # yellow
    num_points = 8
    point_list = []
    center_x = surface.get_width() // 2
    center_y = surface.get_height() // 2
    for i in range(num_points * 2):
        radius = 100
        if i % 2 == 0:
            radius = radius // 2
        ang = i * math.pi / num_points + counter * math.pi / 60
        x = center_x + int(math.cos(ang) * radius)
        y = center_y + int(math.sin(ang) * radius)
        point_list.append((x, y))
    pygame.draw.polygon(surface, color, point_list)


# 3D point rotation

def rotate_3d_points(points, angle_x, angle_y, angle_z):
    new_points = []
    for point in points:
        x, y, z = point
        new_y = y * math.cos(angle_x) - z * math.sin(angle_x)
        new_z = y * math.sin(angle_x) + z * math.cos(angle_x)
        y, z = new_y, new_z

        new_x = x * math.cos(angle_y) - z * math.sin(angle_y)
        new_z = x * math.sin(angle_y) + z * math.cos(angle_y)
        x, z = new_x, new_z

        new_x = x * math.cos(angle_z) - y * math.sin(angle_z)
        new_y = x * math.sin(angle_z) + y * math.cos(angle_z)
        x, y = new_x, new_y

        new_points.append([x, y, z])
    return new_points


# 3D cube line demo

def do_line_demo(surface, counter):
    color = (0, 0, 0)  # black
    cube_points = [
        [-1, -1, 1], [-1, 1, 1], [1, 1, 1], [1, -1, 1],
        [-1, -1, -1], [-1, 1, -1], [1, 1, -1], [1, -1, -1]
    ]
    connections = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    t = counter * 2 * math.pi / 60
    points = rotate_3d_points(cube_points, t / 2, t / 4, t / 6)
    flattened_points = [
        (p[0] * (1 + 1.0 / (p[2] + 3)), p[1] * (1 + 1.0 / (p[2] + 3))) for p in points
    ]
    for con in connections:
        p1 = flattened_points[con[0]]
        p2 = flattened_points[con[1]]
        x1 = p1[0] * 60 + 200
        y1 = p1[1] * 60 + 150
        x2 = p2[0] * 60 + 200
        y2 = p2[1] * 60 + 150
        pygame.draw.line(surface, color, (x1, y1), (x2, y2), 4)


# Main demo runner

def run_demos(width, height, fps):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Press SPACE to switch demo')
    background = create_background(width, height)
    clock = pygame.time.Clock()

    demos = [
        do_rectangle_demo,
        do_circle_demo,
        do_horrible_outlines,
        do_nice_outlines,
        do_polygon_demo,
        do_line_demo
    ]
    counter = 0

    while demos:
        counter += 1
        for event in pygame.event.get():
            if is_trying_to_quit(event):
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                demos.pop(0)
                screen.blit(background, (0, 0))

        if demos:
            screen.blit(background, (0, 0))
            demos[0](screen, counter)

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


# Run the demo sequence
run_demos(400, 300, 60)