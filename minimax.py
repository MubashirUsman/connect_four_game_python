#   Mubashir Usman Ijaz
# MinimaxPlayer class is implemented by following the minimax algorithm
# given on the following link: https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html
# Some changes are made to the above algorithm: Alpha-Beta pruning is
# removed to avoid complexity and evaluate method is added to check for the
# terminal condition (instead of calling is_terminal as in the link).

# In the minimax method we check if the game is over.
# If the game is not over we go through to see whose turn it is
# and return the best_score according to the player (min or max). This
# is done every time minimax is called inside the get_move method.
# Then in the get_move method we make a copy of the board to simulate
# the move by calling the valid_columns_list method. Then we calculate
# the score and check if that score is better than the current_score, if
# score is not better, than the move is discarded otherwise it is returned.


import math
import copy

class MinimaxPlayer:
    def __init__(self, max_depth):
        self.max_depth = max_depth

    def get_move(self, board, token):
        best_move = None
        best_score = -math.inf

        for column in board.valid_columns_list():
            new_board = copy.deepcopy(board)
            new_board.update_board(column, token)
            score = self.minimax(new_board, token, self.max_depth, False)

            if score > best_score:
                best_move = column
                best_score = score
        return best_move

    def minimax(self, board, token, depth, is_maximizing):
        if depth == 0 or board.is_game_tie():
            return self.evaluate(board, token) #print("Game Is Over")

        if is_maximizing:
            best_score = -math.inf
            for column in board.valid_columns_list():
                new_board = copy.deepcopy(board)
                new_board.update_board(column, token)
                score = self.minimax(new_board, token, depth - 1, False)
                best_score = max(best_score, score)
            return best_score

        else:
            best_score = float(math.inf)
            other_token = board.opposite_token(token)
            for column in board.valid_columns_list():
                new_board = copy.deepcopy(board)
                new_board.update_board(column, other_token)
                score = self.minimax(new_board, token, depth - 1, True)
                best_score = min(best_score, score)
            return best_score

    def evaluate(self, board, token):

        if board.vertical_check(token) or board.horizontal_check(token) \
                    or board.diagonal_check_down(token) or board.diagonal_check_up(token):
            return math.inf
        elif board.vertical_check(board.opposite_token(token)) or board.horizontal_check(board.opposite_token(token)) \
                    or board.diagonal_check_down(board.opposite_token(token)) or \
                    board.diagonal_check_up(board.opposite_token(token)):
            return -math.inf
        else:
            return 0
