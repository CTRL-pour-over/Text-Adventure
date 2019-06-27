from termcolor import colored
# initialize rooms and render status
class Room(object):
    player_present = False

    def __init__(self, arg_description, arg_name, arg_items_contained, arg_keywords, arg_events, arg_has_been_visited, arg_adacient_rooms, arg_player_present):
        self.description = arg_description
        self.name = arg_name
        self.items_contained = arg_items_contained
        self.keywords = arg_keywords
        self.events = arg_events
        self.has_been_visited = arg_has_been_visited
        self.adacient_rooms = arg_adacient_rooms
        self.player_present = arg_player_present

    def render_status(self):
        print "<<============================ Displaying Room Stats ============================>>\n"
        print 'Room Description:', colored(self.description, 'yellow')
        print '\nRoom Name:', colored(self.name, 'red')
        print '\nRoom Items:', colored(self.items_contained, 'magenta')
        print '\nRoom Keywords List:', colored(self.keywords, 'green')
        print '\nRoom Events:', colored(self.events, 'yellow')
        print '\nHas Been Visited:', colored(self.has_been_visited, 'red')
        print '\nAdacient Rooms: ', colored(self.adacient_rooms, 'magenta')
        print '\nPlayer Present:', colored(self.player_present, 'green')