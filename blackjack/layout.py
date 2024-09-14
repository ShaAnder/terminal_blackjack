"""
This layout module is going to hold all our images for the game
These will be painted to the screen via terminal paint as we 
progress through the game logic
"""

game_heading = """
██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
"""

welcome_heading = """
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ██╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ██║
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗      ██║
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝      ╚═╝
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗    ██╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝    ╚═╝
"""

win_heading = """
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗    ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║    ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║    ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║    ╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║    ██╗
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═╝
"""

loss_heading = """
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗             
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝             
 ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗               
  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝               
   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗    ██╗██╗██╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝    ╚═╝╚═╝╚═╝
"""

instructions_text = """
The aim of the game is 21! You must hit or get as close to 21 to beat your 
opponent, who will also be trying to do the same!

On starting the game, you will be dealt two cards with the option to 
acquire more or hold your hand! The CPU will also be given the same!

Try to outwit the computer and be the first to blackjack!

───────────────────────────────────────────────────────────────────────────────
 ┌───────────────┐ ┌───────────────┐ 
 │ 1             │ │ 6             │ 
 │               │ │               │ 
 │               │ │               │ 
 │               │ │               │ 
 │               │ │               │ 
 │               │ │               │ 
 │               │ │               │ 
 │               │ │               │ 
 │               │ │               │ 
 │               │ │               │ 
 │             1 │ │             6 │ 
 └───────────────┘ └───────────────┘ 
───────────────────────────────────────────────────────────────────────────────
CPU TOTAL: XX
───────────────────────────────────────────────────────────────────────────────
───────────────────────────────────────────────────────────────────────────────
PLAYER TOTAL: XX
───────────────────────────────────────────────────────────────────────────────
 ┌───────────────┐ ┌───────────────┐
 │ 10            │ │ A             │
 │               │ │               │
 │               │ │               │
 │               │ │               │
 │               │ │               │
 │               │ │               │
 │               │ │               │
 │               │ │               │
 │               │ │               │
 │               │ │               │
 │            10 │ │             A │
 └───────────────┘ └───────────────┘
───────────────────────────────────────────────────────────────────────────────

And remember the house always wins...
"""

# this is an example card, it will be dynamically created via a function and
# inserted into a list for reading later
card = """
┌───────────────┐
│               │
│               │
│               │
│               │
│               │
│               │
│               │
│               │
│               │
└───────────────┘                                                                   
"""

cpu_table = """
───────────────────────────────────────────────────────────────────────────────
CPU TOTAL:
───────────────────────────────────────────────────────────────────────────────
"""

player_table = """
───────────────────────────────────────────────────────────────────────────────
PLAYER TOTAL:
───────────────────────────────────────────────────────────────────────────────
"""

border = """
───────────────────────────────────────────────────────────────────────────────
"""