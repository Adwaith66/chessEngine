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
    rowsToRanks = {'0':'8','1':'7','2':'6','3':'5','4':'4','5':'3','6':'2','7':'1'}
    columnsToFiles = {'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h'}
    ranksToRows =  ((v, k) for k,v in rowsToRanks.items())
    filesToColumns =  ((v, k) for k,v in columnsToFiles.items())


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
        self.selected_piece = ()
        self.selected_squares = []
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

    def move(self, startSquare, endSquare):
        srow = startSquare[0]
        scolumn = startSquare[1]
        erow = endSquare[0]
        ecolumn = endSquare[1]

        

       
        self.board[int(erow)][int(ecolumn)] = self.board[int(srow)][int(scolumn)]
        self.board[int(srow)][(scolumn)] = '--';
        print(self.board)
        print(srow,scolumn,erow, ecolumn)

        
            
    
