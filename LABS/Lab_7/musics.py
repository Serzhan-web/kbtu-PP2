import pygame
import os

pygame.init()

playlist = []
music_folder = "/Users/Lenovo/Desktop/All_Labs/LABS/Lab_7/musics"
allmusic = os.listdir(music_folder)

for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Musics")
clock = pygame.time.Clock()

background = pygame.image.load(os.path.join("LABS/Lab_7/music-elements", "background.png"))

bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))

font2 = pygame.font.SysFont(None, 20)

playb = pygame.image.load(os.path.join("LABS/Lab_7/music-elements", "play.png"))
pausb = pygame.image.load(os.path.join("LABS/Lab_7/music-elements", "pause.png"))
nextb = pygame.image.load(os.path.join("LABS/Lab_7/music-elements", "next.png"))
prevb = pygame.image.load(os.path.join("LABS/Lab_7/music-elements", "back.png"))

playb = pygame.transform.scale(playb, (70, 70))
pausb = pygame.transform.scale(pausb, (70, 70))
nextb = pygame.transform.scale(nextb, (70, 70))
prevb = pygame.transform.scale(prevb, (75, 75))

play_rect = pygame.Rect(370, 590, 70, 70)
next_rect = pygame.Rect(460, 587, 70, 70)
prev_rect = pygame.Rect(273, 585, 75, 75)

index = 0
volume = 0.5

pygame.mixer.music.load(playlist[index]) 
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play(0)
aplay = True 
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()
            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.set_volume(volume)
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.set_volume(volume)
                pygame.mixer.music.play()
            if event.key == pygame.K_UP:
                volume = min(volume + 0.1, 1.0)
                pygame.mixer.music.set_volume(volume)
            if event.key == pygame.K_DOWN:
                volume = max(volume - 0.1, 0.0)
                pygame.mixer.music.set_volume(volume)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()
            elif next_rect.collidepoint(event.pos):
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.set_volume(volume)
                pygame.mixer.music.play()
                aplay = True
            elif prev_rect.collidepoint(event.pos):
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.set_volume(volume)
                pygame.mixer.music.play()
                aplay = True

    screen.blit(background, (-60, -180))
    screen.blit(bg, (155, 500))

    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    screen.blit(text2, (365, 520))

    if aplay:
        screen.blit(pausb, (370, 590))
    else: 
        screen.blit(playb, (370, 590))
    screen.blit(nextb, (460, 587))
    screen.blit(prevb, (273, 585))

    clock.tick(24)
    pygame.display.update()
