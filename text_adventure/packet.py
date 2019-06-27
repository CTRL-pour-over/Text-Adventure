# experimental packet class, super unfinished.
class decision_packet(object):
    def __init__(self, arg_move, arg_items, arg_health, arg_attack, arg_input):
        self.move = -1
        self.items = -1
        self.health = -1
        self.attack = -1
        self.input = -1

    def render_status(self):
        print self.move
        print self.items
        print self.health
        print self.attack
        print self.input