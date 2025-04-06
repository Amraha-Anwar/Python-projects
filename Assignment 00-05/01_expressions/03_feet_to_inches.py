# PROBLEM STATEMENT:
# This program converts a measurement in feet to inches.
# In the American system of measurement, 1 foot is equal to 12 inches.
# "Foot" is the singular form, while "feet" is the plural form.

# SOLUTION 👇

from rich.console import Console  # Import Rich for better output

# Constant for the number of inches in one foot
INCHES_IN_FOOT = 12  

def main():
    """
    Prompts the user to enter a measurement in feet and converts it to inches.
    """
    console = Console()

    print("-----------------------------------------------------")
    print("                 Feet to Inches Converter            ")
    print("-----------------------------------------------------")
    feet: float = float(input("Enter the number of feet: "))

    # Convert feet to inches
    feet_to_inches: float = feet * INCHES_IN_FOOT

    console.print(f"[bold green]{feet} feet[/bold green] is equal to [bold cyan]{feet_to_inches} inches[/bold cyan]!")

if __name__ == '__main__':
    main()
