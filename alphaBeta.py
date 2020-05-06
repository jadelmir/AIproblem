import numpy as np 
from copy import deepcopy
from move import getAvailableMoves
from random import choice
p1Rewards = {0:0,1:1,2:10,3:100, 4:1000}
p2Rewards = {4:0,3:1,2:10,1:100, 0:1000}

flag = None
def unmakeMove(board , move,player):
    global flag
    if flag :
         board[move[0]][move[1]] ,board[move[2]][move[3]] = flag ,board[move[0]][move[1]]
         flag = None
    else :
        board[move[0]][move[1]] ,board[move[2]][move[3]] = board[move[2]][move[3]] ,board[move[0]][move[1]]  

def makeMove(board , move,player):
    global flag 
    if  board[move[2]][move[3]] != 0 :
        flag = board[move[2]][move[3]]
    else :
        board[move[0]][move[1]] ,board[move[2]][move[3]] = 0 ,player
 
def evaluate(indexes,player):
    theSum =0 
    for r ,c in indexes:
        theSum += p1Rewards[r] if player ==1 else p2Rewards[r]
    return theSum


def getBoardValue(board,player):
    good = np.argwhere(board == player)
    bad = np.argwhere(board == 3-player)
    score = evaluate(good,player)-evaluate(bad,3-player)
    return score

    

def alphaBeta(board , player , depth,move = None):
    CBoard = deepcopy(board)
    secondPlayer = 3 -player
    depth += 1
    AvailableMoves = getAvailableMoves(CBoard,player)
    if depth > 2: 
        score = getBoardValue(CBoard , secondPlayer)
        return score,move
    maxScore = 0
    maxindex = None
    for i in AvailableMoves:
        makeMove(CBoard,i,player)
        score, ind = alphaBeta(CBoard,secondPlayer,depth,i)
        unmakeMove(CBoard,i,player)
        if score >= maxScore:
            maxScore , maxindex = score , i
    return maxScore,maxindex

    # CBoard[depth]=player
    # a = alphaBeta(CBoard,player,depth)
    # CBoard[depth]=secondPlayer
    # b = alphaBeta(CBoard,secondPlayer,depth)

if __name__ == "__main__":
    board = np.zeros(4 ,dtype=np.uint8)
    depth = -1
    player = 1
    CBoard = [*board]
    b = alphaBeta(CBoard , player , depth )

