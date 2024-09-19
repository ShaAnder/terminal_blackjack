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
  Class to create our card.
  """

  def __init__(self, suit, value, card_value):
    #suit of the card we want to make
    self.suit = suit
    # the valeu of the card (1-10, A, K)
    self.value = value
    # score of the card 
    self.card_value = card_value

  # added create card function to card class because it's logically to
  # do with card creation
  def create_card(card):
    """
    Function to create our card, takes the card's input and using our
    pieces generates cards to add to our deck.
    """
    # Card pieces - using string formatting we align and format
    # each variable space to 2 spaces, to account for single digita
    top = "┌───────────┐"
    bottom = "└───────────┘"
    base = "│           │"
    left_value_format = "│ {:<2}        │"  # Left-align with width 2
    right_value_format = "│        {:>2} │"  # Right-align with width 2
    suit = "│     {}     │"

    # Create our card template of 11 entries
    card_rows = [top, base, base, base, base, base, base, base, bottom]
    # Apply string formatting to the row based on the card value
    card_rows[1] = left_value_format.format(card.value)
    card_rows[7] = right_value_format.format(card.value) 
    # Format the suit
    card_rows[4] = suit.format(card.suit)
    # If hidden (dealer card) return the hidden card from layout
    return "\n".join(card_rows)



