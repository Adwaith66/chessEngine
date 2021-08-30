import pygame

width = 200
height = 200
row = 8
col = 8
square_size = height // row

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


IMAGES = []

def load_images():
    pieces = ['wp','wR','wN','wB','wK','wQ','bp','bR','bN','bB','bK','bQ']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load('images/' + piece + '.png'), (square_size,square_size))

      
