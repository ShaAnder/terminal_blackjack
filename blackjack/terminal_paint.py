"""
terminal_paint.py
Module to define our terminal printing / updating functions. 
Module uses the blessed library for printing
"""

### --- IMPORTS --- ###

# we want the blessed library, as the project is being deployed on heroku
# the idea of a gui app is out the window. The blessed library allows us to 
# circumvent this via dynamic updating of the of the terminal
from blessed import Terminal

# we also import all our art here
from blackjack import layout

### --- VARIABLES --- ###

# now create a new terminal
term = Terminal()

print (term.height, term.width)
def position(text, xcoords, ycoords, color):
  """
  Gets our position on the terminal for inserting objects.

  Args:
      text (str): text we want to display
      xcoords (int): x coordinate for placement
      ycoords (int): y coordinate for placement
      color (var): color from the terminal lib
  """
  with term.location(x=xcoords, y=ycoords):
    print(color + text)

def clear():
  """
  Clears the terminal
  """
  print(term.home + term.clear)

def intro(display_cards):
  """
  Creates the intro screen using terminal paint.
  """
  # clear screen function
  clear()
  # gets every line in the logo, splits it and then prints / colors it
  for line in layout.game_heading.split("\n"):
    print(term.yellow + term.center(line))
  for l in display_cards:
    print(term.yellow + term.center(l))
  # using our coordinate function, print our start text
  position(term.center("A game of wits and chance, Press any key to continue"), 0, 19, term.black_on_yellow)
  # check for inputs, then clear the screen, 
  # break -> reads keystroke immediately after it's pressed
  # hidden cursor -> hides cursor
  # inkey -> key press event
  with term.cbreak(), term.hidden_cursor():
    term.inkey()
  # clear when inkey is recognized
  clear()

def instructions():
  """
  Creats the instructions screen for the game
  """
  clear()
  for line in layout.welcome_heading.split("\n"):
    print(term.yellow + term.center(line))
  for line in layout.instructions_text.split("\n"):
    print(term.white + term.center(line))
  position(term.center(layout.house_text), 0, 18, term.black_on_yellow)
  position(term.center("Press any key begin the game"), 0, 19, term.black_on_yellow)
  with term.cbreak(), term.hidden_cursor():
    term.inkey()
  clear()

def board(dealer_cards, player_cards, dealer_score, player_score):
  """
  Populate the terminal window with the dynamic cards we created in game.py

  Args:
      dealer_cards (arr): the dealers cards for printing
      player_cards (arr): the players cards for printing
      dealer_score (int): the dealers current HIDDEN score for displaying
      player_score (int): the players current score for displaying
  """
  print(term.yellow + term.center(layout.dealer_hand))
  for line in dealer_cards:
    print(term.yellow + term.center(line))
  print(term.yellow + term.center(layout.scores.format(dealer_score, player_score))) 
  print(term.yellow + term.center(layout.player_hand))
  for line in player_cards:
    print(term.green + term.center(line))
  # clear()

 

def get_user_input(terminal_row):
  """
  Takes the value entered, passes it into the validatior, checks to see if it is either 
  "Hit" or "Stay" then returns that string to tell the program what to do next

  Args:
    terminal_row:  (int) -> number row where we want our input message to appear
    TERMINAL_STATUS:  (int) -> number row where we want our error message to appeaer
  """
  
  print(term.move(terminal_row, 0) + term.black_on_yellow + term.center("Please type H to hit or S to Stay: ") + term.normal)
  print(term.move(terminal_row, 55)+ term.normal)
  with term.cbreak():
    target, inp, i = "", term.inkey(), 1
    print(term.move(terminal_row, 55 + i)+inp)
    while inp.name != "KEY_ENTER":
      target += inp
      print(target)
      inp = term.inkey()
      i +=1
      if i == 1:
        print(term.move(terminal_row, 55+i)+inp)
    print(term.move(terminal_row-1, 0))
  
    return target

def error_message(terminal_row, error_message):
  """
  Rerurns an error message painted on the screen for user feedback

  Args:
    terminal_row (int): number of the row the error message will appear on
    error_message (str): the message for the user
  """
  with term.location(terminal_row, 40):
    print(term.yellow_on_black + term.center(error_message))



def end_game_message(condition, specific_condition):
  """
  Displays a detailed status message depending on the win condition, there
  is only a win or a loss, so we split it into two main messages, with 
  a subsection for each specific condition

  Args:
    condition (str): generalized condition -> player_wins / dealer_wins
    specific_condition (str): specific_condition -> blackjack, bust -> tie
    
  """
  if condition == "player_wins":
    for line in layout.loss_heading.split("\n"):
      print(term.yellow + term.center(line))
    if specific_condition == "blackjack":
      condition_message = "Blackjack! Congratulations on beating the house"
      position(term.center(condition_message), 0, 34, term.yellow)
    else:
      condition_message = "The dealer is bust! Congratulations"
      position(term.center(condition_message), 0, 34, term.yellow)
  elif condition == "dealer_wins":
    for line in layout.win_heading.split("\n"):
      print(term.yellow + term.center(line))
    if specific_condition == "blackjack":
      condition_message = "Blackjack! The house wins... better luck next time"
      position(term.center(condition_message), 0, 34, term.yellow)
    elif specific_condition == "tie":
      condition_message = "It's a tie! But the house always wins..."
      position(term.center(condition_message), 0, 34, term.yellow)
    else:
      condition_message = "You went too high... Player bust! House Wins"
      position(term.center(condition_message), 0, 34, term.yellow)
  # regardless of the condition ask the player if they want to play again:
  inp = input("Play again?")
  position(term.center(inp), 0, 35, term.black_on_yellow)
  clear()
  return inp
    
