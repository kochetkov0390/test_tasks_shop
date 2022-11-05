import unittest

import task1_game as game


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        game.TIMESTAMPS_COUNT = 100
        self.game_stamps = game.generate_game()
        self.start_offset = 0
        self.end_offset = self.game_stamps[-1]['offset']
        self.end_score_home = self.game_stamps[-1]['score']['home']
        self.end_score_away = self.game_stamps[-1]['score']['away']
        self.fake_game_stamps = [game.INITIAL_STAMP,
                                 {
                                     "offset": 1,
                                     "score": {
                                         "home": 1,
                                         "away": 1
                                     }
                                 },
                                 {
                                     "offset": 2,
                                     "score": {
                                         "home": 2,
                                         "away": 2
                                     }
                                 },
                                 {
                                     "offset": 3,
                                     "score": {
                                         "home": 3,
                                         "away": 3
                                     }
                                 }
                                 ]

    def test_get_score_offset_less_than_range(self):
        self.assertEqual(game.get_score(self.game_stamps, -1), (0, 0))

    def test_get_score_offset_more_than_range(self):
        self.assertEqual(game.get_score(self.game_stamps, self.end_offset + 1),
                         (self.end_score_home, self.end_score_away))

    def test_get_score_offset_first_element(self):
        self.assertEqual(game.get_score(self.game_stamps, self.start_offset), (0, 0))

    def test_get_score_offset_last_element(self):
        self.assertEqual(game.get_score(self.game_stamps, self.end_offset),
                         (self.end_score_home, self.end_score_away))

    def test_get_score_offset_in_range(self):
        self.assertEqual(game.get_score(self.fake_game_stamps, 2), (2, 2))


if __name__ == "__main__":
    unittest.main()
