import unittest

from scoring_system import ScoringSystem
from board_functions import BoardFunctions

class MakeBoard(unittest.TestCase):

    # I chose  to test that the board is created with equal values to create a square playing board as the game won't
    # work if the board is in a rectangular style
    def test_are_two_values_equal(self):
        board_functions = BoardFunctions()
        result = board_functions.make_board(3,3)
        test_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.assertEqual(result,test_board)

class ScoringCondtions(unittest.TestCase):

    # I chose to test that the scoring system will work by comparing a  test wining board against the function
    def test_scoring_conditions_validation(self):
        scoring_system = ScoringSystem()
        test_board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        result = scoring_system.check_game(test_board, 'X', 3)
        self.assertEqual(result, True)

