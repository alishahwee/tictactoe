"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    # If terminal board, then just return
    if not any(EMPTY in row for row in board):
        return

    # Give X the first move
    if board == initial_state():
        return X

    # Initialize variables to keep track of turns
    xNum = 0
    oNum = 0

    # Count the number of Xs and Os
    for row in board:
        for cell in row:
            if cell == X:
                xNum += 1
            elif cell == O:
                oNum += 1

    # Since X goes first, they will always be +1 moves greater than O
    if xNum > oNum:
        return O
    elif xNum == oNum:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # If terminal board, then just return
    if not any(EMPTY in row for row in board):
        return

    # Initialize an empty set of available actions
    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
