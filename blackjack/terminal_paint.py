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
  Clears the terminal, this is different to 
  the main clear function in game as I need this
  for when im using the with term.cbreak() calls.
  """
  print(term.home + term.clear)

def intro(display_cards):
  """
  Creates the intro screen using terminal paint.

  Args:
    display_cards (arr) array containing the intro_cards for display.
  """
  with term.location (0, 8):
  # gets every line in the logo, splits it and then prints / colors it
    for line in layout.game_heading.split("\n"):
      print(term.yellow + term.center(line))
    for l in display_cards:
      print(term.yellow + term.center(l))
    # using our coordinate function, print our start text
  position(term.center("A game of wits and chance, Press any key to continue"), 0, 27, term.black_on_yellow)
  # check for inputs, then clear the screen
  with term.cbreak(), term.hidden_cursor():
    term.inkey()
  # clear when inkey is recognized
  clear()

def instructions():
  """
  Creats the instructions screen for the game.
  """
  with term.location (0, 7):
    # gets every line in the logo, splits it and then prints / colors it
    for line in layout.welcome_heading.split("\n"):
      print(term.yellow + term.center(line))
    for line in layout.instructions_text.split("\n"):
      print(term.white + term.center(line))
    position(term.center("Press any key begin the game"), 0, 27, term.black_on_yellow)
  with term.cbreak(), term.hidden_cursor():
    term.inkey()

def board(dealer_cards, player_cards, dealer_score, player_score):
  """
  Populate the terminal window with the dynamic cards we created in game.py.

  Args:
      dealer_cards (arr): the dealers cards for printing.
      player_cards (arr): the players cards for printing.
      dealer_score (int): the dealers current HIDDEN score for displaying.
      player_score (int): the players current score for displaying.
  """
  print(term.white + term.center(layout.border))
  print(term.blue + term.center(layout.dealer_hand))
  for line in dealer_cards:
    print(term.blue + term.center(line))
  print(term.white + term.center(layout.scores.format(dealer_score, player_score))) 
  print(term.green + term.center(layout.player_hand))
  for line in player_cards:
    print(term.green + term.center(line))
  print(term.white + term.center(layout.border))
 
def get_user_input(terminal_row, message):
  """
  Takes the value entered, passes it into the validatior, checks to see if it is either 
  "Hit" or "Stay" then returns that string to tell the program what to do next.

  Args:
    terminal_row (int): number row where we want our input message to appear.
    message (str): message we pass in whenever we want user to input
  """
  print(term.move(terminal_row, 0) + term.black_on_yellow + term.center(message) + term.normal)
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

def error_message(error_message):
  """
  Rerurns an error message painted on the screen for user feedback.

  Args:
    error_message (str): the message for the user.
  """
  with term.location(0, 35):
    print(term.yellow_on_black + term.center(error_message))

def win(condition_message):
  """
  Rerurns an error message painted on the screen for user feedback.

  Args:
    error_message (str): the message for the user.
  """
  with term.location (0, 13):
    for line in layout.win_heading.split("\n"):
        print(term.yellow + term.center(line))
  position(term.center(condition_message), 0, 23, term.black_on_yellow) 

def loss(condition_message):
  """
  Clears and prints the loss scene with the custom message.

  Args:
    error_message (str): the message for the user.
  """
  with term.location (0, 13):
    for line in layout.loss_heading.split("\n"):
        print(term.yellow + term.center(line))
  position(term.center(condition_message), 0, 23, term.black_on_yellow) 

def calculating(message):
  """
  Places a positional text for user feedback on card drawn.

  Args: 
    message (str): string containing our calculation message.
  """
  position(term.center(message), 0, 34, term.white_on_blue)

def cont():
  """
  places a positional text for user_feedback.
  """
  position(term.center("Press any key to continue the game..."), 0, 34, term.black_on_yellow)
  with term.cbreak(), term.hidden_cursor():
    term.inkey()
