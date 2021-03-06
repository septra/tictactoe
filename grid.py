
class Grid(object):
    """
    A grid object representing the positions of the 'X' and 'O' players
    for any given state.

    Parameters
    ----------

    state : tuple of length 9
        Tuple with values 'X', 'O' or None for 
        positions (a1, a2, a3, b1, b2, b3, c1, c2, c3)

    """

    @staticmethod
    def is_valid_gameplay(grid):
        num_x_plays = sum([1 if n == 'X' else 0 for n in grid.raw_state])
        num_o_plays = sum([1 if n == 'O' else 0 for n in grid.raw_state])

        if 0 <= num_x_plays + num_o_plays <= 9:
            return abs(num_x_plays - num_o_plays) <= 1
        else:
            return False
    
    def __init__(self, state):

        self.a1 = state[0] if state[0] else ' '
        self.b1 = state[1] if state[1] else ' '
        self.c1 = state[2] if state[2] else ' '

        self.a2 = state[3] if state[3] else ' '
        self.b2 = state[4] if state[4] else ' '
        self.c2 = state[5] if state[5] else ' '

        self.a3 = state[6] if state[6] else ' '
        self.b3 = state[7] if state[7] else ' '
        self.c3 = state[8] if state[8] else ' '

        self.raw_state = state


    def __repr__(self):

        row1 = '1.\t{:^3}|{:^3}|{:^3}'.format(self.a1, self.b1, self.c1)
        row2 = '2.\t{:^3}|{:^3}|{:^3}'.format(self.a2, self.b2, self.c2)
        row3 = '3.\t{:^3}|{:^3}|{:^3}'.format(self.a3, self.b3, self.c3)
        footer = ' \t{:^3} {:^3} {:^3}'.format('a', 'b', 'c')

        output = '\n' + '\n'.join([row3, row2, row1]) + '\n\n' + footer

        return output


    def __eq__(self, other):

        return (self.a1 == other.a1 and 
                self.b1 == other.b1 and
                self.c1 == other.c1 and

                self.a2 == other.a2 and
                self.b2 == other.b2 and
                self.c2 == other.c2 and

                self.a3 == other.a3 and
                self.b3 == other.b3 and
                self.c3 == other.c3)
