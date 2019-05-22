from termcolor import colored
from os import system, name
from time import sleep
from enum import Enum
print colored('\n\nHello Family. This is a very special game.\t', 'magenta'), colored('Version .01\n\n\n', 'cyan')

class Room(object):
    playerPresent = False

    def __init__(self, arg_description, arg_name, arg_itemsContained, arg_keyWords, arg_events, arg_hasBeenVisited, arg_adacientRooms, arg_playerPresent):
        self.description = arg_description
        self.name = arg_name
        self.itemsContained = arg_itemsContained
        self.keyWords = arg_keyWords
        self.events = arg_events
        self.hasBeenVisited = arg_hasBeenVisited
        self.adacientRooms = arg_adacientRooms
        self.playerPresent = arg_playerPresent

    def Render_Status(self):
        print "<<============================ Displaying Room Stats ============================>>\n"
        print 'Room Description:', colored(self.description, 'yellow')
        print '\nRoom Name:', colored(self.name, 'red')
        print '\nRoom Items:', colored(self.itemsContained, 'magenta')
        print '\nRoom Keywords List:', colored(self.keyWords, 'green')
        print '\nRoom Events:', colored(self.events, 'yellow')
        print '\nHas Been Visited:', colored(self.hasBeenVisited, 'red')
        print '\nAdacient Rooms: ', colored(self.adacientRooms, 'magenta')
        print '\nPlayer Present:', colored(self.playerPresent, 'green')

class Player(object):
    name = "Thomas"
    health = 100.00
    min_damage = 1.0
    max_damage = 999.9

    def __init__(self, arg_name, arg_health, arg_min_damage, arg_max_damage, arg_current_Room):
        # setting the variable to the argument
        self.name = arg_name
        # setting the variable to the argument
        self.health = arg_health
        # setting the variable to the argument
        self.min_damage = 0.0
        # setting the variable to the argument
        self.max_damage = arg_max_damage
        self.current_Room = arg_current_Room # room id

    def Render_Status(self):
        print "<<============================ Displaying Player Stats ============================>>\n"
        print colored("Player Name: " + self.name, 'yellow')
        print colored("\nPlayer Health: " + str(self.health), 'green')
        print colored("\nPlayer Min Damage: " + str(self.min_damage), 'blue')
        print colored("\nPlayer Max Damage: " + str(self.max_damage), 'red')
        print colored("\nPlayer Current Room: " + str(self.current_Room), 'magenta')
        print "\n"
        



class GameManager(object):
    class RoomID(Enum):
        _CaptainsQuarters = 1
        _LowerDeck = 2
        _OutsideDeck = 3

    game_over = False
    def __init__(self):
        self.game_over = False
        # instantiated a Player object
        self.player_1 = Player("Shemar", 100.0, 1.0, 99.9, self.RoomID._OutsideDeck) # player current room needs to be updated! 
        
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
    def Render_Status(self):
        self.player_1.Render_Status()

        if self.player_1.current_Room == self.RoomID._CaptainsQuarters:
            self.captains_quarters.Render_Status()
        elif self.player_1.current_Room == self.RoomID._OutsideDeck:
            self.outside_deck.Render_Status()
        elif self.player_1.current_Room == self.RoomID._LowerDeck:
            self.lower_deck.Render_Status()


    # Catches the raw_input from Player, verifies input is good, does not run intense checks. UwU 
    def Player_Input(self):   
        tempKeywords = self.GetCurrentRoomKeywords()     
        
        print tempKeywords

        choice = raw_input("What do you want to do? >>>   ").lower().split()
        print "choice: %s" % choice
        for thing in tempKeywords:
            if thing in choice:
# loop will scan the full list. instead of having 'good', 'nope', 'nope', lets just plug in a function
# if only i could figure out what function lol
                print "success"
                 
                return "We moved %r" % choice 
            else:
                print "nope"
        return "NONE"

    def Move_Player(arg_DestinationRoomId, arg_PreviousRoomId):    
        #Paranoid check to not waste our time 
        if self.player_1.current_Room == arg_DestinationRoomId:  
            print "You are already here."
            return
        #region playerPresent = False if-statements. DONE.
        #Find the room we are currently in, set playerPresent to false because we are leaving. 
        if self.player_1.current_Room == self.RoomID._CaptainsQuarters:
            #Change variables
            self.captains_quarters.playerPresent = False
        elif self.player_1.current_Room == self.RoomID._LowerDeck:
            #Change variables
            self.lower_deck.playerPresent = False
        elif self.player_1.current_Room == self.RoomID._OutsideDeck:
            #Change variables
            self.outside_deck.playerPresent = False
        # make sure we dont run code we dont have to.
        else: 
            print "ERROR: Move_Player..."
            return
        
        #endregion

        
        #region playerPresent = True for Room we are going to.DONE.
        if arg_DestinationRoomId == self.RoomID._CaptainsQuarters:
            #Change variables
            self.captains_quarters.playerPresent = True
            self.captains_quarters.hasBeenVisited = True
            self.player_1.current_Room = self.RoomID._CaptainsQuarters
        elif arg_DestinationRoomId == self.RoomID._LowerDeck:
            #Change variables
            self.lower_deck.playerPresent = True
            self.lower_deck.hasBeenVisited = True
            self.player_1.current_Room = self.RoomID._LowerDeck
        elif arg_DestinationRoomId == self.RoomID._OutsideDeck:
            #Change variables
            self.outside_deck.playerPresent = True
            self.outside_deck.hasBeenVisited= True
            self.player_1.current_Room = self.RoomID._OutsideDeck
        else:
            print "really should never see this."
            return
        #endregion
        print self.player_1.current_Room

    

    # Goes through previously stored player input, checks input against options. Determines outcome. 
    def Parse_Input(self, arg_playerinput):
        print arg_playerinput
        
    # Visual response to input. 
    def Give_Feedback(self):
        pass
    # Reacts to input and prepares all game objects for next round of GameLoop.
    def React_to_Input(self,arg_choice ):

        print arg_choice
        

        
    def GetCurrentRoomKeywords(self):
        #If statement or loop to mind the current room 
        if self.player_1.current_Room == self.RoomID._CaptainsQuarters:
            print "GetCurrentRoomKeywords: "
            return self.captains_quarters.keyWords
        elif self.player_1.current_Room == self.RoomID._OutsideDeck:
            print "GetCurrentRoomKeywords: "
            return self.outside_deck.keyWords
        elif self.player_1.current_Room == self.RoomID._LowerDeck:
            print "GetCurrentRoomKeywords: "
            return self.lower_deck.keyWords
        else:
            print "really should never see this."
            return ["BrokenList"]
    # gets the adacient rooms so we can move the player smart style
    def GetCurrentRoomAdacientRooms(self):
        if self.captains_quarters.adacientRooms == self.RoomID._CaptainsQuarters:
            print "GetCurrrentRoomAdacientRooms: "
            return self.captains_quarters.adacientRooms
        elif self.outside_deck.adacientRooms == self.RoomID._OutsideDeck:
            print "GetCurrrentRoomAdacientRooms: "
            return self.outside_deck.adacientRooms
        elif self.lower_deck.adacientRooms == self.RoomID._LowerDeck:
            print "GetCurrrentRoomAdacientRooms: "
            return self.outside_deck.adacientRooms


class DecisionPacket(object):
    self.move = arg_move
    self.items = arg_items
    self.health = arg_health
    self.attack = arg_attack
    self.input = arg_input


gm = GameManager()
while gm.game_over is False:
    sleep(.5)
    gm.clear()
    sleep(.4)
    gm.Render_Status()
    #Received and verified input is a good choice.
    sleep(.3)
    playersChoice = gm.Player_Input()
    #Update the game accordingly.
    sleep(.3)
    gm.React_to_Input(playersChoice)
    sleep(.2)
    gm.Parse_Input(playersChoice)
    sleep(.5)