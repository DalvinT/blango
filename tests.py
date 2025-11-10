import unittest
from boggle_solver import Boggle


class TestBoggleSolver(unittest.TestCase):
    def test_empty_dictionary_returns_empty_solution(self):
        grid = [
            ["T", "W", "Y", "R"],
            ["E", "N", "P", "H"],
            ["G", "Z", "QU", "R"],
            ["O", "N", "T", "A"]
        ]
        dictionary = []
        game = Boggle(grid, dictionary)
        self.assertEqual(game.get_solution(), [])

    def test_getSolution_alias(self):
        grid = [["A"]]
        dictionary = ["A"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), [])


if __name__ == "__main__":
    unittest.main()
