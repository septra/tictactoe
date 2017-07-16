class Player(object):

    def __init__(self, name, xo):
        self.name = name
        self.xo = xo

    def __repr__(self):
        return '{} ({})'.format(self.name, self.xo)
