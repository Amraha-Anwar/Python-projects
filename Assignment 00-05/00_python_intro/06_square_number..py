# PROBLEM STATEMENT

# Ask the user for a number and print its square (the product of the number times itself).
# Here's a sample run of the program (user input is in bold italics):
# Type a number to see its square: 4
# 4.0 squared is 16.0

# SOLUTION 👇
from rich.console import Console

def main():
    console = Console()

    print("\n🔢 Welcome to the Square Calculator! 🔢")
    print("--------------------------------------")

    try:
        
        num = float(input("🔹 Type a number to see its square: "))
        square = num ** 2  

        console.print(f"\n✅ [bold green]{num} squared is {square}[/bold green]\n")

    except ValueError:
        console.print("[red]❌ Invalid input! Please enter a numeric value.[/red]")

if __name__ == '__main__':
    main()
