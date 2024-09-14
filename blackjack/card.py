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


  def create_card(self, cards, hidden):
    # Function to print cards

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
    for card in cards:
      c = c + ""



