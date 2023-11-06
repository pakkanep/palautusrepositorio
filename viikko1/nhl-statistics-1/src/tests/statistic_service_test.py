import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class Test_Statistics_Service(unittest.TestCase):
    def setUp(self):
        self.statistics_reader = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        pass

    def test_team(self):
        pass

    def test_top(self):
        result = self.statistics_reader.top(1)
        top_player = (f"Lemieux EDM {45} + {54} = {99}")
        self.assertEqual(str(result), str(top_player))