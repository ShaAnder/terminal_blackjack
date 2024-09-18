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
from os import name, system


### --- VARIABLES --- ###

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

# terminal lines for our input, error message, constants as they should never be changed
TERMINAL_INPUT = 34
TERMINAL_STATUS = 33


### --- FUNCTIONS --- ###

def clear():
    """
    Clears the console.
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

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

def calculate_score(player_card_data):
  """
  Function that loops over the player_card_data and adds the score to a score array
  the function also accounts for multiple aces placed into the array by checking if
  there is already 11 in the array.
  """
  # get our player score
  player_score = []
  # loop over the player card data
  for i in player_card_data:
    #if 11 is already in the array add 1 instead (ace is 1 or 11)
    if 11 in player_score:
      player_score.append(1)
    else: 
      # else append the number
      player_score.append(i.card_value)
    # sum the player scores at the end
    Sum = sum(player_score)
  #return the score
  return Sum

def draw_card(deck, player_card_data, player_cards, hidden):
  """
  Draws A card, converts it and then appends the card data and card to
  the users hand.

  Args:
      deck (list): list (deck of cards)
      player_card_data (list): the card data of the player in question
      player_cards (list): The cards of the player in question
      hidden (Bool): Hidden T/F for card, if False Card face up, else hidden
  """
  # draw a card from the deck
  card = random.choice(deck)
  # we don't want the cards to be removed if the cards are intro cards
  deck.remove(card)
  # convert the card to a readable format
  converted_card = Card.create_card(card, hidden)
  # append to both player card and player card data
  player_card_data.append(card)
  player_cards.append(converted_card)

def display_cards(cards):
  """
  Sorts the card array into a new array for displaying the cards
  side by side 

  Example input / output: 
  ["┌───────────────┐","│ 8             │","┌───────────────┐", "│ 7             │"]
  ["┌───────────────┐┌───────────────┐", "│ 8             ││ 7             │"

  Args:
      cards (list): the player or dealers cards
  """
  # get the lines for each card in the card list
  card_lines = [card.splitlines() for card in cards]
  # get the max lines for however many lines are in the cards
  max_lines = max(len(lines) for lines in card_lines)
  # new card array for containing our line cars
  new_card = []
  # loop through our max lines
  for i in range(max_lines):
    # get our line we want to print (card1[line] + card2[line])
    line_to_print = ""
    # loop through all our card lines
    for lines in card_lines:
      # get the specific line line1, line2 (for each card)
      line = lines[i] if i < len(lines) else " " * len(lines[0])
      # add that to our line to print
      line_to_print += line
    # append that to our array
    new_card.append(line_to_print)
  return new_card


def blackjack_start(deck):
  """
  Main blackjack function, each run is one game.
  """

  #####################
  #Setup Our Variables#
  #####################

  # set our player and dealers cards
  player_card_data = [] # Data containing the card objects
  player_cards = [] # Actual cards for printing
  # dealers cards
  dealer_card_data = []
  dealer_cards = []
  # random cards for the intro
  intro_card_data = []
  intro_cards = []
  # set our player and dealers scores
  player_score = 0
  dealer_score = 0
  # we want to have a hidden dealer score for when we display the dealer
  # score, so the player cannot guess what the dealers hidden first card is.
  # the dealer's real score will keep track of if the dealer goes bust or not.
  dealer_hidden_score = 0

  #######################
  #Step 1 Draw our Intro#
  #######################

  # s here to loop our unique loop, could just pain screen after cards are drawn
  # but want it to be different to player cards
  s = 0
  #we want to do a quick while loop here to create the random intro cards
  while len(intro_card_data) < 2:
    draw_card(deck, intro_card_data, intro_cards, False)
    s+= 1

  # paint our intro (we also feed in a unique card list here so that
  # the blackjack screen has different card on every launch)
  intro(display_cards(intro_cards))

  ##############################
  #Step 2 Draw our Instructions#
  ##############################

  instructions()
  clear()

  ######################
  #Step 3 Draw our Game#
  ######################

  ### STEP 3.1 - DRAW CARDS ###

  # while loop to do our initial card drawing
  # i to keep track of the loops
  i = 0
  while len(player_card_data) < 2:
    # draw our player cards
    draw_card(deck, player_card_data, player_cards, False)
    # update our player score
    if len(player_card_data) == 2:
      player_score += calculate_score(player_card_data)

    # Randomly drawing dealer cards, we want one to be hidden and the rest displayed
    # so for the first loop we will call it with true, and with the second we will call
    #  it with false
    if i == 0:
      draw_card(deck, dealer_card_data, dealer_cards, True)
    else: 
      draw_card(deck, dealer_card_data, dealer_cards, False)
    # Updating Dealer Score, we want it to stay hidden so we
    
    # we increment the loop so we get accurate scoring
    i+=1

  ### STEP 3.2 - CALCULATE OUR SCORE ###
  
  # player score calculated normally
  player_score = calculate_score(player_card_data)
  # dealer score calculated normally
  dealer_score = calculate_score(dealer_card_data)
  # dealer *hidden* score for displaying calculated, by removing the
  # second card onward from the total, this is only needed once, as
  # whenever we update the score from now on, we can just update both
  # values with the new card value
  dealer_hidden_score = dealer_score - dealer_card_data[0].card_value

  # create our board and get a user input from it
  board(dealer_cards = display_cards(dealer_cards), player_cards = display_cards(player_cards), dealer_score = dealer_hidden_score, player_score = player_score)
  get_user_input(TERMINAL_INPUT, TERMINAL_STATUS)
  # 

  # # next we go into the second main phase of the game
  # while True:
  #   # user validation is done in get_user_input, and if correct command is given
  #   # returns either hit or stay so we can do next phase of the game
  #   user_choice = get_user_input(inp)
  #   if user_choice == "hit":
  #     # we draw again
  #     draw_card(deck, player_card_data, player_cards, False)
  #     # update our board
  #     board(dealer_cards = display_cards(dealer_cards), player_cards = display_cards(player_cards), dealer_score = dealer_hidden_score, player_score = player_score)
  #     # recalc score
  #     player_score = calculate_score(player_card_data)
  #     # check if player is bust
  #   elif user_choice == "stay":
  #     pass
    
