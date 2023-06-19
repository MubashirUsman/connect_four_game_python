#   Mubashir Usman Ijaz
# This is the main file and game is started using start_the_game
# function. It selects either the game will be played between
# two human players (human_game_starts) or between a human and a
# computer (computer_game_starts). Both types use Board class to
# create and update the board. Also board class methods are called
# to check for the valid positions available to insert the token, game is draw,
# and winning conditions as the game proceeds. computer_game_starts starts
# by creating an instance of MinimaxPlayer class. Computer is always
# assigned with -1 token and human player always takes first turn. Both
# types of games switch the turn based on the player. games_options function
# is called (to give options of Restart/Quit) every time a player has to make a move.
# game_finished function is invoked if either player wins or game is drawn, and it
# asks the user to either restart or quit the game.

import sys
from game_options import game_options
from minimax import MinimaxPlayer


def computer_game_starts():
    depth = 5
    game_over = False
    turn = 0
    player_one = 1
    player_two = -1
    board = Board()
    computer = MinimaxPlayer(depth)
    while not game_over:
        if turn == 0:
            while True:
                print("Player 1's turn")
                column = game_options()
                if column in ("Q", "q"):
                    sys.exit()
                elif column in ("R", "r"):
                    game_over = False
                    board = Board()
                    turn = 0
                    break
                else:
                    column = int(column) - 1
                if board.is_column_valid(column) and (0 <= column < 5):
                    board.update_board(column, player_one)
                    break
                    # player = False
                else:
                    print("select a different column")
            board.show_board()
            if board.vertical_check(player_one) or board.horizontal_check(player_one) or \
                    board.diagonal_check_down(player_one) or board.diagonal_check_up(player=player_one):
                print("Player 1 WON!!!")
                game_finished()
            if board.is_game_tie():
                print("Game Draw")
                game_finished()
        else:
            # player = True
            column = computer.get_move(board, player_two)
            board.update_board(column, player_two)
            board.show_board()
            if board.vertical_check(player_two) or board.horizontal_check(player_two) or \
                    board.diagonal_check_down(player_two) or board.diagonal_check_up(player=player_two):
                print("Computer WON!!!")
                game_finished()
            if board.is_game_tie():
                print("Game Draw")
                game_finished()

        turn += 1
        turn = turn % 2


def human_game_starts():
    game_over = False
    turn = 0
    player_one = 1
    player_two = -1
    board = Board()
    while not game_over:
        if turn == 0:
            # player = True
            while True:
                print("Player 1's turn")
                column = game_options()
                if column in ("Q", "q"):
                    sys.exit()
                elif column in ("R", "r"):
                    game_over = False
                    board = Board()
                    turn = 0
                    break
                else:
                    column = int(column) - 1
                # column = int(input("Player 1's turn: "))
                if board.is_column_valid(column) and (0 <= column < 5):
                    board.update_board(column, player_one)
                    break
                    # player = False
                else:
                    print("select a different column")
            board.show_board()
            if board.vertical_check(player_one) or board.horizontal_check(player_one) or \
                    board.diagonal_check_down(player_one) or board.diagonal_check_up(player=player_one):
                print("Player 1 WON!!!")
                game_finished()
            if board.is_game_tie():
                print("Game Draw")
                game_finished()
        else:
            # player = True
            while True:
                print("Player 2's turn")
                column = game_options()
                if column in ("Q", "q"):
                    sys.exit()
                elif column in ("R", "r"):
                    game_over = False
                    board = Board()
                    turn = 0
                    break
                else:
                    column = int(column) - 1
                # column = int(input("Player 2's turn: "))
                if board.is_column_valid(column) and (0 <= column < 5):
                    board.update_board(column, player_two)
                    break
                    # player = False
                else:
                    print("select a different column")
            board.show_board()
            if board.vertical_check(player_two) or board.horizontal_check(player_two) \
                    or board.diagonal_check_down(player_two) or board.diagonal_check_up(player_two):
                print("Player 2 WON!!!")
                game_finished()
            if board.is_game_tie():
                print("Game Draw")
                game_finished()

        turn += 1
        turn = turn % 2


def game_finished():
    print("Game finished\n\tWould you like to Restart or Quit the game\nEnter Q or R")
    while True:
        finished_input = input()
        if finished_input in ("R", "r"):
            start_the_game()
            break
        elif finished_input in ("q", "Q"):
            sys.exit()
        else:
            print("Choose a valid option")


class Board:
    def __init__(self):
        self.my_board = [
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', ''],
            ['', '', '', '', '']
        ]
        self.number_of_rows = len(self.my_board)
        self.number_of_columns = len(self.my_board[0])
        self.welcome_string = "Welcome to Connect Four Game!! Key Bindings are:\n\tQ = Quit \n\tR = Restart"
        print(self.welcome_string)

    def update_board(self, column, token):
        for row in range(3, -1, -1):
            if self.my_board[row][column] == '':
                self.my_board[row][column] = token
                break

    def show_board(self):
        for row in self.my_board:
            print(row)

    def is_column_valid(self, column):
        return self.my_board[0][column] == ''

    def vertical_check(self, player):
        for i_column in range(self.number_of_columns):
            for i_row in range(3, -1, -1):
                if (self.my_board[i_row][i_column] == player) and (self.my_board[i_row - 1][i_column] == player) and \
                        self.my_board[i_row - 2][i_column] == player and self.my_board[i_row - 3][i_column] == player:
                    return True

    def horizontal_check(self, player):
        for i_row in range(self.number_of_rows):
            for i_column in range(self.number_of_columns - 3):
                if self.my_board[i_row][i_column] == player and self.my_board[i_row][i_column + 1] == player and \
                        self.my_board[i_row][i_column + 2] == player and self.my_board[i_row][i_column + 3] == player:
                    return True

    def diagonal_check_down(self, player):
        for i_column in range(self.number_of_columns - 3):
            for i_row in range(self.number_of_rows - 3):
                if self.my_board[i_row][i_column] == player and self.my_board[i_row + 1][i_column + 1] == player and \
                        self.my_board[i_row + 2][i_column + 2] == player and self.my_board[i_row + 3][
                     i_column + 3] == player:
                    return True

    def diagonal_check_up(self, player):
        for i_row in range(3, self.number_of_rows):
            for i_column in range(self.number_of_columns - 3):
                if self.my_board[i_row][i_column] == player and self.my_board[i_row - 1][i_column + 1] == player and \
                        self.my_board[i_row - 2][i_column + 2] == player and self.my_board[i_row - 3][
                     i_column + 3] == player:
                    return True

    def is_game_tie(self):
        for i_row in self.my_board:
            if '' in i_row:
                return False
        return True

    def valid_columns_list(self):
        valid_columns = []
        for i_column in range(self.number_of_columns):
            if self.is_column_valid(i_column):
                valid_columns.append(i_column)
        return valid_columns

    def opposite_token(self, token):
        if token == 1:
            return -1
        else:
            return 1


def start_the_game():
    print("Choose between Computer or Human player")
    user_choice = input("\tH for Human\n\tC for computer\n")
    if user_choice == "H":
        print("\n###  Two player mode selected  ###")
        return human_game_starts()
    else:
        print("\n###  Computer will be playing with you!!  ###")
        return computer_game_starts()


start_the_game()