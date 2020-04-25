import numpy as np 


def getVal(board , X , Y , player):
    if X < 1 : return None
    elem = board[X][Y]
    if elem == player : return None 
    if elem == 0 : return (0 , X ,Y ) 
    if elem == 3 - player : return (3 -player , X , Y)

def CoordAvailableMove(board ,X , Y, player):
    TOP = getVal(board, X - 1, Y, player)
    BOT = getVal(board, X + 1, Y, player)
    Right = getVal(board, X , Y+1, player)
    Left = getVal(board, X , Y-1, player)

    return (TOP , Right, BOT, Left)

def getAvailableMoves(board , player):
    points = np.where(board == player)
    X , Y = points
    for i in range(len(X)):
        mov = CoordAvailableMove(board , X[i], Y[i] , player)
        print(mov)
    
    for x in mov :
         if x :
            return(X[i], Y[i], x[1],x[2])




        


if __name__ == "__main__":
    player = 1 
    board = np.zeros((5, 4), dtype=np.uint8)

    board[0] = np.ones(4, dtype=np.uint8)
    board[4] = 2 * np.ones(4, dtype=np.uint8)
    move = getAvailableMoves(board , player)
    print(move)
