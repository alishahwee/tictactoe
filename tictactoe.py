"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_num = 0
    o_num = 0

    # Count the number of Xs and Os
    for row in board:
        for cell in row:
            if cell == X:
                x_num += 1
            elif cell == O:
                o_num += 1

    # Since X goes first, they will always be +1 moves greater than O
    if x_num > o_num:
        return O
    elif x_num == o_num:
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

    # Add coordinates to actions if empty
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Raise a ValueError if board is terminal
    if not any(EMPTY in row for row in board):
        raise ValueError("Invalid action. No more plays can be made.")

    # Create a deepcopy (result) of the board to modify, determine the current player and action
    result = copy.deepcopy(board)
    current_player = player(board)
    i, j = action

    # If cell is empty where action is made, assign the cell to the current player and return result
    if board[i][j] == EMPTY:
        result[i][j] = current_player
        return result
    else:
        raise ValueError("That action is not allowed.")


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
