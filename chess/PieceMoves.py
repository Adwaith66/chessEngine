def pawnMoves(self,rownum, column):
    moveList = []
    currentPos = (rownum,column)
    color = self.chessBoard[rownum][column][0]
    if color == 'w':
        factor = [-1,0]
        original = 6
        final = 0
    else:
        factor = [1,0]
        original = 1
        final = 7
    allMoves = [(0,0),(0,1),(0,-1)]
    newFactor = factor
    #print("Piece pos", currentPos)

        #Check 1 square forward
    for i in allMoves:
        position = ()
        position = addArray(addArray(factor, i), currentPos)
        if(i == (0,0)):
            if containsPiece(self, position[0], position[1])==False and sameColor(self, position[0], position[1], color) != color:
                moveList.append(position)
            if (containsPiece(self, addArray(position,factor)[0], position[1])==False and sameColor(self, addArray(position,factor)[0], position[1], color) != color) and rownum==original:
                moveList.append(addArray(position,factor))
        else:
            if containsPiece(self, position[0], position[1]) and sameColor(self, position[0], position[1], color) != color:
                moveList.append(position)
    return moveList
      

def knightMoves(self,rownum,column):
        color = self.chessBoard[rownum][column][0]
        moveList = []
        allMoves = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,-2),(2,1),(2,-1),(1,2)]
        currentPos = (rownum, column)
        #print("COlro:",color)
     #Left 2 up 1
        for i in allMoves:
            position = addArray(currentPos, i)
            if sameColor(self, position[0],position[1],color) != color:
                moveList.append(position)
        return moveList

def kingMoves(self,rownum,column):
        color = self.chessBoard[rownum][column][0]
        moveList = []
        allMoves = [(-1,0),(-1,1),(1,0),(1,1),(-1,-1),(0,1),(0,-1),(1,-1)]
        currentPos = (rownum, column)
     
        for i in allMoves:
            position = addArray(currentPos, i)
            if sameColor(self, position[0],position[1],color) != color:
                moveList.append(position)
        return moveList



    #check all four linear directions and make list

def containsPiece(self, rownum, column)->bool:
    currentPos = [rownum, column]

    try: 
        #print("Piece:", self.chessBoard[currentPos[0]][currentPos[1]])
        isPiece = self.chessBoard[currentPos[0]][currentPos[1]]!='--'
        return isPiece


    except Exception as e:
        print(e)
        return False
    
def sameColor(self, rownum, column, color)-> bool:
    try:
        currentPos = [rownum, column]
        return self.chessBoard[currentPos[0]][currentPos[1]][0]

    except Exception as e:
        print(e)
        return False


def checkStraight(self, rownum, column):
    moveList = []
    color = self.chessBoard[rownum][column][0]
    oppColor = 'b' if color == 'w' else 'w'
    allMoves = [(-1,0),(0,-1),(1,0),(0,1)]
    currentPos = (rownum, column)
    position = currentPos

    for i in allMoves:
        position = currentPos
        try:
            while((containsPiece(self, position[0]+i[0], position[1]+i[1]) == False or sameColor(self,position[0]+i[0], position[1]+i[1], color)!=color) and ((position[0]+i[0]<=7 and position[0]+i[0]>=0) and (position[1]+i[1]<=7 and position[1]+i[1]>=0))):
                position = addArray(i, position)
                #print('Eror')
                if(sameColor(self,position[0], position[1], color) == oppColor):
                    moveList.append(position)
                    break
                moveList.append(position)
        
        except Exception as e:
            print(e)
            return moveList

        
    return moveList
    
def checkDiagonal(self, rownum, column):
    moveList = []
    color = self.chessBoard[rownum][column][0]
    oppColor = 'b' if color == 'w' else 'w'
    allMoves = [(-1,1),(1,-1),(1,1),(-1,-1)]
    currentPos = (rownum, column)
    position = currentPos

    for i in allMoves:
        position = currentPos
        try:
            while((containsPiece(self, position[0]+i[0], position[1]+i[1]) == False or sameColor(self,position[0]+i[0], position[1]+i[1], color)!=color) and ((position[0]+i[0]<=7 and position[0]+i[0]>=0) and (position[1]+i[1]<=7 and position[1]+i[1]>=0))):
                position = addArray(i, position)
                if(sameColor(self,position[0], position[1], color) == oppColor):
                    moveList.append(position)
                    break
                moveList.append(position)
        
        except Exception as e:
            print(e)
            return moveList

        
    return moveList
    
    
def addArray(arr1, arr2):
    index = 0
    output = [0,0]
    for i in arr1:
        output[index] = arr2[index]+i
        index = index+1
    return tuple(output)