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
# import our card class
from .card import Card
# import random to get our random cards
import random


### --- VARIABLES --- ###

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

### --- FUNCTIONS --- ###

def create_deck():
  """
  Creates a new deck of 52 card objects by passing each card suit, card and card value
  into the Card class, then appending it to the deck array.
  """
  # we now create our deck of cards
  deck = []
  # Loop for every type of suit
  for suit in suits:
      # Loop for every type of card in a suit
      for card in cards:
          # Adding card to the deck
          deck.append(Card(suits_values[suit], card, cards_values[card]))

  return deck

def blackjack_start(deck):
  """
  Main blackjack function, each run is one game
  """
  # set our player and dealers cards
  player_cards = []
  dealer_cards = []
  # set our player and dealers scores
  player_score = 0
  dealer_score = 0
  # from here we do our main game loop, we can check if the player
  # cards lentgth is less than 2 and draw until that. 
  while len(player_cards) < 2:
    # deal our player cards and remove them from the deck
    player_card = random.choice(deck)
    player_cards.append(player_card)
    deck.remove(player_card)
    
  print(Card.create_card(player_cards, False))

