import numpy as np
from random import choice 
# from alphaBeta import alphaBeta

def getAvailableMoves(board,player):
    good = np.argwhere(board == player)
    dir = 1 if player == 1 else -1 

    AvailableMoves = []
    for r ,c in good:
        for dc , dr in [(dir, 0),(0,-1),(0,1)]:
            newr , newc = r + dr , c + dc 
            if newr == -1 :
                continue
            try: 

                x = board [ newr , newc]
                if x != player and (x != 3 - player or dr != 0):
                    AvailableMoves.append((r,c,newr,newc))
            except :
                continue
    return AvailableMoves

# def getmove(board , player):
    
#     AvailableMoves = getAvailableMoves(board,player)
#     alphaBeta(board,player,-1)
#     move = choice(AvailableMoves)
#     return move 


if __name__ == "__main__":
    board = np.zeros((5,4),dtype=np.uint8)
    board[0] = np.ones(4, dtype=np.uint8)
    board[4] = 2* np.ones(4, dtype=np.uint8)
    move = getmove(board , 1)
    print(board , move , board[-1])