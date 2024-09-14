"""
Module to define the logic
Should run after table class has been initialized
then we get terminal_paint class to paint to the screen
"""

### --- IMPORTS --- ###

# we want sleep to create a wait function, to give the user the illusion of 
# the cpu waiting to take their turn / to prevent multiple game logic actions
# triggering early
from time import sleep


# import our card class to build our cards
from card import Card
from layout import hidden_card


### --- VARIABLES --- ###

# our main game function
def blackjack_start():
  pass