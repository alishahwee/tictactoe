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
    if terminal(board):
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
    elif x_num <= o_num:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # If terminal board, then just return
    if terminal(board):
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
    if terminal(board):
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

    # Initialize a set of cumulative actions for each player
    x_cumulative_actions = set()
    o_cumulative_actions = set()

    # Add all actions made by previous player to cumulative actions
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_cumulative_actions.add((i, j))
            elif board[i][j] == O:
                o_cumulative_actions.add((i, j))

    # Return if cumulative actions are less than 3 (not possible to win under 3 moves)
    if len(x_cumulative_actions) < 3 and len(o_cumulative_actions) < 3:
        return

    # Define possible winning states
    winning_states = {
        frozenset([(0, 0), (0, 1), (0, 2)]),
        frozenset([(1, 0), (1, 1), (1, 2)]),
        frozenset([(2, 0), (2, 1), (2, 2)]),
        frozenset([(0, 0), (1, 0), (2, 0)]),
        frozenset([(0, 1), (1, 1), (2, 1)]),
        frozenset([(0, 2), (1, 2), (2, 2)]),
        frozenset([(0, 0), (1, 1), (2, 2)]),
        frozenset([(2, 0), (1, 1), (0, 2)]),
    }

    # If cumulative action is superset of any winning state, return winner, else return
    if any(x_cumulative_actions.issuperset(state) for state in winning_states):
        return X
    elif any(o_cumulative_actions.issuperset(state) for state in winning_states):
        return O
    else:
        return


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # See if the board has a winner
    if winner(board) is not None:
        return True

    # Check if the board is filled
    if not any(EMPTY in row for row in board):
        return True

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

    # If terminal board, then just return
    if terminal(board):
        return

    # Determine the current player and create a dict to map actions to values
    current_player = player(board)
    action_value_dict = dict()

    # Populate the dict with actions corresponding to their resultant value
    for action in actions(board):
        if current_player == X:  # Maximizing player
            key = min_value(result(board, action))
            if key not in action_value_dict:
                action_value_dict[key] = {action}
            else:
                action_value_dict[key].add(action)
        elif current_player == O:  # Minimizing player
            key = max_value(result(board, action))
            if key not in action_value_dict:
                action_value_dict[key] = {action}
            else:
                action_value_dict[key].add(action)

    # Maximizing player chooses highest value and vice versa
    if current_player == X:
        return action_value_dict[max(action_value_dict)].pop()
    elif current_player == O:
        return action_value_dict[min(action_value_dict)].pop()


def max_value(board):
    """
    Returns the highest utility value from optimal recursive plays.
    """

    # Value to compare against
    value = -math.inf

    # Base case
    if terminal(board):
        return utility(board)

    # Determine the max value out of all the actions
    for action in actions(board):
        value = max(value, min_value(result(board, action)))

    return value


def min_value(board):
    """
    Returns the lowest utility value optimal recursive plays.
    """

    # Value to compare against
    value = math.inf

    # Base case
    if terminal(board):
        return utility(board)

    # Determine the min value out of all the actions
    for action in actions(board):
        value = min(value, max_value(result(board, action)))

    return value
