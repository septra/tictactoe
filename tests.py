import unittest

from grid import Grid

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



if __name__ == '__main__':
    unittest.main()


