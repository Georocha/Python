import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('AmoreVerdadeAcústico.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
pygame.event.wait()