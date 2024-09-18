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
TERMINAL_STATUS = 35


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

def calculate_score(card_data):
  """
  Function that loops over the player_card_data and adds the score to a score array
  the function also accounts for multiple aces placed into the array by checking if
  there is already 11 in the array.
  """
  # get our player score
  score = []
  # loop over the player card data
  for i in card_data:
    #if 11 is already in the array add 1 instead (ace is 1 or 11)
    if 11 in score:
      score.append(1)
    else: 
      # else append the number
      score.append(i.card_value)
    # sum the player scores at the end
    Sum = sum(score)
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

def paint_board(dealer_cards, player_cards, dealer_hidden_score, player_score):
  """
  Paints the board for the player to interact with and see

  Args:
    dealer_cards (arr): the dealers cards for printing
    player_cards (arr): the players cards for printing
    dealer_score (int): the dealers current HIDDEN score for displaying
    player_score (int): the players current score for displaying
  """

  ### 1. Paint Board ###
  board(dealer_cards = display_cards(dealer_cards), player_cards = display_cards(player_cards), dealer_score = dealer_hidden_score, player_score = player_score)     
  
  ### 2. Get user Input ###
  user_choice = get_user_input(TERMINAL_INPUT)

  return user_choice
  
def validate_input(choice):
  """
  We want to return true if the user_choice is valid, if not we throw our error and return false
  
  Args:
    user_choice (str): user choice, str if correct
  """
  # check if the user choice len is not 1 and if the choice is not H or S
  if len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S'):
    #throw our error message, setting y coord to be the line below our hit or stay
    error_message(TERMINAL_STATUS, "Error: Please enter a valid input: H for Hit or S for Stay")
    # return false so that loop does not return the correct choice
    return False
  # well if the input is valid, it must be what we want
  else:
    return True 

def calculate_victor(player_win, message):
  sleep(0.5)
  calculating(TERMINAL_INPUT)
  sleep(0.5)
  if player_win == "player":
    win(message)
  else:
    loss(message)
  sleep(2)
  clear()
  

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

  # create an empty user input here so we can check it for validating
  user_choice = ""

  game_on = True

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

  ### STEP 3.3 - PRINT OUR BOARD ###
  
  # we also get the return from this container func from our user validation
  user_choice = paint_board(dealer_cards, player_cards, dealer_hidden_score, player_score)
  
  #######################
  #Step 4 Begin Our Game#
  #######################
  
  # the game should allow us to play until the user goes over 21 or the dealer goes over 17
  # we set these conditions here in case the user get's a blackjack straight away
  while player_score <= 21:
    ### Step 4.0 - BLACKJACK ###
    # first and foremost, even before we validate, we want to see if the player or dealer
    # has a blackjack, if so they automatically win
    clear()
    if player_score == 21 and dealer_score == 21:
      calculate_victor("dealer", "Double blackjack! However the house always wins...")
      break
    elif dealer_score == 21:
      calculate_victor("dealer", "Dealer Blackjack! Better luck next time!")
      break
    elif player_score == 21:
      calculate_victor("player", "Player Blackjack! Congratulations!")
      break
    else:
      clear()
      ### Step 4.1 - Validate Input ###
      is_validated = validate_input(user_choice)
      ### Step 4.2 - Check validation ### 
      if is_validated:
        ### 4.3 - Player Chooses To Hit ###
        # the player chooses to hit, they are allowed to hit until they go bust or stand
        if user_choice.upper() == "H" or user_choice == "h":
          draw_card(deck, player_card_data, player_cards, False)
          player_score += player_card_data[len(player_card_data) -1].card_value
          # we put the check for player score being too much here, because player can accidently go over 21
          if player_score > 21:
            calculate_victor("dealer", f"Your score is: {player_score}, you've gone bust...")
            break
        ### 4.4 - Player Chooses To Stand ###
        # when the player chooses to stand, the dealer will draw UNTIL it reaches 17
        if user_choice.upper() == "S" or user_choice == "s":
          while dealer_score <= 17:
            clear()
            draw_card(deck, dealer_card_data, dealer_cards, False)
            dealer_score += dealer_card_data[len(dealer_card_data) -1].card_value
            dealer_hidden_score = dealer_score - dealer_card_data[0].card_value
            # we want to keep the screen updating until the dealer gets over 17
            board(dealer_cards, player_cards, dealer_hidden_score, player_score)
            # if the dealers score is over 17 break the loop
            if dealer_score >= 17 or player_score > 21:
              clear()
              ## 4.6 - Display victory conditions - ###
              # if the player has finished hitting and the dealer has finished drawing we should run our victory conditions here
              if player_score > dealer_score:
                paint_board(dealer_cards, player_cards, dealer_hidden_score, player_score)
                sleep(2)
                calculate_victor("player", f"Your score is: {player_score} the dealers is: {dealer_score}, you win!")
                break
              elif player_score < dealer_score:
                paint_board(dealer_cards, player_cards, dealer_hidden_score, player_score)
                sleep(2)
                calculate_victor("dealer", f"Your score is: {player_score} the dealers is: {dealer_score}, you lose...")
                break
              elif dealer_score > 21:
                paint_board(dealer_cards, player_cards, dealer_hidden_score, player_score)
                sleep(2)
                calculate_victor("player", f"The dealers score is: {dealer_score}, they've gone bust! You win!")
                break  
        ### 4.5 - Regardless of choice, board is updated ###
        user_choice = paint_board(dealer_cards, player_cards, dealer_hidden_score, player_score)
  
      else: 
        # we also get the return from this container func from our user validation
        user_choice = paint_board(dealer_cards, player_cards, dealer_hidden_score, player_score)
        # ERROR MESSAGE HERE FOR LATER
        is_validated = validate_input(user_choice)

