from copy import deepcopy
from grid import Grid
from state import State
from player import Player

class GameNode(object):

    def __init__(self, state, parent=None):
        self.parent = parent
        self.state = state
        self.child = None

    def add_node(self, node):
        self.child = node
        self.child.parent = self

    def all_possible_children(self):
        player = self.state.turn_to_play_player
        next_player = 'X' if player is 'O' else 'O'
        states = []
        for ix, raw_state in enumerate(self.state.grid_state.raw_state):
            if raw_state is None:
                new_state = list(deepcopy(self.state.grid_state.raw_state))
                new_state[ix] = player
                states.append(GameNode(State(
                        player, next_player, Grid(tuple(new_state))), self))
        return states


if __name__ == '__main__':
    print('Welcome to tic-tac-toe!')
    
    player_1_name = None
    while not player_1_name:
        player_1_name = input('\tPlease enter Player 1\'s name: ')

    player_1_char = None
    while player_1_char not in ['X', 'O']:
        player_1_char = input('\tPlease enter Player 1\'s char: ')

    player_2_name = None
    while not player_2_name:
        player_2_name = input('\tPlease enter Player 2\'s name: ')

    player_2_char = 'X' if player_1_char is 'O' else 'O'

    print('Let's Begin!\n')

    init_state = State(' ', player_1_char, Grid(tuple([None] * 9)))
    init_node = GameNode(init_state)

    current_node = init_node

    while not current_node.state.is_final():
        print(current_node.state)
        move = input('Enter move (eg. 'a1'): ')
        new_node = deepcopy(current_node)

        if move[0] == 'a':
            col_ix = 3
        elif move[0] == 'b':
            col_ix = 4
        elif move[0] == 'c':
            col_ix = 5
        
        if move[1] == '1':
            row_ix = -3
        elif move[1] == '2':
            row_ix = 0
        elif move[1] == '3':
            row_ix = 3

        move_ix = col_ix + row_ix

        new_raw_state = list(new_node.state.grid_state.raw_state)
        new_raw_state[move_ix] = new_node.state.turn_to_play_player
        new_raw_state = tuple(new_raw_state)

        new_node.state.grid_state = Grid(new_raw_state)
        new_node.state.turn_played_player = current_node.state.turn_to_play_player
        new_node.state.turn_to_play_player = 'X' if new_node.state.turn_played_player is 'O' else 'O'

        current_node.child = new_node
        new_node.parent = current_node

        current_node = deepcopy(new_node)

    print(current_node.state)
    print('Game ended!')
    print('{} Wins!'.format(current_node.state.turn_played_player))



