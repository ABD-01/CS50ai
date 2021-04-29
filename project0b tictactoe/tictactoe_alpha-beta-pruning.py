"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    # raise NotImplementedError
    return X if sum(sum([cell is EMPTY for cell in row]) for row in board) % 2 else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # raise NotImplementedError
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i,j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise NotImplementedError
    if action is None:
        return board
    i,j = action
    if board[i][j] != EMPTY:
        raise Exception("Invalid Move")
    bc = deepcopy(board)
    plyr = player(bc)
    bc[i][j] = plyr
    return bc

# Helper function
def transpose(board):
    return [list(row) for row in zip(*board)]

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal and Vertical cases
    if any(row.count(X) == 3 for row in board) or any(row.count(X) == 3 for row in transpose(board)):
        return X
    if any(row.count(O) == 3 for row in board) or any(row.count(O) == 3 for row in transpose(board)):
        return O

    # Diagonal Cases
    if all(board[i][i] == X for i in range(3)) or all(board[i][2-i] == X for i in range(3)):
        return X
    if all(board[i][i] == O for i in range(3)) or all(board[i][2-i] == O for i in range(3)):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # raise NotImplementedError
    if winner(board) is not None:
        return True # Win/lose condition
    if all(row.count(EMPTY) == 0 for row in board):
        return True # Tie Condition
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # raise NotImplementedError
    wnr = winner(board)
    if wnr is EMPTY:
        return 0
    if wnr == X:
        return 1 
    return -1

# cases_explored = 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # global cases_explored
    # cases_explored = 0
    alpha = -math.inf
    beta = math.inf
    if terminal(board):
        return None

    # MAX-VALUE
    if player(board) == X:  
        value = -math.inf
        optimAction = None
        for action in actions(board):
            # cases_explored += 1
            new_value = min_value(result(board,action), alpha, beta)
            if value < new_value:
                optimAction = action
                value = new_value
            alpha = max(alpha, value)
            if alpha >= beta:
                break
    
    # MIN-VALUE
    else:
        value = math.inf
        optimAction = None
        for action in actions(board):
            # cases_explored += 1
            new_value = max_value(result(board, action), alpha, beta)
            if value > new_value:
                optimAction = action
                value = new_value
            beta = min(beta, value)
            if beta <= alpha:
                break

    # print("No. of cases explored :", cases_explored)
    return optimAction


def max_value(board, alpha, beta):
    """
    Return the max-value for the given state
    """
    # global cases_explored
    if terminal(board):
        return utility(board)

    value = -math.inf
    for action in actions(board):
        # cases_explored += 1
        value = max(value, min_value(result(board, action), alpha, beta))
        alpha = max(alpha, value)
        if alpha >= beta:
            break
    return value

def min_value(board, alpha, beta):
    """
    Return the min-value for the given state
    """   
    # global cases_explored
    if terminal(board):
        return utility(board)

    value = math.inf
    for action in actions(board):
        # cases_explored += 1
        value = min(value, max_value(result(board, action), alpha, beta))
        beta = min(beta, value)
        if beta <= alpha:
            break
    return value