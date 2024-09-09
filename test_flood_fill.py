import unittest
from typing import List
from flood_fill import get_connected_tiles, get_largest_connected_color, flood_fill

class TestFloodFill(unittest.TestCase):
    """Unit tests for the flood fill algorithm functions."""

    def setUp(self):
        """Sets up the test environment by initializing the board and colors."""
        
        self.board_1 = [
            ['R', 'R', 'G', 'G', 'G', 'G'],
            ['R', 'G', 'G', 'G', 'G', 'G'],
            ['R', 'G', 'R', 'R', 'G', 'G'],
            ['R', 'G', 'R', 'R', 'G', 'G'],
            ['R', 'G', 'G', 'G', 'G', 'G'],
            ['R', 'G', 'G', 'G', 'G', 'G']
        ]
        self.colors_2 = ['R', 'G']
        self.board_2 = [
            ['R', 'R', 'R'],
            ['R', 'G', 'G'],
            ['R', 'G', 'G']
        ]


    def test_get_connected_tiles(self):
        """
        Tests the get_connected_tiles function for correct output.

        Checks that the function correctly identifies all tiles connected
        to the origin (0, 0) of color 'R'.
        """
        expected_tiles = {(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)}
        actual_tiles = get_connected_tiles(self.board_2, 'R')
        self.assertEqual(expected_tiles, actual_tiles)


    def test_get_largest_connected_color(self):
        """
        Tests the get_largest_connected_color function for correct color selection.

        Determines which color (either 'R' or 'G') has the largest connected
        region starting from the origin and checks that the function returns
        the correct color.
        """
        expected_color = 'G'
        actual_color = get_largest_connected_color(self.board_2, self.colors_2)
        self.assertEqual(expected_color, actual_color)


    def test_flood_fill(self):

        board = [row[:] for row in self.board_1]  # Create a copy of the board
        expected_moves = 2
        actual_moves = flood_fill(board, self.colors_2)
        self.assertEqual(expected_moves, actual_moves)
        expected_board = [
                ['R', 'R', 'R', 'R', 'R', 'R'],
                ['R', 'R', 'R', 'R', 'R', 'R'],
                ['R', 'R', 'R', 'R', 'R', 'R'],
                ['R', 'R', 'R', 'R', 'R', 'R'],
                ['R', 'R', 'R', 'R', 'R', 'R'],
                ['R', 'R', 'R', 'R', 'R', 'R']
            ]
        self.assertEqual(expected_board, board)


if __name__ == "__main__":
    unittest.main()
