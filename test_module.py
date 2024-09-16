# test_module.py

import unittest
from RPS_game import play, quincy, abigail, kriss, mrugesh
from RPS import player

class TestRPS(unittest.TestCase):
    def test_player_vs_quincy(self):
        result = play(player, quincy, 1000)
        self.assertGreaterEqual(result[0], 600, "The player should win at least 60% of the games against Quincy")

    def test_player_vs_abigail(self):
        result = play(player, abigail, 1000)
        self.assertGreaterEqual(result[0], 600, "The player should win at least 60% of the games against Abigail")

    def test_player_vs_kriss(self):
        result = play(player, kriss, 1000)
        self.assertGreaterEqual(result[0], 600, "The player should win at least 60% of the games against Kriss")

    def test_player_vs_mrugesh(self):
        result = play(player, mrugesh, 1000)
        self.assertGreaterEqual(result[0], 600, "The player should win at least 60% of the games against Mrugesh")

if __name__ == "__main__":
    unittest.main()
