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
from .terminal_paint import *


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


def draw_card(deck, player_card_data, player_cards, hidden):
  """
  Draws A card, converts it and then appends the card data and card to
  the users hand.

  Args:
      deck (list): list (deck of cars)
      player_card_data (list): the card data of the player in question
      player_cards (list): The cards of the player in question
      hidden (Bool): Hidden T/F for card, if False Card face up, else hidden
  """
  # draw a card from the deck
  card = random.choice(deck)
  deck.remove(card)
  # convert the card to a readable format
  converted_card = Card.create_card(card, hidden)
  # append to both player card and player card data
  player_card_data.append(card)
  player_cards.append(converted_card)


def display_cards(cards):
  """
  Takes the card array and splits it into lines for
  printing side by side in the terminal

  Args:
      cards (list): the player or dealer card list for displaying cards
  """
  # get the lines for each card in the card list
  card_lines = [card.splitlines() for card in cards]
  max_lines = max(len(lines) for lines in card_lines)

  for i in range(max_lines):
    line_to_print = ""
    for lines in card_lines:
      line = lines[i] if i < len(lines) else " " * len(lines[0])
      line_to_print += line + " "
    print(line_to_print)

def blackjack_start(deck):
  """
  Main blackjack function, each run is one game
  """

  ########################
  #Step 1 Draw our Intro#
  ########################
  intro()
  instructions()

  # set our player and dealers cards
  player_card_data = [] # Data containing the card objects
  player_cards = [] # Actual cards for printing
  dealer_card_data = []
  dealer_cards = []
  # set our player and dealers scores
  player_score = 0
  dealer_score = 0
  total_cards = 5

  # while loop to do our initial card drawing
  # i to keep track of the loops
  i = 0
  while len(player_card_data) < total_cards:
    # draw our player cards
    draw_card(deck, player_card_data, player_cards, False)
    # update our player score
    player_score += player_card_data[i].card_value

    # next we need to account for aces
    if len(player_card_data) == total_cards:
      if player_card_data[0].card_value == 11 and player_card_data[1].card_value == 11:
        player_card_data[0] = 1
        player_score -= 10

#testing
  # display_cards(player_cards)


  