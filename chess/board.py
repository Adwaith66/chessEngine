import pygame


width = 600
height = 600
row = 8
col = 8
square_size = height // row

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


IMAGES = {}




class Board:
    def __init__(self):
        self.board = [
        ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
        ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
        ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
    

    ]
        self.selected_piece = None
        self.white_left = self.black_left = 16
        self.white_kings = self.black_kings = 1

    def draw_squares(self, window):
        for i in range(8):
          for j in range(i%2, 8, 2):
            pygame.draw.rect(window, WHITE, (i * square_size, j * square_size, square_size, square_size))

    def draw_pieces(self,window):
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece != '--':
                    window.blit(IMAGES[piece], pygame.Rect(j*square_size, i*square_size, square_size, square_size))
                    
    def load_images(self):
        pieces =  ['wQ', 'wK', 'wB', 'wN', 'wR','bp', 'wp','bQ', 'bK', 'bB', 'bN', 'bR']
        for piece in pieces:
            IMAGES[piece] = pygame.transform.scale(pygame.image.load('images/' + piece + ".png"), (square_size,square_size))
            
