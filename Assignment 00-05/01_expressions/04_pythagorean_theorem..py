# Problem Statement:
# This program calculates the hypotenuse of a right triangle using the Pythagorean theorem:
# BC² = AB² + AC²
# where:
#   - BC is the hypotenuse (longest side),
#   - AB and AC are the two perpendicular sides.
# The user enters the lengths of AB and AC, and the program computes the hypotenuse (BC).

# SOLUTION 👇

import math  # math module for square root calculation
from rich.console import Console 

def main():
    console = Console()

    print("-----------------------------------------------------")
    print("            Right Triangle Hypotenuse Finder         ")
    print("-----------------------------------------------------")

    side_AB: float = float(input("Enter the length of AB: "))
    side_AC: float = float(input("Enter the length of AC: "))
    side_BC: float = math.sqrt(side_AB**2 + side_AC**2)

    
    console.print(f"\nThe length of BC (the hypotenuse) is: [bold cyan]{side_BC:.2f}[/bold cyan]")  #:.2f for only 2 decimal places

if __name__ == '__main__':
    main()
