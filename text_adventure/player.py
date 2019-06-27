from termcolor import colored
# initialize player and render status
class Player(object):
    name = "Thomas"
    health = 100.00
    min_damage = 1.0
    max_damage = 999.9

    def __init__(self, arg_name, arg_health, arg_min_damage, arg_max_damage, arg_current_room):
        # setting the variable to the argument
        self.name = arg_name
        # setting the variable to the argument
        self.health = arg_health
        # setting the variable to the argument
        self.min_damage = 0.0
        # setting the variable to the argument
        self.max_damage = arg_max_damage
        self.current_room = arg_current_room # room id

    def render_status(self):
        print "<<============================ Displaying Player Stats ============================>>\n"
        print colored("Player Name: " + self.name, 'yellow')
        print colored("\nPlayer Health: " + str(self.health), 'green')
        print colored("\nPlayer Min Damage: " + str(self.min_damage), 'blue')
        print colored("\nPlayer Max Damage: " + str(self.max_damage), 'red')
        print colored("\nPlayer Current Room: " + str(self.current_room), 'magenta')
        print "\n"