import pygame
from pygame.examples.sprite_texture import running

pygame.init()
SCREEN_WIDTH=600
SCREEN_HEGHT=800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEGHT))
pygame.display.set_caption('Игра Тир')
icon = pygame.image.load('tir_icon.jpg')
runnig = True
while running:
    running = False

print('hi git')
pygame.quit()
