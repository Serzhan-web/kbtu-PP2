import pygame 
import time
import math
pygame.init()

#пайда болатын экран ұзындықтары
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#пайда болған экранның жоғар жағындағы атау
pygame.display.set_caption("Mickey clock")

#суреттерді пайда болған экранға енгіземіз
leftarm = pygame.image.load("images/leftarm.png")
rightarm = pygame.image.load("images/rightarm.png")
mainclock = pygame.transform.scale(pygame.image.load("images/clock.png"), (800, 600))

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #localtime арқылы минут пен сикундты анықтап аламыз
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    #минут пен сикундтың бұрышын алып аламыз
    #қазіргі минут * 360 градус / 60 минут + қазіргі секундты қосамыз 
    minute_angle = minute * 6    + (second / 60) * 6   
    second_angle = second * 6  
    
    #экран бетіне пайда фонмен болуы
    screen.blit(mainclock, (0,0))
    
    #оң қол минутты орналастыру
    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(rightarm, (800, 600)), -minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(800 // 2, 600 // 2 + 12))
    screen.blit(rotated_rightarm, rightarmrect)
    
    #сол қол секундты орналастыру
    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(leftarm, (40.95, 682.5)), -second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(800 // 2, 600 // 2 + 10))
    screen.blit(rotated_leftarm, leftarmrect)
    
    pygame.display.flip() #окноны жаңартады
    clock.tick(60) #fps
    
pygame.quit()