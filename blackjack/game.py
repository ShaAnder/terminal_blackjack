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
SLEEP_TIMER = 0.5


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

def swap_screen():
  """
  Small loop for swapping between screens consisting of
  our clear function and the sleep module.
  """
  sleep(SLEEP_TIMER)
  clear()
  sleep(SLEEP_TIMER)

def create_deck():
  """
  Creates a new deck of 52 card objects by passing each card suit, card and
   card value into the Card class, then appending it to the deck array.
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

  Args:
    card_data (arr): calculates the score of the card data array of the player 
  """
  # get our player score
  total = 0
  score = []
  # loop over the player card data
  for i in card_data:
    # if 11 is already in the array add 1 instead (ace is 1 or 11)
    if 11 in score:
      score.append(1)
    else: 
      # else append the number
      score.append(i.card_value)
    # sum the player scores at the end
    total = sum(score)
  # we want to run another condition here to automatically recalculate the score
  # if there is an ace and the score is over 21 because then it will prevent the 
  # user from atuomatically losing
  if total > 21 and 11 in score:
    # return the score
    return total - 10
  else: 
    return total

def draw_card(deck, card_data, owners_cards, delete):
  """
  Draws A card, converts it and then appends the card data and card to
  the users hand.
  
  Args:
    deck (list): list (deck of cards)
    card_data (list): the card data of the player in question
    player_cards (list): The cards of the player in question
    delete (Bool): bool for confiming card deletion
  """
  # draw a card from the deck
  card = random.choice(deck)
  # convert the card to a readable format
  converted_card = Card.create_card(card)
  # append to both player card and player card data
  card_data.append(card)
  owners_cards.append(converted_card)
  # checks to see if the delete argument is True or not
  if delete == True:
    deck.remove(card)
  else:
    pass
    
def display_cards(cards):
  """
  Sorts the card array into a new array for displaying the cards
  side by side.

  Example input / output: 
  ["┌───────────────┐","│ 8             │","┌───────────────┐", "│ 7             │"]
  ["┌───────────────┐┌───────────────┐", "│ 8             ││ 7             │"

  Args:
      cards (list): player / dealer / intro cards
  """
  # get the lines for each card in the card list
  card_lines = [card.splitlines() for card in cards]
  # get the max lines for however many lines are in the cards
  max_lines = max(len(lines) for lines in card_lines)
  # new card array for containing our card lines
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

def paint_board(dealer_cards, player_cards, dealer_score, player_score, condition):
  """
  Paints the board for the player to interact with and see.

  Args:
    dealer_cards (arr): the dealers cards for printing
    player_cards (arr): the players cards for printing
    dealer_score (int): the dealers current score for displaying
    player_score (int): the players current score for displaying
    condition (str): condition we pass in to determine what the board paints 
  """

  # the reason this is 2 function calls in one is I want to not only paint the board
  # but also different status messages alongside it, allowing the user to effectively
  # see the stage changes and get feedback.

  ### 1. Clear our screen ###
  # firstly we want to clear our screen whenever the game board is updated
  clear()

  ### 2. Paint Board ###
  # paint our board with the cards, and scores
  board(dealer_cards = display_cards(dealer_cards), player_cards = display_cards(player_cards), dealer_score = dealer_score, player_score = player_score)     
  
  ### 3. paint our message ###
  # paints our status / terminal / feedback message based on the various
  # conditions we provide. This made sense to be here as one of these will
  # always be painted when im painting the board

  # we have 3 conditions: accepting_inputs, calculating, continue state
  if condition == "accepting_inputs":
    user_choice = get_user_input(TERMINAL_INPUT, "Please type H to hit or S to Stay: ")
    return user_choice
  elif condition == "continue":
    #if it's not accepting_inputs or calculating it must be user prompt to hit enter
    cont()
  else:
    pass
  
def validate_input(choice, op1, op2):
  """
  Validates the input, and returns true if input is valid false if it is not.
  
  Args:
    user_choice (str): user choice, str if correct.
  """
  # I wanted to keep the user input validation as simple as possible, to ensure that the 
  # user could not get any wrong ideas as well as not having to write an exhaustive loop
  # check to see if the user choice meets the criteria, if not more than one and not H or S
  if len(choice) != 1 or (choice.upper() != op1 and choice.upper() != op2):
    # return false so that loop does not return the correct choice
    return False
  # well if the input is valid, it must be what we want
  else:
    return True 

def calculate_victor(player_win, message):
  """
  Takes the player whos winning string and a message and passes it to the 
  terminal to paint.

  Args:
    player_win (str): "player" or "dealer".
    message (str): string with the message to paint to the terminal.
  """
  if player_win == "player":
    win(message)
  else:
    loss(message)
  
def play_again(deck):
  """
  Ask the user if they want to play again.
  """
  #clear screen
  clear()
  # get user input
  try_again = get_user_input("Would you like to play again? Y/N: ")
  # validate input
  valid_try_again = validate_input(try_again, "Y", "N")
  if valid_try_again == True:
    if try_again == "Y":
      # if validation == True reset game 
      clear()
      blackjack_start(deck)
    else:
      clear()
      break
    


def blackjack_start(deck):
  """
  Main blackjack function, each run is one game.

  Args:
    deck (arr): array containing our deck of card objects.
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
  # create an empty user input here so we can check it for validating
  user_choice = ""
  # set our game start variable
  game_on = True
  #######################
  #Step 1 Draw our Cards#
  #######################  
  # while loop to do our initial card drawing
  # i to keep track of the loops
  i = 0
  while len(player_card_data) < 2:
    # draw our player cards
    draw_card(deck, player_card_data, player_cards, True)
    # draw our intro cards
    draw_card(deck, intro_card_data, intro_cards, False)
    # we increment the loop so we get accurate scoring
    i+=1
    # once our player cards are at 2 break the loop
    if len(player_card_data) == 2:
      break
  # now we draw our dealers card, dealer will only draw one for simplicity
  # then when player finishes hitting the dealer will begin to draw his cards
  draw_card(deck, dealer_card_data, dealer_cards, True)   
  ### STEP 1.2 - CALCULATE OUR SCORE ### 
  # player score calculated normally
  player_score = calculate_score(player_card_data)
  # dealer score calculated normally
  dealer_score = calculate_score(dealer_card_data)  
  ##############################
  #Step 2 Draw our Instructions#
  ##############################
  # paint our intro 
  intro(display_cards(intro_cards))
  # swap screens
  swap_screen()
  # paint our instructions
  instructions()
  ######################
  #Step 3 Draw our Game#
  ######################
  # firstly we paint our game screen
  # we also get the return from this container func from our user validation
  user_choice = paint_board(dealer_cards, player_cards, dealer_score, player_score, "accepting_inputs")  
  #######################
  #Step 4 Begin Our Game#
  #######################
  # while game_on
  while player_score <= 21:
    ### 4.1 - If validation == True play game ###
    is_validated = validate_input(user_choice, "H", "S")
    if is_validated == True:
      ### 4.3 - Player Chooses To Hit ###
      # the player chooses to hit, they are allowed to hit until they go bust or stand
      if user_choice.upper() == "H" or user_choice == "h":
        draw_card(deck, player_card_data, player_cards, True)
        player_score += player_card_data[len(player_card_data) -1].card_value
        sleep(1)
        calculating("Cards Drawn, calculating score...")
        sleep(1)
        # if the player goes over 21 we want to prevent them from hitting
        paint_board(dealer_cards, player_cards, dealer_score, player_score, "continue")
        if player_score > 21:
          paint_board(dealer_cards, player_cards, dealer_score, player_score, "")
          calculating("User has drawn over 21... Moving to dealers turn")
          user_choice = "S"
          sleep(2)
        else:
          user_choice = paint_board(dealer_cards, player_cards, dealer_score, player_score, "accepting_inputs")
      ### 4.4 - Player Chooses To Stand or user draws over 21 ###
      # when the player chooses to stand, the dealer will draw UNTIL it reaches 17
      if user_choice.upper() == "S" or user_choice == "s":
        paint_board(dealer_cards, player_cards, dealer_score, player_score, "")
        calculating("Dealer Drawing...")
        sleep(2)
        while dealer_score <= 17:
          #let the dealer draw cards and calc score until it hit's 17
          draw_card(deck, dealer_card_data, dealer_cards, True)
          dealer_score += dealer_card_data[len(dealer_card_data) -1].card_value
          if dealer_score >= 17:
            clear()
            break
        # we want to do our score calculation inside of the dealers turn because
        # we want the dealer to be last on a turn, instructions will convey this
        
        # one dealer has finished drawing, we let the user know someone has one
        # "calculate" the victor and let user continue
        paint_board(dealer_cards, player_cards, dealer_score, player_score, "")
        calculating("All Draws Complete Calculating Winner...")
        sleep(2)
        paint_board(dealer_cards, player_cards, dealer_score, player_score, "continue")
        ### FIRST VICTORY CONDITION ### 
        ## BLACKJACK
        # Firstly check if there is a blackjack, we only check it here because
        # common sense is that a player will not it if they have a winning number
        # if they do they lose
        if player_score == 21 or dealer_score == 21:
          paint_board(dealer_cards, player_cards, dealer_score, player_score, "")
          # if 21 is detected we swap screens and give control to the player to continue
          sleep(1)
          calculating("BLACKJACK DETECTED! Calculating victor...")
          sleep(1)
          paint_board(dealer_cards, player_cards, dealer_score, player_score, "continue")
          if player_score == 21 and dealer_score == 21:
            # we also have a screen swap function which bundles two sleeps and a clear
            # in case we're swapping to a different screen
            swap_screen()
            calculate_victor("dealer", "Double blackjack! However the house always wins...")
          elif dealer_score == 21:
            swap_screen()
            calculate_victor("dealer", "Dealer Blackjack! Better luck next time!")
          elif player_score == 21:
            swap_screen()
            calculate_victor("player", "Player Blackjack! Congratulations!")
        elif player_score > dealer_score and player_score < 21:
          swap_screen()
          calculate_victor("player", f"Your score is: {player_score} the dealers is: {dealer_score}, You win!")
        elif player_score < dealer_score and dealer_score < 21:
          swap_screen()
          calculate_victor("dealer", f"Your score is: {player_score} the dealers is: {dealer_score}, you lose...")
        elif player_score > 21 and dealer_score < 21:
          swap_screen()
          calculate_victor("dealer", f"Your score is: {player_score}, you've gone bust...")

        elif dealer_score > 21 and player_score < 21:
          swap_screen()
          calculate_victor("player", f"The dealers score is: {dealer_score}, they've gone bust! You win!")
        else:
          # both players have drawn over 21 both lose 
          swap_screen()
          calculate_victor("dealer", f"Your score is: {player_score} the dealers is: {dealer_score}, Double bust... You both lose...")
        sleep(2)
        play_again(deck)
    # well if if validated is not true, we need to throw our error and go again
    else:
      # if code not valid, throw error
      error_message("Error: Please enter a valid input: H for Hit or S for Stay")
      sleep(1)
      user_choice = paint_board(dealer_cards, player_cards, dealer_score, player_score, "accepting_inputs")

