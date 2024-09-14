# Terminal Blackjack

![Terminal blackjack Gif]()

Visit the deployed site: [Terminal Blackjack](https://shaAnder.github.io/Quizzical/)

![GitHub last commit](https://img.shields.io/github/last-commit/shaAnder/terminal_blackjack?color=red&style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/shaAnder/terminal_blackjack?color=orange&style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/shaAnder/terminal_blackjack?color=yellow&style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/shaAnder/terminal_blackjack?color=green&style=for-the-badge)

## CONTENTS

- [Terminal Blackjack](#terminal-blackjack)
  - [The History Of Blackjack](#the-history-of-blackjack)
  - [Terminal Blackjack Overview](#terminal-blackjack-overview)
  - [How It Works](#how-it-works)
  - [User Stories](#user-stories)
  - [Features](#features)
    - [Future Features](#future-features)
  - [Data Model](#data-model)
  - [Testing](#testing)
    - [Validator Testing](#validator-testing)
    - [Bugs Found During Testing](#bugs-found-during-testing)
    - [Known Remaining Bugs](#known-remaining-bugs)
  - [Deployment](#deployment)
  - [Development](#development)
    - [Languages](#languages)
    - [Tools](#tools)
  - [Credits & Attributions](#credits---attributions)
    - [Attribution](#attributions-)
    - [Other](#other)

---

### The history of blackjack

Equally well known as Twenty-One. Blackjack is a card game where players face off to create a hand of 21 on each round all while trying not to go over the number. While the popularity of Blackjack dates from World War I, its roots go back to the 1760s in France, where it is called Vingt-et-Un (French for 21). Today, Blackjack is the one card game that can be found in every casino.

### Terminal Blackjack Overview

Terminal blackjack is a game of blackjack that is well running on the users terminal. The game leverages the blessed library to create, paint to and refresh objects on the terminal
allowing the terminal to act like a basic GUI.

The game has a number of features

- A well mapped out data model with a flexible modular class to store state and attributes
- Usage of the `blessed` Python library for manipulation and control of the terminal
- A clean UX that provides an overlay of the current game progression and provides solid user feedback on the outcome of their choices.

---

### How It Works

Terminal blackjack works in the following way:

- Firstly: Initialize the game object (class)
- Seconly: Draw our terminal Output
- Third: Run the game until a victor is declared:
  - Player Step:
    - Presents the player with their choices
    - Allows the player to act on their choice
    - Update the game to give player feedback on their choice
  - CPU Step:
    - Passes the turn to the CPU
    - CPU makes their move
    - Update the board with the CPU's move
  - Check Game State:
    - Check to see if any of the victory / loss conditions are met
    - Repeat player and CPU steps
- Finally: Print Victory Message

The game runs utilizing a simplified version of the rules and concepts of blackjack so as to make the game a bit easier to code:

- The players attempt to beat the CPU by getting a count as close to 21 as possible, without going over 21.
- Players can opt to hit or stand, hit will deal them another card, stand will prevent them from drawing new cards until the next round.
- for simplicities sake the CPU will always try and draw until it is at 16 or over and then will automatically stand
- The closest player to 21 OR whoever lands on 21 wins, also for simplicities sake if both the player and CPU hit 21, the CPU (house) will be declared the winner
- Whoever goes over 21 on their turn is automatically declared the loser.

---

### User Stories

I opted to follow a traditional user stories / objective model on how to run the game.

As a user

- I want a dynamic game of blackjack that I can play, I don't want to have to scroll through hundreds of print statements
- I want the game to be simple to understand and play with clear instructions
- I want clear visual cues indicating the current state of the game

As the owner:

- I want to ensure a simple clean terminal that doesn't require a lot of print() statements
- I want to ensure that the site is visually striking and memorable
- My concern is less the site being responsive and more than it can be played on the devices, as it will be hosted in the terminal it won't be playable on mobile
- I want to ensure that the code leverages best practices as I want to extend this application in the future

---

### Features

---

### Data Model

---

### Testing

---

### Deployment

---

### Development

---

### Credits & Attributions
