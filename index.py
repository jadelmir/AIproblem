import numpy as np 


def getElement(board , X , Y , player):
    if  X < 0 or X > 4 : return None
    if  Y <0 or Y > 3: return None
    elem = board[X][Y]
    if elem == player : return None 
    if elem == 0 : return (0 , X ,Y ) 
    if elem == 3 - player : return (3 -player , X , Y)

def CoordAvailableMove(board ,X , Y, player):
    TOP = getElement(board, X - 1, Y, player)
    BOT = getElement(board, X + 1, Y, player)
    Right = getElement(board, X , Y+1, player)
    Left = getElement(board, X , Y-1, player)

    return (TOP , Right, BOT, Left)

def getAvailableMoves(board , player):
    print("player is",player)
    points = np.where(board == player)
    X , Y = points
    for i in range(len(X)):
        mov = CoordAvailableMove(board , X[i], Y[i] , player)
    
    for x in mov :
         if x :
            return(X[i], Y[i], x[1],x[2])


def makeMove(board , move):
     board[move[0]][move[1]] ,board[move[2]][move[3]] = board[move[2]][move[3]] ,board[move[0]][move[1]]   


        


if __name__ == "__main__":
    player = 1 
    isRunning = True
    board = np.zeros((5, 4), dtype=np.uint8)
    board[0] = np.ones(4, dtype=np.uint8)
    board[4] = 2 * np.ones(4, dtype=np.uint8)
    while(isRunning):
        print(board)
        input("? ")
        move = getAvailableMoves(board , player)
        makeMove(board , move)
        player = 3 - player
