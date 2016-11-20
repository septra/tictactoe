import numpy as np

# Any position can be filled by 'X', 'O' or None.

players = [None, 'X', 'O']

allStates = [
        [(a, b, c),
         (d, e, f),
         (g, h, i)]
         for a in players
         for b in players
         for c in players
         for d in players
         for e in players
         for f in players
         for g in players
         for h in players
         for i in players
         ]

class State(object):
    def __init__(self, state, turn):
        self.state = np.matrix(state)
        self.turn = turn
        self.over_, self.winner_ = self.checkWin(self.state)

    def checkWin(self, state):
        """Returns (Boolean, Player)"""

        #check rows
        for row in state:
            if len(set(row.tolist()[0])) == 1 and row.tolist()[0][0] is not None:
                print "row"
                return True, row[0]

        #check columns
        for column in state.T:
            if len(set(column.tolist()[0])) == 1 and column.tolist()[0][0] is not None:
                print "column"
                return True, column[0]

        #check diagonals
        diagonal1 = np.diag(self.state).tolist()
        diagonal2 = np.diag(np.fliplr(self.state)).tolist()

        if len(set(diagonal1)) == 1 and diagonal1[0] is not None:
            print "diag1"
            return True, diagonal1[0]
        if len(set(diagonal2)) == 1 and diagonal2[0] is not None:
            print "diag2"
            return True, diagonal2[0]

        return False, None

    def nextStates(self):
        holder = []

        for rowNum, row in enumerate(self.state.tolist()):
            for colNum, position in enumerate(row):
                if position is None:
                    newState = self.state.copy().tolist()
                    newState[rowNum][colNum] = self.turn
                    newTurn = 'X' if self.turn == 'O' else 'O'
                    #print "going in"
                    holder.append(State(newState, newTurn))


        return holder

    def __repr__(self):
        return str(np.matrix(self.state)) + "Player: %s \n" % self.turn

