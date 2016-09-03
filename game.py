import random

class Game(object):
    def __init__(self):
        self.xs = 'X'
        self.os = 'O'
        self.grid = [[None, None, None],
                     [None, None, None],
                     [None, None, None]]
        self.turn = random.choice([self.xs, self.os])

        self.over = False

        print("It's %s's turn to begin" % self.turn)

    def play(self, row, col):

        if self.over is True:
           print("Game is Over! Start a new one.")
           return None

        # To convert into 0 based index
        row -= 1
        col -= 1

        if self.grid[row][col]:
            raise AssignmentError("Position already taken!")
        else:
            self.grid[row][col] = self.turn

            self.check()

            self.turn = self.xs if self.turn == self.os else self.os

        print(self)


    def check(self):
        if None != self.grid[0][0] == self.grid[0][1] == self.grid[0][2] or \
           None != self.grid[1][0] == self.grid[1][1] == self.grid[1][2] or \
           None != self.grid[2][0] == self.grid[2][1] == self.grid[2][2] or \
           None != self.grid[0][0] == self.grid[1][0] == self.grid[2][0] or \
           None != self.grid[0][1] == self.grid[1][1] == self.grid[2][1] or \
           None != self.grid[0][2] == self.grid[1][2] == self.grid[2][2] or \
           None != self.grid[0][0] == self.grid[1][1] == self.grid[2][2] or \
           None != self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
               self.over = True
               print("Game Over! %s Wins." % self.turn)


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


class AssignmentError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message




