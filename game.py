import random

class Game(object):
    def __init__(self):
        self.xs = 'X'
        self.os = 'O'
        self.grid = [[None, None, None],
                     [None, None, None],
                     [None, None, None]]
        self.turn = random.choice([self.xs, self.os])

        print("It's %s's turn to begin" % self.turn)

    def play(self, row, col):
        self.grid[row][col] = self.turn
        self.turn = self.xs if self.turn == self.os else self.os
        print(self)


    def __str__(self):
        output = []
        for row in self.grid:
            output.append("{:^3}|{:^3}|{:^3}".format( 
                    *[piece 
                       if piece is not None 
                       else ' ' 
                       for piece in row]))

        return "\n".join(output)

    def __repr__(self):
        output = []
        for row in self.grid:
            output.append("{:^3}|{:^3}|{:^3}".format( 
                    *[piece     
                       if piece is not None 
                       else ' ' 
                       for piece in row])) 

        return "\n".join(output)





