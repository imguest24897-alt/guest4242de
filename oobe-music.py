import pygame
file_path = 'music/welcome_to_osu.mp3' # i dunno why osu! music but decided to put that ¯\_(ツ)_/¯
pygame.mixer.init()

pygame.mixer.music.load(file_path)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
pygame.quit()
