# this is the file that needs to be run in order to start up the game

from os import system, name
from time import sleep
from enum import Enum
from text_adventure.manager import GameManager

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