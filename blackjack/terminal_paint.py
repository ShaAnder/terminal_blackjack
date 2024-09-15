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

def intro():
  """
  Creates the intro screen using terminal paint.
  """
  # clear screen function
  clear()
  # gets every line in the logo, splits it and then prints / colors it
  for line in layout.game_heading.split("\n"):
    print(term.white + term.center(line))
  for line in layout.instructions_cards.split("\n"):
    print(term.white + term.center(line))
  # using our coordinate function, print our start text
  position(term.center("press any key to continue"), 0, 25, term.black_on_orange)
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
    print(term.white + term.center(line))
  for line in layout.instructions_text.split("\n"):
    print(term.white + term.center(line))
  for line in layout.border.split("\n"):
    print(term.white + term.center(line))
  position(term.center(layout.house_text), 0, 39, term.black_on_white)
  position(term.center("press to begin the game"), 0, 40, term.black_on_white)
  with term.cbreak(), term.hidden_cursor():
    term.inkey()
  clear()

def board(*display_cards):
  """
  Populate the terminal window with the dynamic cards we created in game.py

  Args:
      display_cards (func): returned function for displaying the current cards
  """
  clear()
  position(term.center(layout.computer_board))
  position(term.center(display_cards), 0, 39, term.black_on_orange)
  position(term.center("press to begin the game"), 0, 40, term.black_on_orange)


def table_setup():
  # create our table positions for the cpu and player
  position(layout.cpu_table, 1, 0, term.white)
  position(layout.player_table, 1, 15, term.green)