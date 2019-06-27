from enum import Enum
from os import system, name
from text_adventure.player import Player
from text_adventure.room import Room
# this is gm. this is where all the magic happens
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
                 
                return "We movedgit" 
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
