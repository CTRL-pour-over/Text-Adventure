from termcolor import colored
from os import system, name
from time import sleep
from enum import Enum
print colored('\n\nHello Family. This is a very special game.\t', 'magenta'), colored('Version .01\n\n\n', 'cyan')

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
        

class GameManager(object):
    class RoomID(Enum):
        _captains_quarters = 1
        _lower_deck = 2
        _outside_deck = 3

    game_over = False
    def __init__(self):
        self.game_over = False
        # instantiated a Player object
        self.player_1 = Player("Shemar", 100.0, 1.0, 99.9, self.RoomID._outside_deck) # player current room needs to be updated! 
        
        # instantiate ALL rooms
        self.captains_quarters = Room("This is the captains_quarters Do you walk out the door or na?", "captains_quarters", {'baby':'item'}, ['walk', 'door', 'go'],[], True, ['outside deck'], True)
        self.outside_deck = Room("Wecome to the Outside Deck. The captains quarters is behind a door visible to you. There is also a stair well leading to the ammo room.", "Outside Deck", {'cannon':'item'}, ['captain', 'back', 'downstairs'], ['captains quarters', 'lower deck'], False, [], False)
        self.lower_deck = Room("It smells dank down here. There are scorched whisky barrels for the sailors, along with a pile of cannon balls. What do you do?", "Lower Deck", {'cannon ball' : 'item'}, ['upstairs', 'cannon', 'ball', 'grab', 'carry', 'back'], ['outside deck'], False, [], False)
        # Give the player a current location.
        print "player_1, captains_quarters, outside_deck, lower_deck have been instantiated by the GameManager."
    #Clears the terminal window.
    def clear(self):
        if name == 'nt': 
            _ = system('cls') 
        else: 
            _ = system('clear')

    #Explains the situation of the game, Renders text, display stats and other important imformation.
    def render_status(self):
        self.player_1.render_status()

        if self.player_1.current_room == self.RoomID._captains_quarters:
            self.captains_quarters.render_status()
        elif self.player_1.current_room == self.RoomID._outside_deck:
            self.outside_deck.render_status()
        elif self.player_1.current_room == self.RoomID._lower_deck:
            self.lower_deck.render_status()


    # Catches the raw_input from Player, verifies input is good, does not run intense checks. UwU 
    def player_input(self):   
        temp_keywords = self.get_current_room_keywords()     
        
        print temp_keywords

        choice = raw_input("What do you want to do? >>>   ").lower().split()
        print "choice: %s" % choice
        for thing in temp_keywords:
            if thing in choice:
# loop will scan the full list. instead of having 'good', 'nope', 'nope', lets just plug in a function
# if only i could figure out what function lol
                print "success"
                 
                return "We moved %r" % choice 
            else:
                print "nope"
        return "NONE"

    def move_player(self, arg_destination_room_id, arg_previous_room_id):    
        #Paranoid check to not waste our time 
        if self.player_1.current_room == arg_destination_room_id:  
            print "You are already here."
            return
        #region player_present = False if-statements. DONE.
        #Find the room we are currently in, set player_present to false because we are leaving. 
        if self.player_1.current_room == self.RoomID._captains_quarters:
            #Change variables
            self.captains_quarters.player_present = False
        elif self.player_1.current_room == self.RoomID._lower_deck:
            #Change variables
            self.lower_deck.player_present = False
        elif self.player_1.current_room == self.RoomID._outside_deck:
            #Change variables
            self.outside_deck.player_present = False
        # make sure we dont run code we dont have to.
        else: 
            print "ERROR: move_player..."
            return       
        #endregion        
        #region player_present = True for Room we are going to.DONE.
        if arg_destination_room_id == self.RoomID._captains_quarters:
            #Change variables
            self.captains_quarters.player_present = True
            self.captains_quarters.has_been_visited = True
            self.player_1.current_room = self.RoomID._captains_quarters
        elif arg_destination_room_id == self.RoomID._lower_deck:
            #Change variables
            self.lower_deck.player_present = True
            self.lower_deck.has_been_visited = True
            self.player_1.current_room = self.RoomID._lower_deck
        elif arg_destination_room_id == self.RoomID._outside_deck:
            #Change variables
            self.outside_deck.player_present = True
            self.outside_deck.has_been_visited= True
            self.player_1.current_room = self.RoomID._outside_deck
        else:
            print "really should never see this."
            return
        #endregion
        print self.player_1.current_room

    

    # Goes through previously stored player input, checks input against options. Determines outcome. 
    def parse_input(self, arg_player_input):
        print arg_player_input
        
    # Visual response to input. 
    def give_feedback(self):
        pass
    # Reacts to input and prepares all game objects for next round of GameLoop.
    def react_to_input(self,arg_choice ):

        print arg_choice
        

        
    def get_current_room_keywords(self):
        #If statement or loop to mind the current room 
        if self.player_1.current_room == self.RoomID._captains_quarters:
            print "get_current_room_keywords: "
            return self.captains_quarters.keywords
        elif self.player_1.current_room == self.RoomID._outside_deck:
            print "get_current_room_keywords: "
            return self.outside_deck.keywords
        elif self.player_1.current_room == self.RoomID._lower_deck:
            print "get_current_room_keywords: "
            return self.lower_deck.keywords
        else:
            print "really should never see this."
            return ["BrokenList"]
    # gets the adacient rooms so we can move the player smart style
    def get_current_room_adacient_rooms(self):
        if self.captains_quarters.adacient_rooms == self.RoomID._captains_quarters:
            print "GetCurrrentRoomAdacientRooms: "
            return self.captains_quarters.adacient_rooms
        elif self.outside_deck.adacient_rooms == self.RoomID._outside_deck:
            print "GetCurrrentRoomAdacientRooms: "
            return self.outside_deck.adacient_rooms
        elif self.lower_deck.adacient_rooms == self.RoomID._lower_deck:
            print "GetCurrrentRoomAdacientRooms: "
            return self.outside_deck.adacient_rooms


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

gm = GameManager()
while gm.game_over is False:
    sleep(.5)
    gm.clear()
    sleep(.4)
    gm.render_status()
    #Received and verified input is a good choice.
    sleep(.3)
    players_choice = gm.player_input()
    #Update the game accordingly.
    sleep(.3)
    gm.react_to_input(players_choice)
    sleep(.2)
    gm.parse_input(players_choice)
    sleep(.5)
