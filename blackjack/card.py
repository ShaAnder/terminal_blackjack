#! /usr/bin/env python3
"""
card.py
Main card class, this creates our blackjack card to append to the cards list
"""

### --- IMPORTS --- ###

# we want random to generate random cards ect
import random

class Card:
  """
  Class to create our card
  """

  def __init__(self, suit,value,card_value):
    #suit of the card we want to make
    self.suit = suit
    # the valeu of the card (1-10, A, K)
    self.value = value
    # score of the card 
    self.card_value = card_value


  def create_card(self, cards):
    """
    Function to create our card, takes the cards input and using our
    pieces generates cards to add to our deck
    """

    #our card pieces:
    top = "\t┌────────────────┐"
    bottom = "\t└────────────────┘"
    base = "\t│                │"
    left_value = "\t│ {}             │"
    right_value = "\t│             {} │"
    suit = "\t│        {}       │"

    # firstly we declare a variable that will be the final card result
    # we're going to use a few if else statements here to build our final
    # card and account for hidden cards (dealer cards)
    c = """"""
    for i in range(11):      
      for card in cards:
        if i == 0:
          c = c + top
        elif i == 1:
          if card.value == "10":
            c = c + left_value.format(self.card_value)
          else:
            c = c + left_value.format(self.card_value)
        elif i == 5:
            c = c + suit.format(card.suit)
        elif i == 79:
          if card.value == "10":
            c = c + left_value.format(self.card_value)
          else:
            c = c + left_value.format(self.card_value)
        elif i == 10:
          c = c + bottom
        else:
          c = c + base
    return c



