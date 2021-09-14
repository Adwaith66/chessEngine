def pawnMoves(self,rownum, column):
    moveList = []
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

    return moveList


def knightMoves(self,rownum,column):
        color = self.chessBoard[rownum][column][0]
        moveList = []
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
    
        return moveList


    #check all four linear directions and make list

def checkStraight(self, rownum, column):
    moveList = []
    color = self.chessBoard[rownum][column][0]
    oppColor = 'b' if color == 'w' else 'w'

    #check up
    i = -1
    try:
        while ((self.chessBoard[rownum+i][column] == '--' or self.chessBoard[rownum+i][column][0] != color) and rownum+i>=0):
          if(self.chessBoard[rownum+i][column][0] == oppColor):
            moveList.append((rownum+i,column))
            break
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
            pass
    except Exception as e:
            print(e)
            pass


    #check right
    i = 1
    try:
        while ((self.chessBoard[rownum][column+i] == '--' or self.chessBoard[rownum][column+i][0] != color) and column+i<=7):
            moveList.append((rownum,column+i))
            i+=1
        else:
            return moveList
    except Exception as e:
            return moveList
            print(e)
            pass

