import pygame
import os

pygame.init()

playlist = []
# музыкалар орналасқан жерге path 
music_folder = "/Users/bekzatshaiyrgozha/Documents/PP2/lab7/musics"
allmusic = os.listdir(music_folder)

# playlist-қа .mp3 деп аяқталса қосамыз 
for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))
# экран бетіне шағатын терезе көлемі, аты
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Darkhan-Juzz")
clock = pygame.time.Clock()

# артқы фонды енгіземіз
background = pygame.image.load(os.path.join("music-elements", "background.png"))

# кнопкалар тұратын жердің фонын жасаймыз, алдымен көлемі, сосын RGB ақ түс
bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))

# плейлист аты шығып тұратын жер көлемі
font2 = pygame.font.SysFont(None, 20)

# кнопкаларды папкадан енгіземіз
playb = pygame.image.load(os.path.join("music-elements", "play.png"))
pausb = pygame.image.load(os.path.join("music-elements", "pause.png"))
nextb = pygame.image.load(os.path.join("music-elements", "next.png"))
prevb = pygame.image.load(os.path.join("music-elements", "back.png"))

index = 0
aplay = False

pygame.mixer.music.load(playlist[index]) 
pygame.mixer.music.play(1)
aplay = True 

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN: #клавишты басса
            if event.key == pygame.K_SPACE: #егер пробелге тең болса
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT: #егер оң жаққа тең болса
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT: #егер сол жаққа тең болса
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
    #музыка аты шығатын жер 
    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    
    # әр кнопканың орналасуын, көлемін көрсетеміз
    screen.blit(background, (-50, 0))
    screen.blit(bg, (155, 500))
    screen.blit(text2, (365, 520))
    playb = pygame.transform.scale(playb, (70, 70))
    pausb = pygame.transform.scale(pausb, (70, 70))
    if aplay:
        screen.blit(pausb, (370, 590))
    else: 
        screen.blit(playb, (370, 590))
    nextb = pygame.transform.scale(nextb, (70, 70))
    screen.blit(nextb, (460, 587))
    prevb = pygame.transform.scale(prevb, (75, 75))
    screen.blit(prevb, (273, 585))

    clock.tick(24)
    pygame.display.update()
