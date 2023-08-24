from board_functions import BoardFunctions
from scoring_system import ScoringSystem

# Here I lay out  the design of the game that can easily be changed and I have locked the grid to be equal rows and
# columns by only having one variable where a integer can be

class Tic_tac_toe:

    grid_layout = 3
    rows = grid_layout
    cols = grid_layout

    player_one = 'X'
    player_two = 'O'

    player_one_count = 0
    player_two_count = 0

    board_functions = BoardFunctions()
    scoring_system = ScoringSystem()

    play_board = board_functions.make_board( rows, cols)

    while True:
        player = player_one if player_one_count <= player_two_count else player_two
        move_row_string = input(f"Next move for player {player} select row position out of 1 to {grid_layout} :")
        move_col_string = input(f"Next move for player {player} select column position out of 1 to {grid_layout} :")
        move_row = int(move_row_string) - 1
        move_col =  int(move_col_string) - 1

        if play_board[move_row][move_col] == ' ':
            play_board[move_row][move_col] =  player
            board_functions.format_board(play_board, rows, cols)
            if scoring_system.check_game(play_board, player, grid_layout) == True:
                print(f"{player} wins the game!")
                break

            if player == player_one:
                player_one_count += 1
            else:
                player_two_count += 1

        else:
            print("Please enter a empty location on a board")


