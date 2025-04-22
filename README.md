# the-calculator-game
A game about a calculator, inspired by [the password game](https://neal.fun/password-game/), and [balatro](https://store.steampowered.com/app/2379780/Balatro/).

Sections:
- [Gameplay Information](#Game-Info)
- [Installation](#Installation)

# Game Info

## Rounds
The game will be round-based. Each round:
- There will be a target number that the player must attempt to reach via performing calculations.
- There will be a maximum number of button presses allowed
- There will be a random effect placed on the calculator.

As input, the player can enter at most a 2 digit number. The target number may be any number of digits long.

At the beginning of each round, the player is given a random 1- or 2-digit number to work with. The result of each calculation is the first operand in the next. An example to illustrate:
- The player is given the value 9
- To calculate 18, the player hits "*2="
- To calculate 20, the player hits "+2="

## Scoring
Score is based on how close the current number is to the target at the end of the round. Button presses that remain at the end will contribute extra to the score.

## Random Effects
Each round, there is a random effect placed on the calculator. 

Some examples of what effects can look like:
- Can't use even buttons
- Multiplication button uses 10 score
- Addition only
- Can only use equals button once
- No parentheses

# Installation

## Windows
- Clone this repository.
- Find the game executable in the `builds/` directory.

## Unix
- Clone this repository.
- Run `install.sh` to create an executable inside the `builds/` directory.

# Uninstallation
To uninstall, delete this repository.
