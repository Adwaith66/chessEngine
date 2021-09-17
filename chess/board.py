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
    wkingHasMoved = False
    wshortRookHasMoved = False
    wlongRookHasMoved = False
    bkingHasMoved = False
    bshortRookHasMoved = False
    blongRookHasMoved = False
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
            
    
    def move2(self, startSquare, endSquare):
        srow = startSquare[0]
        scolumn = startSquare[1]
        erow = endSquare[0]
        ecolumn = endSquare[1]

        self.chessBoard[erow][ecolumn] = self.chessBoard[srow][scolumn]
        self.chessBoard[srow][scolumn] = '--'

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
                if piecemoved == 'wK':
                    self.wkingHasMoved = True
                    if endSquare==addArray(startSquare,(0,2)):
                        print('startsq', startSquare, 'endsq', endSquare)
                        self.move2((7,7),(7,5))
                    if endSquare==addArray(startSquare,(0,-2)):
                        print('startsq', startSquare, 'endsq', endSquare)
                        self.move2((7,0),(7,3))
                elif piecemoved == 'bK':
                    self.bkingHasMoved = True
                    if endSquare==addArray(startSquare,(0,2)):
                        print('startsq', startSquare, 'endsq', endSquare)
                        self.move2((0,7),(0,5))
                    if endSquare==addArray(startSquare,(0,-2)):
                        print('startsq', startSquare, 'endsq', endSquare)
                        self.move2((0,0),(0,3))
                elif piecemoved == 'wR' and (srow,scolumn) == (7,7):
                    self.wshortRookHasMoved = True
                elif piecemoved == 'wR' and (srow, scolumn) == (7,0):
                    self.wlongRookHasMoved = True 
                elif piecemoved == 'bR' and (srow,scolumn) == (0,7):
                    self.bshortRookHasMoved = True
                elif piecemoved == 'bR' and (srow,scolumn) == (0,0):
                    self.blongRookHasMoved = True

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
            #print(e)
            return False
            
    def showMoves(self,rownum, column, startSquare):
        moveList = []
        color = self.sameColor(startSquare[0],startSquare[1], 'w')
        if ((color=='w' and self.whiteToMove) or (color=='b' and not self.whiteToMove)):
            pass
            
        else:
            #print('color', color, 'toMove', self.whiteToMove)
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
            kingPos = self.kingPosition()
            kingRow = kingPos[0]
            kingCol = kingPos[1]
            if (self.canCastleS()):
                moveList.append((kingRow,kingCol+2))
            if (self.canCastleL()):
                moveList.append((kingRow,kingCol-2))
         
        #print('MoveList:',moveList)
        moveList = self.determineCheckMoves(startSquare, moveList)
        return moveList


    def showMoves2(self,rownum, column, startSquare):
        moveList = []
        color = self.sameColor(startSquare[0],startSquare[1], 'w')
        self.whiteToMove = not self.whiteToMove
        if ((color=='w' and self.whiteToMove) or (color=='b' and not self.whiteToMove)):
            pass
            self.whiteToMove = not self.whiteToMove
        else:
            #print('color', color, 'toMove', self.whiteToMove)
            self.whiteToMove = not self.whiteToMove
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
            kingPos = self.kingPosition()
            kingRow = kingPos[0]
            kingCol = kingPos[1]
            if (self.canCastleS()):
                moveList.append((kingRow,kingCol+2))
            if (self.canCastleL()):
                moveList.append((kingRow,kingCol-2))
         
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
            #print("BISHOP MOVES", moveList)

        elif self.chessBoard[rownum][column][1] =='Q':
            moveList = checkDiagonal(self,rownum,column)
            #print('QUEEN MOVE DIAGONAL', moveList)
            moveList2 = checkStraight(self,rownum,column)
            #print('QUEEN MOVE STRAIGHT', moveList)
            moveList = moveList + moveList2
            #print('QUEEN MOVE LIST', moveList)
        elif self.chessBoard[rownum][column][1] =='K':
            moveList = kingMoves(self,rownum,column)
         
        #print('MoveList:',moveList)
        #moveList = self.determineCheckMoves(rownum, column, moveList)
        return moveList   
    

    def inCheck(self):
        checked = False
        kingPos = self.kingPosition()
        
        #print('KingPosiiton',kingPosition)
        #print('Queen Possible Moves' ,self.possibleMoves2(3,7))



        for i in range(8):
            for j in range(8):
                if kingPos in self.possibleMoves2(i, j):
                    #print('Rownum', i)
                    #print('Column', j)
                    ##print('Piece', self.chessBoard[i][j])
                    checked = True

  
        return checked


    def determineCheckMoves(self, startSquare, moveList):
        moveList2 = []
        for i in moveList:
            testBoard = copy.deepcopy(self)
            
            testBoard.move(startSquare, i, moveList)
            #print(testBoard.whiteToMove)
            testBoard.whiteToMove=not testBoard.whiteToMove
            if(not testBoard.inCheck()):
                moveList2.append(i)
        #print('Updated Move List:', moveList)
        return moveList2


    def kingPosition(self):
        kingPosition = None
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
        return kingPosition

    def canCastleS(self):
      
        kingPos = self.kingPosition()
        kingRow = kingPos[0]
        kingCol = kingPos[1]
        color = self.sameColor(kingRow,kingCol,'b')
        canCastle=False
        hasntMoved = False
        if(color=='w'):
            if(self.wkingHasMoved==False and self.wshortRookHasMoved==False):
                hasntMoved=True
            
        else:
            if(self.bkingHasMoved==False and self.bshortRookHasMoved==False):
                hasntMoved=True
        if(hasntMoved):
            testBoard = Board()
            testBoard = copy.deepcopy(self)
            moveList = self.possibleMoves2(kingRow,kingCol)
            #print('OriginalMoveList' , moveList)
            testBoard.move(kingPos,(kingRow, kingCol+1), moveList)
            canCastle = (kingRow,kingCol+2) in testBoard.possibleMoves2(kingRow,kingCol+1)
            #print('newMoveList',testBoard.possibleMoves2(kingRow,kingCol+1))
            #print(canCastle)
        return canCastle

    def canCastleL(self):
      
       
        kingPos = self.kingPosition()
        kingRow = kingPos[0]
        kingCol = kingPos[1]
        color = self.sameColor(kingRow,kingCol,'b')
        canCastle=False
        hasntMoved = False
        if(color=='w'):
            if(self.wkingHasMoved==False and self.wlongRookHasMoved==False):
                hasntMoved=True
            
        else:
            if(self.bkingHasMoved==False and self.blongRookHasMoved==False):
                hasntMoved=True
        if(hasntMoved):
            testBoard = Board()
            testBoard = copy.deepcopy(self)
            moveList = self.possibleMoves2(kingRow,kingCol)
            print('OriginalMoveList' , moveList)
            testBoard.move(kingPos,(kingRow, kingCol-1), moveList)
            canCastle = (kingRow,kingCol-2) in testBoard.possibleMoves2(kingRow,kingCol-1)
            print('newMoveList',testBoard.possibleMoves2(kingRow,kingCol-1))
            print(canCastle)
        return canCastle

    def addArray(arr1, arr2):
        index = 0
        output = [0,0]
        for i in arr1:
            output[index] = arr2[index]+i
            index = index+1
        return tuple(output)

    def filterOutNotInBoard(self,arr):
        arr2 = []
        for i in arr:
            if ((i[0]>=0 or i[0]<=7) and (i[1]>=7 or i[1]<=0)):
                arr2.append(i)
        return arr2

    def checkMate(self) -> bool:
        allPossibleMoves = []
        color = 'b' if self.whiteToMove else 'w'
        for i in range(8):
            for j in range(8):
                #print(i,j)
                if(self.chessBoard[i][j][0] == color):
                    for x in self.showMoves2(i,j, (i,j)):
                        allPossibleMoves.append(x)
                    print(self.showMoves2(i,j, (i,j)))

        allPossibleMoves = self.filterOutNotInBoard(allPossibleMoves)
        print(allPossibleMoves)
        return allPossibleMoves==[]


   