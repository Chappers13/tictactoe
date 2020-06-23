"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    no_count = 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1
            elif board[i][j] == EMPTY:
                no_count += 1
    if no_count == 9:
        return X
    elif x_count > o_count:
        return O
    else:
        return X
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actns = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                act = (i,j)
                actns.add(act)
    return actns


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if ((int(action[0]) + int(action[1])) > 4) or board[action[0]][action[1]] != EMPTY or ((int(action[0]) + int(action[1])) < 0):
        raise Exception("Not a valid board input")
    new_board = copy.deepcopy(board)
    turn = player(new_board)
    new_board[action[0]][action[1]] = turn
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        #check column wins
        if (board[0][i] == board[1][i] and
            board[1][i] == board[2][i] and
            board[2][i] != EMPTY):
            if board[2][i] == X:
                return X
            else:
                return O
        #checking for row wins
        if (board[i][0] == board[i][1] and
            board[i][1] == board[i][2] and
            board[i][2] != EMPTY):
            if board[i][2] == X:
                return X
            else:
                return O
        #diagonal checks
    if (board[0][0] == board[1][1] and
            board[1][1] == board[2][2] and
            board[2][2] != EMPTY):
            if board[2][2] == X:
                return X
            else:
                return O
    if (board[0][2] == board[1][1] and
            board[1][1] == board[2][0] and
            board[2][0] != EMPTY):
            if board[2][0] == X:
                return X
            else:
                return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                empty_count += 1

    win = winner(board)
    if win == X or win == O or empty_count == 0:
        return True
    else:
        return False

        

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """ 
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    bestScore = None
    #consider all the possible actions i can take
    #put myself in opponents shoes
    #then so on and so forth
    #until we get to a terminal state
    #and then return the minimum or maximum value 
    #the further we are from the terminal state, the bigger the tree is
    if terminal(board):
        return None
    else:
        if player(board) == X:
            bestMove = None
            v = -1000
            for action in actions(board):
                bestScore = max(minimax(result(board, action)), bestScore)
                if bestScore == 1:
                    return action
                else:
                    if v < bestScore:
                        v = bestScore
                        bestMove = action
            return bestMove
        else:
            bestMove = None
            v = 1000
            for action in actions(board):
                bestScore = min(minimax(result(board, action)), bestScore)
                if bestScore == -1:
                    return action
                else:
                    if v > bestScore:
                        v = bestScore
                        bestMove = action
            return bestMove

'''

def MAX(board):
    if terminal(board):
        return utility(board)

    bestMove = None
    v = -1000
    for action in actions(board):
        if board[action[0]][action[1]] == EMPTY:
            bestScore = max(minimax(result(board, action)), bestScore)
        if bestScore == 1:
            return action
        else:
            if v < bestScore:
                v = bestScore
                bestMove = action
    return bestMove            

def MIN(board):
    if terminal(board):
        return utility(board)

    bestScore = 1000
    for action in actions(board):
        if board[action[0]][action[1]] == EMPTY:
            bestScore = min(minimax(result(board, action)), bestScore)
    return bestScore
'''