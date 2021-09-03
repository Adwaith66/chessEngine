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
    whiteToMove = True
    moveLog = []

    def __init__(self):
        self.chessBoard = [
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
        self.move_log = []

    def draw_squares(self, window):
        for i in range(8):
          for j in range(i%2, 8, 2):
            pygame.draw.rect(window, WHITE, (i * square_size, j * square_size, square_size, square_size))

    def draw_pieces(self,window):
        for i in range(8):
            for j in range(8):
                piece = self.chessBoard[i][j]
                if piece != '--':
                    window.blit(IMAGES[piece], pygame.Rect(j*square_size, i*square_size, square_size, square_size))
                
                    
    def load_images(self):
        pieces =  ['wQ', 'wK', 'wB', 'wN', 'wR','bp', 'wp','bQ', 'bK', 'bB', 'bN', 'bR']
        for piece in pieces:
            IMAGES[piece] = pygame.transform.scale(pygame.image.load('images/' + piece + ".png"), (square_size,square_size))
            
    

    def move(self, startSquare, endSquare, moveList):
        if endSquare in moveList:
            srow = startSquare[0]
            scolumn = startSquare[1]
            erow = endSquare[0]
            ecolumn = endSquare[1]
            piecemoved = self.chessBoard[srow][scolumn]
            pieceremoved = self.chessBoard[erow][ecolumn]
            
            
           
            self.chessBoard[erow][ecolumn] = self.chessBoard[srow][scolumn]
            self.chessBoard[srow][scolumn] = '--';
            self.move_log.append((startSquare, endSquare, piecemoved, pieceremoved))
            if endSquare[0] == 0 and piecemoved == 'wp':
                self.chessBoard[erow][ecolumn] = 'wQ'
            
            print(self.move_log)
            
    def undo(self):
        if len(self.move_log)!=0:
            self.chessBoard[self.move_log[-1][0][0]][self.move_log[-1][0][1]] = self.move_log[-1][2]
            self.chessBoard[self.move_log[-1][1][0]][self.move_log[-1][1][1]] = self.move_log[-1][3]
            self.move_log.pop()
            
    def possibleMoves(self, window,rownum, column):
        moveList = []
        #If pawn
        if self.chessBoard[rownum][column][1] == 'p':
            color = self.chessBoard[rownum][column][0]
            if color == 'w':
                factor = -1
                original = 6
            else:
                factor = 1
                original = 1
            print(color,factor)
            
            #Check 1 square forward
            try:
                if self.chessBoard[rownum+factor][column] == '--' and self.chessBoard[rownum+factor][column][0] != color:
                    moveList.append((rownum+factor,column))
            except Exception as e:
                print(e)
                pass
            
            #Check 2 squares forward
            print(rownum,original,(factor*2)+rownum)
            try:
                if self.chessBoard[rownum+(factor*2)][column] == '--' and (self.chessBoard[rownum+factor][column][0] != color and rownum == original):
                    moveList.append((rownum+(factor*2),column))
            except Exception as e:
                print(e)
                pass

            #Check left diagonal
            try: 
                if self.chessBoard[rownum+factor][column-1] != '--' and self.chessBoard[rownum+factor][column-1][0] != color:
                    moveList.append((rownum+factor,column-1))
            except Exception as e:
                print(e)
                pass

            #Check right diagonal
            try:
                if self.chessBoard[rownum+factor][column+1] != '--' and self.chessBoard[rownum+factor][column+1][0] != color:
                    moveList.append((rownum+factor,column+1))
            except Exception as e:
                print(e)
                pass

        #Knight
        elif self.chessBoard[rownum][column][1] == 'N':
            color = self.chessBoard[rownum][column][0]
        
    
        
         #Left 2 up 1
            try:
                if self.chessBoard[rownum-1][column-2][0] != color:
                    moveList.append((rownum-1,column-2))
            except Exception as e:
                print(e)
                pass

            #Left 1 up 2
            try:
                if self.chessBoard[rownum-2][column-1][0] != color:
                    moveList.append((rownum-2,column-1))
            except Exception as e:
                print(e)
                pass

            #Right 1 up 2
            try:
                if self.chessBoard[rownum-2][column+1][0] != color:
                    
                    moveList.append((rownum-2,column+1))
            except Exception as e:
                print(e)
                pass

            #Right 2 up 1
            try:
                if self.chessBoard[rownum-1][column+2][0] != color:
                    moveList.append((rownum-1,column+2))
            except Exception as e:
                print(e)
                pass

          
            #Left 2 down 1
            try:
                if self.chessBoard[rownum+1][column-2][0] != color:
                    moveList.append((rownum+1,column-2))
            except Exception as e:
                print(e)
                pass

            #Left 1 down 2
            try:
                if self.chessBoard[rownum+2][column-1][0] != color:
                    moveList.append((rownum+2,column-1))
            except Exception as e:
                print(e)
                pass

            #Right 1 down 2
            try:
                if self.chessBoard[rownum+2][column+1][0] != color:
                    moveList.append((rownum+2,column+1))
            except Exception as e:
                print(e)
                pass

            #Right 2 down 1
            try:
                if self.chessBoard[rownum+1][column+2][0] != color:
                    moveList.append((rownum+1,column+2))
            except Exception as e:
                print(e)
                pass
        elif self.chessBoard[rownum][column][1] == 'R':
            moveList= self.checkStraight(rownum,column)
            print('results:',self.checkStraight(rownum,column), moveList)

         
        print(moveList)
        return moveList
    

    #check all four linear directions and make list

    def checkStraight(self, rownum, column):
        moveList = []
        color = self.chessBoard[rownum][column][0]

        #check up
        i = -1
        try:
            while ((self.chessBoard[rownum+i][column] == '--' or self.chessBoard[rownum+i][column][0] != color) and rownum+i>=0):
                moveList.append((rownum+i,column))
                i-=1
            else:
                pass
        except Exception as e:
                print(e)
                pass

        #check left 
        i = -1
        try:
            while ((self.chessBoard[rownum][column+i] == '--' or self.chessBoard[rownum][column+i][0] != color) and column+i>=0):
                moveList.append((rownum,column+i))
                i-=1
            else:
                pass
        except Exception as e:
                print(e)
                pass

        #check bottom
        i = 1
        try:
            while ((self.chessBoard[rownum+i][column] == '--' or self.chessBoard[rownum+i][column][0] != color) and rownum+i<=7):
                moveList.append((rownum+i,column))
                i+=1
            else:
                return moveList
        except Exception as e:
                print(e)
                pass


        #check right
        i = 1
        try:
            while ((self.chessBoard[rownum][column+i] == '--' or self.chessBoard[rownum][column+i][0] != color) and column+i<=7):
                moveList.append((rownum,column+i))
                print("POG")
                i+=1
            else:
                return moveList
        except Exception as e:
                return moveList
                print(e)
                pass


