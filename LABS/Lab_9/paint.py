import pygame 
 
 
WIDTH, HEIGHT = 1200, 600  #Defines the width and height of the game window.
FPS = 90 #screen refresh rate
draw = False   #indicating whether to draw on the screen           
radius = 2    #Brush radius
color = 'blue'           
mode = 'pen'                
fill = False
 
pygame.init() 
screen = pygame.display.set_mode([WIDTH, HEIGHT]) #Creating a window of specified sizes
pygame.display.set_caption('Paint') #name window 
clock = pygame.time.Clock() #for time management
screen.fill(pygame.Color('white'))  #Fills the screen with white.
font = pygame.font.SysFont('None', 30) #Creating a font to display text
 
 
def drawLine(screen, start, end, width, color): 
    # Extract x and y coordinates of start and end points
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    
    # Calculate absolute differences in x and y coordinates
    dx = abs(x1 - x2) 
    dy = abs(y1 - y2) 
    
    # Coefficients for the line equation Ax + By + C = 0
    A = y2 - y1  # Vertically
    B = x1 - x2  # Horizontally
    C = x2 * y1 - x1 * y2 
    
    # If the line is more horizontal than vertical
    if dx > dy: 
        # Ensure x1 is to the left of x2
        if x1 > x2: 
            x1, x2 = x2, x1 
            y1, y2 = y2, y1 
        # Iterate over x coordinates
        for x in range(x1, x2): 
            # Calculate y coordinate using the line equation
            y = (-C - A * x) / B 
            # Draw a circle (pixel) at (x, y) position
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width) 
    # If the line is more vertical than horizontal
    else: 
        # Ensure y1 is below y2
        if y1 > y2: 
            x1, x2 = x2, x1 
            y1, y2 = y2, y1 
        # Iterate over y coordinates
        for y in range(y1, y2): 
            # Calculate x coordinate using the line equation
            x = (-C - B * y) / A 
            # Draw a circle (pixel) at (x, y) position
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)
 
def drawCircle(screen, start, end, width, color): 
    # Extract x and y coordinates of start and end points
    x1 = start[0]  # Extract x-coordinate of the start point
    x2 = end[0]  # Extract x-coordinate of the end point
    y1 = start[1]  # Extract y-coordinate of the start point
    y2 = end[1]  # Extract y-coordinate of the end point
    
    # Calculate the center of the circle
    x = (x1 + x2) / 2  # Calculate the center of the circle along the x-axis
    y = (y1 + y2) / 2  # Calculate the center of the circle along the y-axis
    
    # Calculate the radius of the circle
    radius = abs(x1 - x2) / 2  # Calculate the radius of the circle
    
    # Draw the circle on the screen
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)  # Draw the circle on the screen
 
def drawRectangle(screen, start, end, width, color): 
    # Extract x and y coordinates of start and end points
    x1 = start[0]  # Extract x-coordinate of the start point
    x2 = end[0]  # Extract x-coordinate of the end point
    y1 = start[1]  # Extract y-coordinate of the start point
    y2 = end[1]  # Extract y-coordinate of the end point
    
    # Calculate the width and height of the rectangle
    widthr = abs(x1 - x2)  # Calculate the width of the rectangle
    height = abs(y1 - y2)  # Calculate the height of the rectangle
    
    # Draw the rectangle on the screen based on the position of start and end points
    if x2 > x1 and y2 > y1: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widthr, height), width)  # Draw the rectangle on the screen
    if y2 > y1 and x1 > x2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widthr, height), width)  # Draw the rectangle on the screen
    if x1 > x2 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widthr, height), width)  # Draw the rectangle on the screen
    if x2 > x1 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width)  # Draw the rectangle on the screen

def drawSquare(screen, start, end, color, width=0):
    x1, y1 = start
    x2, y2 = end
    mn = min(abs(x2 - x1), abs(y2 - y1))

    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, mn, mn), width)
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, mn, mn), width)
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, mn, mn), width)
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, mn, mn), width)
 
def drawRightTriangle(screen, start, end, color, width):
    x1, y1 = start
    x2, y2 = end

    points = []
    if x2 > x1 and y2 > y1:
        points = [(x1, y1), (x2, y2), (x1, y2)]
    elif y2 > y1 and x1 > x2:
        points = [(x1, y1), (x2, y2), (x1, y2)]
    elif x1 > x2 and y1 > y2:
        points = [(x1, y1), (x2, y2), (x2, y1)]
    elif x2 > x1 and y1 > y2:
        points = [(x1, y1), (x2, y2), (x2, y1)]

    pygame.draw.polygon(screen, pygame.Color(color), points, width)
 
def drawEquilateralTriangle(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
 
    width_b = abs(x2 - x1) 
    height = (3**0.5) * width_b / 2 
 
    if y2 > y1: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), width) 
    else: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height))) 
     
def drawRhombus(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    pygame.draw.lines(screen, pygame.Color(color), True, (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), width) 
 
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exit()  # Exit the program if the window is closed
         
        # Handling keyboard events
        if event.type == pygame.KEYDOWN: 
            # Change the mode based on the pressed key
            if event.key == pygame.K_r: 
                mode = 'rectangle'  # Set the mode to draw rectangles
            if event.key == pygame.K_c: 
                mode = 'circle'  # Set the mode to draw circles
            if event.key == pygame.K_p: 
                mode = 'pen'  # Set the mode to use a pen
            if event.key == pygame.K_e: 
                mode = 'erase'  # Set the mode to erase
            if event.key == pygame.K_s: 
                mode = 'square'  # Set the mode to draw squares
            if event.key == pygame.K_t: 
                mode = 'right_tri'  # Set the mode to draw right triangles
            if event.key == pygame.K_u: 
                mode = 'eq_tri'  # Set the mode to draw equilateral triangles
            if event.key == pygame.K_h: 
                mode = 'rhombus'  # Set the mode to draw rhombuses
            if event.key == pygame.K_q: 
                screen.fill(pygame.Color('white'))  # Clear the screen by filling it with white color

            if event.key == pygame.K_f:
                fill = not fill  #  switching between fill and contour
            if event.key == pygame.K_RETURN:  # ENTER saved
                pygame.image.save(screen, "drawing.png") 
 
            # Change the color based on the pressed key
            if event.key == pygame.K_1: 
                color = 'black'  # Set the color to black
            if event.key == pygame.K_2: 
                color = 'green'  # Set the color to green
            if event.key == pygame.K_3: 
                color = 'red'  # Set the color to red
            if event.key == pygame.K_4: 
                color = 'blue'  # Set the color to blue
            if event.key == pygame.K_5: 
                color = 'yellow'  # Set the color to yellow
            if event.key == pygame.K_6: 
                color = 'purple'  # Set the color to yellow
            if event.key == pygame.K_7: 
                color = 'orange'  # Set the color to yellow
            
            if event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:  # keys "+"
                radius += 1
                if radius > 100:
                    radius = 100  # lesser 101

            if event.key == pygame.K_MINUS: # keys "-"
                radius -= 1
                if radius < 1:
                    radius = 1  # bigger 0
      
        if event.type == pygame.MOUSEBUTTONDOWN:  
            draw = True  # Enable drawing
            if mode == 'pen': 
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)  # Draw a circle (pixel) if the pen mode is active
            prevPos = event.pos  # Store the current position as the previous position
        
        if event.type == pygame.MOUSEBUTTONUP:  
            w = 0 if fill else radius  # choose size of contour

        # When the mouse button is released
            if mode == 'rectangle': 
                drawRectangle(screen, prevPos, event.pos, w, color)  # Draw a rectangle if the mode is set to draw rectangles
            elif mode == 'circle': 
                drawCircle(screen, prevPos, event.pos, w, color)  # Draw a circle if the mode is set to draw circles
            elif mode == 'square': 
                drawSquare(screen, prevPos, event.pos, color, w)  # Draw a square if the mode is set to draw squares
            elif mode == 'right_tri': 
                drawRightTriangle(screen, prevPos, event.pos, color, w)  # Draw a right triangle if the mode is set to draw right triangles
            elif mode == 'eq_tri': 
                drawEquilateralTriangle(screen, prevPos, event.pos, w, color)  # Draw an equilateral triangle if the mode is set to draw equilateral triangles
            elif mode == 'rhombus': 
                drawRhombus(screen, prevPos, event.pos, w, color)  # Draw a rhombus if the mode is set to draw rhombuses
            draw = False  # Disable drawing
       
        if event.type == pygame.MOUSEMOTION:  
        # When the mouse is moved
            if draw and mode == 'pen': 
                drawLine(screen, lastPos, event.pos, radius, color)  # If drawing is enabled and pen mode is active, draw a line between the last position and the current position
            elif draw and mode == 'erase': 
                drawLine(screen, lastPos, event.pos, radius, 'white')  # If drawing is enabled and erase mode is active, draw a white line (erase) between the last position and the current position
            lastPos = event.pos  # Update the last position to the current position
 
    # Draw a rectangle to display the radius information
    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 170, 110))  # Draw a white rectangle to display the radius information
    pygame.draw.rect(screen, pygame.Color('black'), (5, 5, 170, 110), 2) # black rectangle contour

    renderRadius = font.render(f'R: {radius}', True, pygame.Color('black'))  # Render the text showing the current radius
    color_text = font.render(f'Color: {color}', True, pygame.Color('black'))
    mode_text = font.render(f'Mode: {mode}', True, pygame.Color('black'))
    fill_text = font.render(f'Fill: {fill}', True, pygame.Color('black'))

    screen.blit(renderRadius, (10, 7))  # Blit the rendered text onto the screen at the specified position
    screen.blit(color_text, (10, 30))
    screen.blit(mode_text, (10, 60))
    screen.blit(fill_text, (10, 90))
 
    pygame.display.flip()  # Update the display
    clock.tick(FPS)  # Control the frame rate