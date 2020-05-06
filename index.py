import numpy as np
from random import choice 
from alphaBeta import alphaBeta
from move import getAvailableMoves

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




def makeMove(board , move):
     board[move[0]][move[1]] ,board[move[2]][move[3]] = board[move[2]][move[3]] ,board[move[0]][move[1]]   

def getmove(board , player):
    
    AvailableMoves = getAvailableMoves(board,player)
    for i in AvailableMoves:
        if player == 1 and i[3] == 4 :
                return i
        elif player == 2 and i[3]== 0:
                return i    
        if board[i[2],i[3]] == 3- player:
            return i 
    move = alphaBeta(board,player,-1)
    return move[1] 
        
def getname():
    return "MR..JAD"  


if __name__ == "__main__":
    # player = 1 
    # isRunning = True
    # board = np.zeros((5, 4), dtype=np.uint8)
    # board[0] = np.ones(4, dtype=np.uint8)
    # board[4] = 2 * np.ones(4, dtype=np.uint8)
    # while(isRunning):
    #     print(board)
    #     input("? ")
    #     move = getAvailableMoves(board , player)
    #     makeMove(board , move)
    #     player = 3 - player

    board = np.zeros((5,4),dtype=np.uint8)
    board[0] = np.ones(4, dtype=np.uint8)
    board[4] = 2* np.ones(4, dtype=np.uint8)
    while(True):
        move = getmove(board , 1)
        makeMove(board,move)

        move = getmove(board , 2)
        makeMove(board,move)

        print(board)
        input("? ")