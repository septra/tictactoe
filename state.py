from grid import Grid

class State(object):

    def __init__(self, player, grid_state):

        self.player = player
        self.grid_state = grid_state


    def check_win(self):

        grid_state = self.grid_state

        if (
            # Check rows for win
            ' ' != grid_state.a3 == grid_state.b3 == grid_state.c3 or
            ' ' != grid_state.a2 == grid_state.b2 == grid_state.c2 or
            ' ' != grid_state.a1 == grid_state.b1 == grid_state.c1 or

            # Check columns for win
            ' ' != grid_state.a3 == grid_state.a2 == grid_state.a1 or
            ' ' != grid_state.b3 == grid_state.b2 == grid_state.b1 or
            ' ' != grid_state.c3 == grid_state.c2 == grid_state.c1 or

            # Check diagonals for win
            ' ' != grid_state.a1 == grid_state.b2 == grid_state.c3 or
            ' ' != grid_state.a3 == grid_state.b2 == grid_state.c1):
            return True

        else:
            return False

    def is_final(self):

        if self.check_win():
            return True
        elif None not in set(self.grid_state.raw_state):
            return True
        else:
            return False

