from unittest import TestCase

class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, number):
        self.rolls.append(number)

    def strike_bonus(self, row_index):
        return self.rolls[row_index + 1] + self.rolls[row_index + 2]

    def spare_bonus(self, row_index):
        return self.rolls[row_index+ 2]

    def frame_score(self, row_index):
        return self.rolls[row_index] + self.rolls[row_index+ 1]


    def score(self):
        row_index= 0
        score = 0

        for _ in range(10):
            if self.rolls[row_index] == 10:
                score += 10 + self.strike_bonus(row_index)
                row_index+= 1
            elif self.frame_score(row_index) == 10:
                score += 10 + self.spare_bonus(row_index)
                row_index+= 2
            else:
                score += self.frame_score(row_index)
                row_index+= 2

        return score

class TestBowlingGame(TestCase):

    def setUp(self):
        self.game = Game()

    def test_all_zeros(self):

        for _ in range(20):
            self.game.roll(0)

        self.assertEqual(self.game.score(), 0)

    def test_all_ones(self):

        for _ in range(20):
            self.game.roll(1)

        self.assertEqual(self.game.score(), 20)

    def test_spare(self):

        self.game.roll(4)
        self.game.roll(6)

        for _ in range(18):
            self.game.roll(1)

        self.assertEqual(self.game.score(), 29)

    def test_strike(self):

        self.game.roll(10)

        for _ in range(18):
            self.game.roll(1)

        self.assertEqual(self.game.score(), 30)

    def test_perfect_game(self):

        for _ in range(20):
            self.game.roll(10)

        self.assertEqual(self.game.score(), 300)
