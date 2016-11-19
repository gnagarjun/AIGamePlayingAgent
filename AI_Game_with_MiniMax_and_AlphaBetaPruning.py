from copy import deepcopy
import sys

FirstLevelmovesList = []

def max(a,b):
    if(int(a) > int(b)):
        return int(a)
    else:
        return int(b)

def min(a,b):
    if(int(a) < int(b)):
        return int(a)
    else:
        return int(b)

def evalMax(board,state,depth,dimension,whoseMove,myPlayer,a,b):
    if depth == 0:
        #terminal moves find eval and return
        return(evalState(state,board,int(dimension),myPlayer))
    else:
        nextStatesList = findNextStates(state,dimension,whoseMove)
        for nextState in nextStatesList:
            a = max(a,evalMin(board,nextState,(int(depth)-1),dimension,'O',myPlayer,a,b))
        return a

def evalMin(board,state,depth,dimension,whoseMove,myPlayer,a,b):
    if depth == 0:
        #terminal moves find eval and return
        return(evalState(state,board,int(dimension),myPlayer))
    else:
        nextStatesList = findNextStates(state,dimension,whoseMove)
        for nextState in nextStatesList:
            b = min (b,evalMax(board,nextState,(int(depth)-1),dimension,'X',myPlayer,a,b))
        return b


#Alpha beta block

def AlphaBetaEvalMax(board,state,depth,dimension,whoseMove,myPlayer,a,b):
    if depth == 0:
        #terminal moves find eval and return
        return(evalState(state,board,int(dimension),myPlayer))
    else:
        nextStatesList = findNextStates(state,dimension,whoseMove)
        for nextState in nextStatesList:
            a = max(a,AlphaBetaEvalMin(board,nextState,(int(depth)-1),dimension,'O',myPlayer,a,b))
            if (a >= b):
                return b
        return a

def AlphaBetaEvalMin(board,state,depth,dimension,whoseMove,myPlayer,a,b):
    if depth == 0:
        #terminal moves find eval and return
        return(evalState(state,board,int(dimension),myPlayer))
    else:
        nextStatesList = findNextStates(state,dimension,whoseMove)
        for nextState in nextStatesList:
            b = min (b,AlphaBetaEvalMax(board,nextState,(int(depth)-1),dimension,'X',myPlayer,a,b))
            if(b <= a):
                return a
        return b

#Alpha beta block


def findNextStates(state,dimension,whoseMove):
    statesList = []
    for i in range(int(dimension)):
        for j in range(int(dimension)):
            whoseMoveFlag = False
            opponentPieceFlag = False
            #Stake moves collection
            if(state[i][j] == '.'):
                nextState = deepcopy(state)
                nextState[i][j] = whoseMove
                statesList.append(nextState)

                #raid moves collection
                if(dimension != 1):

                    #top left corner
                    if(i==0 and j==0):
                        if((state[i][j+1] != '.' and state[i][j+1] != whoseMove) or (state[i+1][j] != '.' and state[i+1][j] != whoseMove)):
                            opponentPieceFlag = True
                        if((state[i][j+1] != '.' and state[i][j+1] == whoseMove) or (state[i+1][j] != '.' and state[i+1][j] == whoseMove)):
                            whoseMoveFlag = True
                        if(opponentPieceFlag and whoseMoveFlag):
                            nextState = deepcopy(state)
                            nextState[i][j+1] = whoseMove
                            nextState[i+1][j] = whoseMove

                            nextState[i][j] = whoseMove
                            statesList.append(nextState)               
                    
                    #top right corner
                    elif(i==0 and (j== dimension-1)):
                        if((state[i][j-1] != '.' and state[i][j-1] != whoseMove) or (state[i+1][j] != '.' and state[i+1][j] != whoseMove)):
                            opponentPieceFlag = True
                        if((state[i][j-1] != '.' and state[i][j-1] == whoseMove) or (state[i+1][j] != '.' and state[i+1][j] == whoseMove)):
                            whoseMoveFlag = True
                        if(opponentPieceFlag and whoseMoveFlag):
                            nextState = deepcopy(state)
                            nextState[i][j-1] = whoseMove
                            nextState[i+1][j] = whoseMove

                            nextState[i][j] = whoseMove
                            statesList.append(nextState)

                    #bottom right corner
                    elif(i== (dimension -1) and j== (dimension-1)):
                        if((state[i][j-1] != '.' and state[i][j-1] != whoseMove) or (state[i-1][j] != '.' and state[i-1][j] != whoseMove)):
                            opponentPieceFlag = True
                        if((state[i][j-1] != '.' and state[i][j-1] == whoseMove) or (state[i-1][j] != '.' and state[i-1][j] == whoseMove)):
                            whoseMoveFlag = True
                        if(opponentPieceFlag and whoseMoveFlag):
                            nextState = deepcopy(state)
                            nextState[i][j-1] = whoseMove
                            nextState[i-1][j] = whoseMove

                            nextState[i][j] = whoseMove
                            statesList.append(nextState)

                    #bottom left corner
                    elif(i== (dimension -1) and j==0):
                        if((state[i][j+1] != '.' and state[i][j+1] != whoseMove) or (state[i-1][j] != '.' and state[i-1][j] != whoseMove)):
                            opponentPieceFlag = True
                        if((state[i][j+1] != '.' and state[i][j+1] == whoseMove) or (state[i-1][j] != '.' and state[i-1][j] == whoseMove)):
                            whoseMoveFlag = True
                        if(opponentPieceFlag and whoseMoveFlag):
                            nextState = deepcopy(state)
                            nextState[i][j+1] = whoseMove
                            nextState[i-1][j] = whoseMove

                            nextState[i][j] = whoseMove
                            statesList.append(nextState)

                    #first row
                    elif(i == 0 and j>0):
                        if((state[i][j-1] != '.' and state[i][j-1] != whoseMove) or (state[i][j+1] != '.' and state[i][j+1] != whoseMove) or (state[i+1][j] != '.' and state[i+1][j] != whoseMove)):
                            opponentPieceFlag = True
                        if((state[i][j-1] != '.' and state[i][j-1] == whoseMove) or (state[i][j+1] != '.' and state[i][j+1] == whoseMove) or (state[i+1][j] != '.' and state[i+1][j] == whoseMove)):
                            whoseMoveFlag = True
                        if(opponentPieceFlag and whoseMoveFlag):
                            nextState = deepcopy(state)
                            if(nextState[i][j-1] != '.'):
                                nextState[i][j-1] = whoseMove
                            if(nextState[i][j+1] != '.'):
                                nextState[i][j+1] = whoseMove
                            if(nextState[i+1][j] != '.'):
                                nextState[i+1][j] = whoseMove
                            
                            nextState[i][j] = whoseMove
                            statesList.append(nextState)
                        
                    #last column
                    elif(i>0 and j== (dimension-1)):
                        if((state[i-1][j] != '.' and state[i-1][j] != whoseMove) or (state[i+1][j] != '.' and state[i+1][j] != whoseMove) or (state[i][j-1] != '.' and state[i][j-1] != whoseMove)):
                            opponentPieceFlag = True
                        if((state[i-1][j] != '.' and state[i-1][j] == whoseMove) or (state[i+1][j] != '.' and state[i+1][j] == whoseMove) or (state[i][j-1] != '.' and state[i][j-1] == whoseMove)):
                            whoseMoveFlag = True
                        if(opponentPieceFlag and whoseMoveFlag):
                            nextState = deepcopy(state)
                            if(nextState[i-1][j] != '.'):
                                nextState[i-1][j] = whoseMove
                            if(nextState[i+1][j] != '.'):
                                nextState[i+1][j] = whoseMove
                            if(nextState[i][j-1] != '.'):
                                nextState[i][j-1] = whoseMove
                            
                            nextState[i][j] = whoseMove
                            statesList.append(nextState)

                    #last row
                    elif(i== (dimension-1) and j>0):
                        if((state[i][j-1] != '.' and state[i][j-1] != whoseMove) or (state[i][j+1] != '.' and state[i][j+1] != whoseMove) or (state[i-1][j] != '.' and state[i-1][j] != whoseMove)):
                            opponentPieceFlag = True
                        if((state[i][j-1] != '.' and state[i][j-1] == whoseMove) or (state[i][j+1] != '.' and state[i][j+1] == whoseMove) or (state[i-1][j] != '.' and state[i-1][j] == whoseMove)):
                            whoseMoveFlag = True
                        if(opponentPieceFlag and whoseMoveFlag):
                            nextState = deepcopy(state)
                            if(nextState[i][j-1] != '.'):
                                nextState[i][j-1] = whoseMove
                            if(nextState[i][j+1] != '.'):
                                nextState[i][j+1] = whoseMove
                            if(nextState[i-1][j] != '.'):
                                nextState[i-1][j] = whoseMove
                            
                            nextState[i][j] = whoseMove
                            statesList.append(nextState)
                        
                    #first column
                    elif(i > 0 and j==0):
                        if((state[i-1][j] != '.' and state[i-1][j] != whoseMove) or (state[i+1][j] != '.' and state[i+1][j] != whoseMove) or (state[i][j+1] != '.' and state[i][j+1] != whoseMove)):
                            opponentPieceFlag = True
                        if((state[i-1][j] != '.' and state[i-1][j] == whoseMove) or (state[i+1][j] != '.' and state[i+1][j] == whoseMove) or (state[i][j+1] != '.' and state[i][j+1] == whoseMove)):
                            whoseMoveFlag = True
                        if(opponentPieceFlag and whoseMoveFlag):
                            nextState = deepcopy(state)
                            if(nextState[i-1][j] != '.'):
                                nextState[i-1][j] = whoseMove
                            if(nextState[i+1][j] != '.'):
                                nextState[i+1][j] = whoseMove
                            if(nextState[i][j+1] != '.'):
                                nextState[i][j+1] = whoseMove
                            
                            nextState[i][j] = whoseMove
                            statesList.append(nextState)

                    #rest anywhere in the middle
                    else:
                        if((state[i][j-1] != '.' and state[i][j-1] != whoseMove) or (state[i][j+1] != '.' and state[i][j+1] != whoseMove) or (state[i+1][j] != '.' and state[i+1][j] != whoseMove) or (state[i-1][j] != '.' and state[i-1][j] != whoseMove)):
                            opponentPieceFlag = True
                        if((state[i][j-1] != '.' and state[i][j-1] == whoseMove) or (state[i][j+1] != '.' and state[i][j+1] == whoseMove) or (state[i+1][j] != '.' and state[i+1][j] == whoseMove or (state[i-1][j] != '.' and state[i-1][j] == whoseMove))):
                            whoseMoveFlag = True
                        if(opponentPieceFlag and whoseMoveFlag):
                            nextState = deepcopy(state)
                            if(nextState[i][j-1] != '.'):
                                nextState[i][j-1] = whoseMove
                            if(nextState[i][j+1] != '.'):
                                nextState[i][j+1] = whoseMove
                            if(nextState[i+1][j] != '.'):
                                nextState[i+1][j] = whoseMove
                            if(nextState[i-1][j] != '.'):
                                nextState[i-1][j] = whoseMove
                            
                            nextState[i][j] = whoseMove
                            statesList.append(nextState)
                    
    #return the list of successors
    return statesList



def evalALPHABETA(board,state,depth,myPlayer,dimension):
    #do
    c=0

def evalCOMPETITION(board,state,depth,myPlayer,dimension):
    #do
    b=0

def evalState(state,board,dimension,myPlayer):
    myScore = 0
    opponentScore = 0
    for i in range(int(dimension)):
        for j in range(int(dimension)):
            if(state[i][j] == myPlayer):
                myScore += int(board[i][j])
            if(state[i][j] != myPlayer and state[i][j] != '.'):
                opponentScore += int(board[i][j])
    return (myScore - opponentScore)


def findNextMoves(state,dimension,player):
    movesList = []
    for i in range(int(dimension)):
        for j in range(int(dimension)):
            myPieceFlag = False
            opponentPieceFlag = False
            #Stake moves collection
            if(state[i][j] == '.'):
                movesList.append(['S',i,j])

                #raid moves collection
                if(dimension != 1):

                    #top left corner
                    if(i==0 and j==0):
                        if((state[i][j+1] != '.' and state[i][j+1] != player) or (state[i+1][j] != '.' and state[i+1][j] != player)):
                            opponentPieceFlag = True
                        if((state[i][j+1] != '.' and state[i][j+1] == player) or (state[i+1][j] != '.' and state[i+1][j] == player)):
                            myPieceFlag = True                    
                    
                    #top right corner
                    elif(i==0 and (j== dimension-1)):
                        if((state[i][j-1] != '.' and state[i][j-1] != player) or (state[i+1][j] != '.' and state[i+1][j] != player)):
                            opponentPieceFlag = True
                        if((state[i][j-1] != '.' and state[i][j-1] == player) or (state[i+1][j] != '.' and state[i+1][j] == player)):
                            myPieceFlag = True

                    #bottom right corner
                    elif(i== (dimension -1) and j== (dimension-1)):
                        if((state[i][j-1] != '.' and state[i][j-1] != player) or (state[i-1][j] != '.' and state[i-1][j] != player)):
                            opponentPieceFlag = True
                        if((state[i][j-1] != '.' and state[i][j-1] == player) or (state[i-1][j] != '.' and state[i-1][j] == player)):
                            myPieceFlag = True

                    #bottom left corner
                    elif(i== (dimension -1) and j==0):
                        if((state[i][j+1] != '.' and state[i][j+1] != player) or (state[i-1][j] != '.' and state[i-1][j] != player)):
                            opponentPieceFlag = True
                        if((state[i][j+1] != '.' and state[i][j+1] == player) or (state[i-1][j] != '.' and state[i-1][j] == player)):
                            myPieceFlag = True

                    #first row
                    elif(i == 0 and j>0):
                        if((state[i][j-1] != '.' and state[i][j-1] != player) or (state[i][j+1] != '.' and state[i][j+1] != player) or (state[i+1][j] != '.' and state[i+1][j] != player)):
                            opponentPieceFlag = True
                        if((state[i][j-1] != '.' and state[i][j-1] == player) or (state[i][j+1] != '.' and state[i][j+1] == player) or (state[i+1][j] != '.' and state[i+1][j] == player)):
                            myPieceFlag = True
                        
                    #last column
                    elif(i>0 and j== (dimension-1)):
                        if((state[i-1][j] != '.' and state[i-1][j] != player) or (state[i+1][j] != '.' and state[i+1][j] != player) or (state[i][j-1] != '.' and state[i][j-1] != player)):
                            opponentPieceFlag = True
                        if((state[i-1][j] != '.' and state[i-1][j] == player) or (state[i+1][j] != '.' and state[i+1][j] == player) or (state[i][j-1] != '.' and state[i][j-1] == player)):
                            myPieceFlag = True

                    #last row
                    elif(i== (dimension-1) and j>0):
                        if((state[i][j-1] != '.' and state[i][j-1] != player) or (state[i][j+1] != '.' and state[i][j+1] != player) or (state[i-1][j] != '.' and state[i-1][j] != player)):
                            opponentPieceFlag = True
                        if((state[i][j-1] != '.' and state[i][j-1] == player) or (state[i][j+1] != '.' and state[i][j+1] == player) or (state[i-1][j] != '.' and state[i-1][j] == player)):
                            myPieceFlag = True
                        
                    #first column
                    elif(i > 0 and j==0):
                        if((state[i-1][j] != '.' and state[i-1][j] != player) or (state[i+1][j] != '.' and state[i+1][j] != player) or (state[i][j+1] != '.' and state[i][j+1] != player)):
                            opponentPieceFlag = True
                        if((state[i-1][j] != '.' and state[i-1][j] == player) or (state[i+1][j] != '.' and state[i+1][j] == player) or (state[i][j+1] != '.' and state[i][j+1] == player)):
                            myPieceFlag = True

                    #rest anywhere in the middle
                    else:
                        if((state[i][j-1] != '.' and state[i][j-1] != player) or (state[i][j+1] != '.' and state[i][j+1] != player) or (state[i+1][j] != '.' and state[i+1][j] != player) or (state[i-1][j] != '.' and state[i-1][j] != player)):
                            opponentPieceFlag = True
                        if((state[i][j-1] != '.' and state[i][j-1] == player) or (state[i][j+1] != '.' and state[i][j+1] == player) or (state[i+1][j] != '.' and state[i+1][j] == player or (state[i-1][j] != '.' and state[i-1][j] == player))):
                            myPieceFlag = True
                    
                    if (myPieceFlag and opponentPieceFlag):
                        movesList.append(['R',i,j])
    #return the list of successors
    return movesList
                            


def main():

    #reading input file content
    fileName = 'input.txt'
    fileReader = open(fileName)
    fileContent = fileReader.read()
    fileReader.close()

	#splitting file content
    splitContent = fileContent.split('\n')
    dimension = splitContent[0]
    mode = splitContent[1]
    myPlayer = splitContent[2]
    depth = splitContent[3]

    board = []
    for i in range(4,(int(dimension)+4)):
        board.append(str(splitContent[i]).split(' '))

    state = []
    offset = int(dimension) + 4
    for i in range(offset,offset+int(dimension)):
        state.append(list(splitContent[i]))

    #checking if the depth is greater than the number of moves possible till the end
    emptyCellsCount = 0
    for i in range(int(dimension)):
        for j in range(int(dimension)):
            if(state[i][j] == '.'):
                emptyCellsCount += 1

    if(int(depth) > emptyCellsCount):
        depth = emptyCellsCount

    #print fileName
    #print dimension
    #print mode
    #print myPlayer
    #print depth
    #print board
    #print state


    allMoves = findNextMoves(state,int(dimension),myPlayer)
    #for move in allMoves:
    #    print move


    allMaxValues = []
    max_value = -999999
    i=0
    j=0
    
    if(myPlayer == 'X'):
        opponent = 'O'
    else:
        opponent = 'X'

    if(mode == 'MINIMAX'):
        allMaxStates = findNextStates(state,int(dimension),myPlayer)
        for maxState in allMaxStates:
            Value = evalMin(board,maxState,(int(depth)-1),int(dimension),opponent,myPlayer,-999999,999999)
            allMaxValues.append(int(Value))
            if(int(Value) > max_value):
                max_value = Value
                j=i
            i+=1

        #######
        #tie breaker for stake and raid moves with the same utlility values
        index = 0
        sameMaxValuesIndices = []
        for eachValue in allMaxValues:
            if (eachValue == max_value):
                sameMaxValuesIndices.append(index)
            index += 1


        raidFound = False
        for eachIndex in sameMaxValuesIndices:
            if(allMoves[int(eachIndex)][0] == 'S'):
                stakeFound = True
                j = eachIndex
                break
            else:
                if (raidFound == False):
                    raidFound = True
                    j = eachIndex

        #######
    
   


    if(mode == 'ALPHABETA'):
        allMaxStates = findNextStates(state,int(dimension),myPlayer)
        for maxState in allMaxStates:
            Value = AlphaBetaEvalMin(board,maxState,(int(depth)-1),int(dimension),opponent,myPlayer,-999999,999999)
            allMaxValues.append(int(Value))
            if(int(Value) > max_value):
                max_value = Value
                j=i
            i+=1
        
        #######
        #tie breaker for stake and raid moves with the same utlility values
        index = 0
        sameMaxValuesIndices = []
        for eachValue in allMaxValues:
            if (eachValue == max_value):
                sameMaxValuesIndices.append(index)
            index += 1

        raidFound = False
        for eachIndex in sameMaxValuesIndices:
            if(allMoves[int(eachIndex)][0] == 'S'):
                stakeFound = True
                j = eachIndex
                break
            else:
                if (raidFound == False):
                    raidFound = True
                    j = eachIndex

        #######

    dudeState = allMoves[j]

    dudeState[1] = dudeState[1] + 1
    dudeState[2] = dudeState[2] + 1

    print dudeState[0]
    if(dudeState[2] == 1):
        dudeState[2] = 'A'
    if(dudeState[2] == 2):
        dudeState[2] = 'B'
    if(dudeState[2] == 3):
        dudeState[2] = 'C'
    if(dudeState[2] == 4):
        dudeState[2] = 'D'
    if(dudeState[2] == 5):
        dudeState[2] = 'E'
    if(dudeState[2] == 6):
        dudeState[2] = 'F'
    if(dudeState[2] == 7):
        dudeState[2] = 'G'
    if(dudeState[2] == 8):
        dudeState[2] = 'H'
    if(dudeState[2] == 9):
        dudeState[2] = 'I'
    if(dudeState[2] == 10):
        dudeState[2] = 'J'
    if(dudeState[2] == 11):
        dudeState[2] = 'K'
    if(dudeState[2] == 12):
        dudeState[2] = 'L'
    if(dudeState[2] == 13):
        dudeState[2] = 'M'
    if(dudeState[2] == 14):
        dudeState[2] = 'N'
    if(dudeState[2] == 15):
        dudeState[2] = 'O'
    if(dudeState[2] == 16):
        dudeState[2] = 'P'
    if(dudeState[2] == 17):
        dudeState[2] = 'Q'
    if(dudeState[2] == 18):
        dudeState[2] = 'R'
    if(dudeState[2] == 19):
        dudeState[2] = 'S'
    if(dudeState[2] == 20):
        dudeState[2] = 'T'
    if(dudeState[2] == 21):
        dudeState[2] = 'U'
    if(dudeState[2] == 22):
        dudeState[2] = 'V'
    if(dudeState[2] == 23):
        dudeState[2] = 'W'
    if(dudeState[2] == 24):
        dudeState[2] = 'X'
    if(dudeState[2] == 25):
        dudeState[2] = 'Y'
    if(dudeState[2] == 26):
        dudeState[2] = 'Z'

    #writing the output to a file
    fileName = "output.txt"
    fileWriter = open(fileName,'w')
    if(dudeState[0] == 'S'):
        strategy = "Stake"
    else:
        strategy = "Raid"
    fileWriter.write(str(dudeState[2])+str(dudeState[1])+' '+strategy+'\n')
    for x in range(int(dimension)):
        for y in range(int(dimension)):
            fileWriter.write(allMaxStates[j][x][y])
        fileWriter.write('\n')

    

main()