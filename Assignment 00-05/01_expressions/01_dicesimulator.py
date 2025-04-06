# PROBLEM STATEMENT
# This program simulates rolling two dice three times and prints the result of each roll.
# It also demonstrates how variable scope works.

# SOLUTION 👇

import random  # Import the random module for generating random numbers

DICE_SIDES = 6  # Number of sides on each die

def roll_dice():
    
    die1: int = random.randint(1, DICE_SIDES)
    die2: int = random.randint(1, DICE_SIDES)
    total: int = die1 + die2
    print("The total of both dice is:", total)

def main():
    die1: int = 12  # Local variable in main()
    
    print("-----------------------------------------------------")
    print("                  🎲 Dice Roll Results 🎲              ")
    print("-----------------------------------------------------")
    
    print("The value of 'die1' in main() before rolling the dice:", die1)
    roll_dice()
    roll_dice()
    roll_dice()
    print("The value of 'die1' in main() after rolling the dice:", die1)

if __name__ == '__main__':
    main()
