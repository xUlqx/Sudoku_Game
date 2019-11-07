import unittest
import unittest.mock
from board_api import BoardApi
from parameterized import parameterized
from sudoku_interface import Interface
from sudoku_game import Sudoku4x4, Sudoku9x9

class TestSudokuBoard(unittest.TestCase):
    def setUp(self):
        self.incomplete_board = [["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                               ["6", "x", "x", "x", "9", "5", "x", "x", "x"],
                               ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                               ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                               ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                               ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                               ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                               ["x", "x", "x", "4", "1", "9", "x", "x", "5"],
                               ["x", "x", "x", "x", "8", "x", "x", "7", "9"]]
        
        self.finished_board = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                         ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                         ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                         ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                         ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                         ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                         ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                         ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                         ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
        
        self.board_4x4 = [["4", "x", "3", "1"],
                               ["x", "3", "x", "x"],
                               ["3", "1", "x", "2"],
                               ["x", "4", "x", "x"]]

        self.game_object = Sudoku9x9()
        self.game_object.set_board(self.incomplete_board)
        self.game_object_4x4 = Sudoku4x4()
        self.game_object_4x4.set_board(self.board_4x4)

    
    def test_Validate_Board_9x9(self):
        self.assertTrue(self.game_object.validate_board())
    
    @parameterized.expand([
        (7, 0, 0),
        (5, 0, 1),
        (6, 0, 4),
        (8, 1, 0),
        (4, 1, 4),
        (7, 1, 5),
        (6, 2, 1),
        (9, 2, 2),
        (8, 2, 7),
        (5, 3, 0),
        (3, 3, 4),
        (8, 3, 8),
        (4, 4, 0),
        (7, 4, 3),
        (9, 4, 5),
        (2, 4, 8),
        (6, 5, 0),
        (9, 5, 4),
        (3, 5, 8),
        (9, 6, 1),
        (6, 6, 6),
        (7, 6, 7)
    ])
    def test_Replace_Base_Numbers_9x9(self, number, row, column):

        error_message = self.game_object.insert_number(number, row, column)

        self.assertEqual(error_message, "Ilegal Value, Or trying to Replace Base Number")

    @parameterized.expand([
        (7, 0, 2),  
        (5, 1, 7),  
        (6, 2, 3),  
        (8, 3, 6),  
        (4, 4, 4),  
        (7, 5, 6),  
        (6, 6, 3),  
        (9, 7, 0),  
        (8, 8, 1),  
        (5, 8, 0),  
        (3, 8, 1),  
        (8, 7, 2),  
        (4, 0, 3),  
        (7, 6, 4),  
        (9, 0, 5),  
        (2, 0, 6),  
        (6, 7, 7),  
        (9, 0, 8),  
        (3, 2, 0),  
        (9, 0, 3),  
        (6, 0, 8),  
        (7, 3, 2),  
        (2, 3, 5),  
        (6, 3, 6),  
        (6, 8, 0),  
        (9, 8, 3),  
        (8, 8, 6)  
    ])
    def test_Validate_Ilegal_Numbers_9x9(self, number, row, column):

        error_message = self.game_object.insert_number(number, row, column)

        self.assertEqual(error_message, "Ilegal Value, Or trying to Replace Base Number")
    
    @parameterized.expand([
        (4, 0, 2),
        (6, 0, 3),
        (8, 0, 5),
        (9, 0, 6),
        (1, 0, 7),
        (2, 0, 8),
        (7, 1, 1),
        (2, 1, 2),
        (1, 1, 3),
        (3, 1, 6),
        (4, 1, 7),
        (8, 1, 8),
        (1, 2, 0),
        (3, 2, 3),
        (4, 2, 4),
        (2, 2, 5),
        (5, 2, 6),
        (7, 2, 8),
        (5, 3, 1),
        (9, 3, 2),
        (7, 3, 3),
        (1, 3, 5),
        (4, 3, 6),
        (2, 3, 7),
        (2, 4, 1),
        (6, 4, 2),
        (5, 4, 4),
        (7, 4, 6),
        (9, 4, 7),
        (1, 5, 1),
        (3, 5, 2),
        (9, 5, 3),
        (4, 5, 5),
        (8, 5, 6),
        (5, 5, 7),
        (9, 6, 0),
        (1, 6, 2),
        (5, 6, 3),
        (3, 6, 4),
        (7, 6, 5),
        (4, 6, 8),
        (2, 7, 0),
        (8, 7, 1),
        (7, 7, 2),
        (6, 7, 6),
        (3, 7, 7),
        (3, 8, 0),
        (4, 8, 1),
        (5, 8, 2),
        (2, 8, 3),
        (6, 8, 5),
        ("x", 8, 2),
        ("x", 8, 3),
        ("x", 8, 5),
        ("x", 8, 6),
        (1, 8, 6),
    ])
    def test_Validate_Legal_Numbers_9x9(self, number, row, column):

        error_message = self.game_object.insert_number(number, row, column)

        self.assertNotEqual(error_message, "Ilegal Value, Or trying to Replace Base Number")

    @parameterized.expand([
        ("7", 0, 2),
        ("5", 1, 7),
        ("6", 2, 3),
        ("8", 3, 6),
        ("4", 4, 4),
        ("7", 5, 6),
        ("6", 6, 3),
        ("9", 7, 0),
        ("8", 8, 1),
        ])
    def test_Validate_Row_Method_9x9(self, number, row, column):

        self.game_object.board[row][column] = number

        self.assertFalse(self.game_object.check_rows(self.game_object.board))

    @parameterized.expand([
        ("7", 0, 2),
        ("5", 1, 7),
        ("6", 2, 3),
        ("8", 3, 6),
        ("4", 4, 4),
        ("7", 5, 6),
        ("6", 6, 3),
        ("9", 7, 0),
        ("8", 8, 1),
        ("5", 8, 0),
        ("3", 8, 1),
        ("8", 7, 2),
        ("4", 0, 3),
        ("7", 6, 4),
        ("9", 0, 5),
        ("2", 0, 6),
        ("6", 7, 7),
        ("9", 0, 8),
        ("3", 2, 0),
        ("9", 0, 3),
        ("6", 0, 8),
        ("7", 3, 2),
        ("2", 3, 5),
        ("6", 3, 6),
        ("6", 8, 0),
        ("9", 8, 3),
        ("8", 8, 6),
    ])
    def test_Validate_Method_9x9(self, number, row, column):

        self.game_object.board[row][column] = number

        self.assertFalse(self.game_object.validate_board())

    def test_Not_Win_Method_9x9(self):

        self.assertFalse(self.game_object.win())

    def test_Already_Won_Method_9x9(self):
        self.board_9x9 = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                         ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                         ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                         ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                         ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                         ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                         ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                         ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                         ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]

        self.game_object = Sudoku9x9()
        self.game_object.set_board(self.board_9x9)
        self.assertTrue(self.game_object.win())

    @parameterized.expand([
        (1, 0, 0),
        (1, 0, 2),
        (1, 0, 3),
        (1, 1, 1),
        (1, 2, 0),
        (1, 2, 1),
        (1, 2, 3),
        (1, 3, 1),
        (1, 0, 0),
        (1, 0, 2),
        (1, 0, 3),
        (1, 1, 1),
        (1, 2, 0),
        (1, 2, 1),
        (1, 2, 3),
        (1, 3, 1),
        (2, 0, 0),
        (2, 0, 2),
        (2, 0, 3),
        (2, 1, 1),
        (2, 2, 0),
        (2, 2, 1),
        (2, 2, 3),
        (2, 3, 1),
        (3, 0, 0),
        (3, 0, 2),
        (3, 0, 3),
        (3, 1, 1),
        (3, 2, 0),
        (3, 2, 1),
        (3, 2, 3),
        (3, 3, 1),
        (4, 0, 0),
        (4, 0, 2),
        (4, 0, 3),
        (4, 1, 1),
        (4, 2, 0),
        (4, 2, 1),
        (4, 2, 3),
        (4, 3, 1),
    ])
    def test_test_Replace_Base_Numbers_4x4(self, number, row, column):

        error_message = self.game_object_4x4.insert_number(number, row, column)

        self.assertEqual(error_message, "Ilegal Value, Or trying to Replace Base Number" )

    @parameterized.expand([
        ("4", 0, 1),
        ("3", 0, 1),
        ("4", 1, 0),
        ("3", 1, 0),
        ("1", 3, 0),
        ("1", 1, 2),
        ("2", 3, 2),
        ("3", 0, 1),
        ("3", 1, 3),
        ("1", 2, 2),
        ("4", 3, 3),
        ("4", 3, 0),
        ("3", 1, 0),
        ("4", 0, 1),
        ("1", 0, 1),
        ("3", 3, 2),
        ("1", 3, 3),
        ("2", 1, 3)
    ])
    def test_Validate_Method(self, number, row, column):
   
        self.game_object_4x4.board[row][column] = number
        self.assertFalse(self.game_object_4x4.validate_board())

    def test_Validate_Board_4x4(self):

        self.assertTrue(self.game_object_4x4.validate_board())

    @parameterized.expand([
        (4, 0, 1),
        (3, 0, 1),
        (4, 1, 0),
        (3, 1, 0),
        (1, 3, 0),
        (1, 1, 2),
        (2, 3, 2)
    ])
    def test_Validad_Region_4x4(self, number, row, column):

        error_message = self.game_object_4x4.insert_number(number, row, column)

        self.assertEqual(error_message, "Ilegal Value, Or trying to Replace Base Number")

    @parameterized.expand([
        (3, 0, 1),
        (3, 1, 3),
        (1, 2, 2),
        (4, 3, 3)
    ])
    def test_Validate_Row_Method_4x4(self, number, row, column):

        error_message = self.game_object_4x4.insert_number(number, row, column)

        self.assertEqual(error_message, "Ilegal Value, Or trying to Replace Base Number")

    @parameterized.expand([
        (4, 3, 0),
        (3, 1, 0),
        (4, 0, 1),
        (1, 0, 1),
        (3, 3, 2),
        (1, 3, 3),
        (2, 1, 3)
    ])
    def test_Validate_Column_Method(self, number, row, column):

        error_message = self.game_object_4x4.insert_number(number, row, column)

        self.assertEqual(error_message, "Ilegal Value, Or trying to Replace Base Number")

    @parameterized.expand([
        (2, 0, 1),
        (4, 2, 2),
        (1, 1, 0),
        (2, 3, 0),
        (2, 1, 2),
        (4, 1, 3),
        (1, 3, 2),
        ("x", 1, 2),
        ("x", 1, 3),
        ("x", 3, 2),
        (3, 3, 3),
    ])
    def test_Validate_Ilegal_Number_4x4(self, number, row, column):

        error_message = self.game_object_4x4.insert_number(number, row, column)

        self.assertNotEqual(error_message, "Ilegal Value, Or trying to Replace Base Number")

    def test_Validate_Not_Won_Method(self):

        self.assertFalse(self.game_object_4x4.win())

    def test_Validate_Already_Won_Method(self):
        self.board_4x4_2 = [["4", "2", "3", "1"],
                         ["1", "3", "2", "4"],
                         ["3", "1", "4", "2"],
                         ["2", "4", "1", "3"]]
        self.game_object_4x4 = Sudoku4x4()
        self.game_object_4x4.set_board(self.board_4x4_2)
        self.assertTrue(self.game_object_4x4.win())

if __name__ == '__main__':
    unittest.main()
