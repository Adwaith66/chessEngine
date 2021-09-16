import pygame
import copy
from chess.PieceMoves import *
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
        try:
            if endSquare in moveList:
            
                srow = startSquare[0]
                scolumn = startSquare[1]
                erow = endSquare[0]
                ecolumn = endSquare[1]
                piecemoved = self.chessBoard[srow][scolumn]
                pieceremoved = self.chessBoard[erow][ecolumn]
                
            
            
                self.chessBoard[erow][ecolumn] = self.chessBoard[srow][scolumn]
                self.chessBoard[srow][scolumn] = '--'


                self.whiteToMove=not self.whiteToMove
                self.move_log.append((startSquare, endSquare, piecemoved, pieceremoved))
                if endSquare[0] == 0 and piecemoved == 'wp':
                    self.chessBoard[erow][ecolumn] = 'wQ'
        except:
            pass
            
            
    def undo(self):
        if len(self.move_log)!=0:
            self.chessBoard[self.move_log[-1][0][0]][self.move_log[-1][0][1]] = self.move_log[-1][2]
            self.chessBoard[self.move_log[-1][1][0]][self.move_log[-1][1][1]] = self.move_log[-1][3]
            self.move_log.pop()
            self.whiteToMove = not self.whiteToMove

    def sameColor(self, rownum, column, color):
        try:
            currentPos = [rownum, column]
            return self.chessBoard[currentPos[0]][currentPos[1]][0]

        except Exception as e:
            print(e)
            return False
            
    def showMoves(self,rownum, column, startSquare):
        moveList = []
        color = self.sameColor(self.selected_piece[0],self.selected_piece[1], 'w')
        if ((color=='w' and self.whiteToMove) or (color=='b' and not self.whiteToMove)):
            pass
            
        else:
            print('color', color, 'toMove', self.whiteToMove)
            return moveList
        #If pawn
        if self.chessBoard[rownum][column][1] == 'p':
            moveList = pawnMoves(self,rownum,column)
           
        #Knight
        elif self.chessBoard[rownum][column][1] == 'N':
            moveList = knightMoves(self,rownum, column)
            
        elif self.chessBoard[rownum][column][1] == 'R':
            moveList= checkStraight(self,rownum,column)
            #print('results:',self.checkStraight(rownum,column), moveList)
        elif self.chessBoard[rownum][column][1] =='B':
            moveList = checkDiagonal(self,rownum,column)
        elif self.chessBoard[rownum][column][1] =='Q':
            moveList = checkDiagonal(self,rownum,column)
            moveList2 = checkStraight(self,rownum,column)
            moveList = moveList + moveList2
        elif self.chessBoard[rownum][column][1] =='K':
            moveList = kingMoves(self,rownum,column)
         
        #print('MoveList:',moveList)
        moveList = self.determineCheckMoves(startSquare, moveList)
        return moveList

    def possibleMoves2(self,rownum, column):
        moveList = []
        #If pawn
        if self.chessBoard[rownum][column][1] == 'p':
            moveList = pawnMoves(self,rownum,column)
           
        #Knight
        elif self.chessBoard[rownum][column][1] == 'N':
            moveList = knightMoves(self,rownum, column)
            
        elif self.chessBoard[rownum][column][1] == 'R':
            moveList= checkStraight(self,rownum,column)
            #print('results:',self.checkStraight(rownum,column), moveList)
        elif self.chessBoard[rownum][column][1] =='B':
            moveList = checkDiagonal(self,rownum,column)
            print("BISHOP MOVES", moveList)

        elif self.chessBoard[rownum][column][1] =='Q':
            moveList = checkDiagonal(self,rownum,column)
            print('QUEEN MOVE DIAGONAL', moveList)
            moveList2 = checkStraight(self,rownum,column)
            print('QUEEN MOVE STRAIGHT', moveList)
            moveList = moveList + moveList2
            print('QUEEN MOVE LIST', moveList)
        elif self.chessBoard[rownum][column][1] =='K':
            moveList = kingMoves(self,rownum,column)
         
        #print('MoveList:',moveList)
        #moveList = self.determineCheckMoves(rownum, column, moveList)
        return moveList   
    

    def inCheck(self):
        checked = False
        if self.whiteToMove:
            color = 'w'
        else:
            color = "b"
        for i in range(8):
            for j in range(8):
                if self.chessBoard[i][j][0] == color and self.chessBoard[i][j][1]=='K':
                    rownum = i
                    column = j
                    kingPosition = (rownum,column)
        
        print('KingPosiiton',kingPosition)
        print('Queen Possible Moves' ,self.possibleMoves2(3,7))



        for i in range(8):
            for j in range(8):
                if kingPosition in self.possibleMoves2(i, j):
                    print('Rownum', i)
                    print('Column', j)
                    print('Piece', self.chessBoard[i][j])
                    checked = True

        if(checked):
            print('INCHECK!LK:JSDFAL:KJSDPIJOH')
        return checked


    def determineCheckMoves(self, startSquare, moveList):
        for i in moveList:
            testBoard = copy.deepcopy(self)
            
            testBoard.move(startSquare, i, moveList)
            #print(testBoard.whiteToMove)
            testBoard.whiteToMove=not testBoard.whiteToMove
            if(testBoard.inCheck()):
                moveList.remove(i)
        #print('Updated Move List:', moveList)
        return moveList


    

    