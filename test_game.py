import unittest

from GameLib.GameRunner import GameRunner
from GameLib.TicTacToe import TicTacToe


class TestGameRunner(unittest.TestCase):

    def setUp(self):
        self.game_runner = GameRunner()

    def test_should_return_current_player_in_0_or_1(self):
        actual = self.game_runner.get_current_player()
        expected = [0, 1]
        self.assertIn(actual, expected)

    def test_should_alternate_current_player(self):
        actual1 = self.game_runner.get_current_player()
        allowed = self.game_runner.take_turn(5)
        actual2 = self.game_runner.get_current_player()
        self.assertTrue(allowed)
        self.assertNotEqual(actual1, actual2)

    def test_should_return_false_when_all_postions_taken(self):
        for i in range(1, 10):
            self.game_runner.take_turn(i)
        allowed = self.game_runner.take_turn(1)
        self.assertFalse(allowed)

    def test_should_throw_exception_when_invalid_turn(self):
        self.game_runner.take_turn(1)
        with self.assertRaises(ValueError):
            self.game_runner.take_turn(1)

    def test_should_return_correct_winner(self):
        for i in [1, 2, 4, 6, 8, 9]:
            self.game_runner.take_turn(i)
        for i in [3, 5, 7]:
            self.game_runner.take_turn(i)
        actual = self.game_runner.get_winner()
        expected = [1, 2]
        self.assertIn(actual, expected)


class TestTickTacToeGame(unittest.TestCase):

    def setUp(self):
        self.tictactoe = TicTacToe()

    def test_should_initlize_board(self):
        actual = self.tictactoe.draw(False)
        expected = "| 1 | 2 | 3 |\n------------\n| 4 | 5 | 6 |\n------------\n| 7 | 8 | 9 |\n"
        self.assertEqual(actual, expected)

    def test_should_allow_valid_turn(self):
        self.tictactoe.turn(1, 'x')
        actual = self.tictactoe.draw()
        expected = "| x |   |   |\n------------\n|   |   |   |\n------------\n|   |   |   |\n"
        self.assertEqual(actual, expected)

    def test_should_throw_exception_when_invalid_turn(self):
        self.tictactoe.turn(1, 'x')
        with self.assertRaises(ValueError):
            self.tictactoe.turn(1, 'x')

    def test_should_return_all_postions_taken_as_false(self):
        self.tictactoe.turn(1, 'x')
        actual = self.tictactoe.all_positions_taken()
        expected = False
        self.assertEqual(actual, expected)

    def test_should_return_all_postions_taken_as_true(self):
        for i in range(1, 10):
            self.tictactoe.turn(i, 'x')
        actual = self.tictactoe.all_positions_taken()
        expected = True
        self.assertEqual(actual, expected)

    def test_should_check_column_and_return_true(self):
        for i in [1, 4, 7, 3, 6, 9]:
            self.tictactoe.turn(i, 'o')
        for i in [2, 5, 8]:
            self.tictactoe.turn(i, 'x')
        actual = self.tictactoe.check('x')
        expected = True
        self.assertEqual(actual, expected)

    def test_should_check_row_and_return_true(self):
        for i in [1, 2, 3, 7, 8, 9]:
            self.tictactoe.turn(i, 'o')
        for i in [4, 5, 6]:
            self.tictactoe.turn(i, 'x')
        actual = self.tictactoe.check('x')
        expected = True
        self.assertEqual(actual, expected)

    def test_should_check_diagonal_and_return_true(self):
        for i in [2, 3, 4, 6, 7, 8]:
            self.tictactoe.turn(i, 'o')
        for i in [1, 5, 9]:
            self.tictactoe.turn(i, 'x')
        actual = self.tictactoe.check('x')
        expected = True
        self.assertEqual(actual, expected)

    def test_should_check_anti_diagonal_and_return_true(self):
        for i in [1, 2, 4, 6, 8, 9]:
            self.tictactoe.turn(i, 'o')
        for i in [3, 5, 7]:
            self.tictactoe.turn(i, 'x')
        actual = self.tictactoe.check('x')
        expected = True
        self.assertEqual(actual, expected)

    def test_should_check_game_draw_and_return_false(self):
        for i in [1, 3, 4, 8]:
            self.tictactoe.turn(i, 'o')
        for i in [2, 5, 6, 7, 9]:
            self.tictactoe.turn(i, 'x')

        actual = self.tictactoe.check('x')
        expected = False
        self.assertEqual(actual, expected)

        actual = self.tictactoe.check('o')
        expected = False
        self.assertEqual(actual, expected)


unittest.main(verbosity=0)
