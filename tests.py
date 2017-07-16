import unittest

from grid import Grid
from player import Player
from state import State

class GridTest(unittest.TestCase):

    def setUp(self):

        self.raw_state_1 = ('X', None, None, 'O', 'X', None, 'O', 'O', 'X')
        self.raw_state_2 = ('X', None, None, 'O', 'X', None, 'O', 'O', 'X')
        self.raw_state_3 = ('O', None, None, 'O', 'O',  'X', 'X', 'X', 'O')

        self.grid_1 = Grid(self.raw_state_1)
        self.grid_2 = Grid(self.raw_state_2)
        self.grid_3 = Grid(self.raw_state_3)


    def test_grid_equality(self):

        self.assertEqual(self.grid_1, self.grid_2)

        self.assertNotEqual(self.grid_1, self.grid_3)
        self.assertNotEqual(self.grid_2, self.grid_3)


    def test_grid_display(self):

        display_1 = "\n O | O | X \n O | X |   \n X |   |   "
        display_2 = "\n O | O | X \n O | X |   \n X |   |   "
        display_3 = "\n X | X | O \n O | O | X \n O |   |   "

        self.assertEqual(str(self.grid_1), display_1)
        self.assertEqual(str(self.grid_2), display_2)
        self.assertEqual(str(self.grid_3), display_3)


class PlayerTest(unittest.TestCase):

    def test_display_output(self):
        player_1 = Player('Chandler Bing', 'X')
        player_2 = Player('Ross Gellar', 'O')

        chandler_output = 'Chandler Bing (X)'
        ross_output = 'Ross Gellar (O)'

        self.assertEqual(str(player_1), chandler_output)
        self.assertEqual(str(player_2), ross_output)


class StateTest(unittest.TestCase):

    def setUp(self):

        self.player_1 = Player('Ross Gellar',   'X')
        self.player_2 = Player('Chandler Bing', 'O')

        raw_state_1 = ('X', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'O') # n'O' win
        raw_state_2 = ('X', None, 'O', 'X', 'O', 'X', 'O', None, 'O') # 'O' win
        raw_state_3 = (None, None, 'O', None, 'X', None, None, None, 'X')

        self.state_1 = State(self.player_1, Grid(raw_state_1))
        self.state_2 = State(self.player_2, Grid(raw_state_2))
        self.state_3 = State(self.player_1, Grid(raw_state_3))


    def test_state_win(self):

        self.assertEqual(self.state_1.check_win(), False)
        self.assertEqual(self.state_2.check_win(), True)
        self.assertEqual(self.state_3.check_win(), False)


    def test_state_is_final(self):

        self.assertEqual(self.state_1.is_final(), True)
        self.assertEqual(self.state_2.is_final(), True)
        self.assertEqual(self.state_3.is_final(), False)

    


if __name__ == '__main__':
    unittest.main()


