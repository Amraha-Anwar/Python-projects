# PROBLEM STATEMENT

# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).
# Here's a sample run of the program (user input is in bold italics):
# What is the length of side 1? 3
# What is the length of side 2? 4
# What is the length of side 3? 5.5
# The perimeter of the triangle is 12.5

# SOLUTION👇

from rich.console import Console

def main():
    console = Console()

    print("\n📐 Welcome to the Triangle Perimeter Calculator! 📐")
    print("---------------------------------------------------")

    try:
        side1 = float(input("🔹 Enter the length of side 1: "))
        side2 = float(input("🔹 Enter the length of side 2: "))
        side3 = float(input("🔹 Enter the length of side 3: "))

        perimeter = side1 + side2 + side3

        print("\n---------------------------------------------------")
        console.print(f"📏 Side 1: [bold italic]{side1}[/bold italic]")
        console.print(f"📏 Side 2: [bold italic]{side2}[/bold italic]")
        console.print(f"📏 Side 3: [bold italic]{side3}[/bold italic]")
        console.print(f"✅ The perimeter of the triangle is: [bold green]{perimeter}[/bold green]")
        print("---------------------------------------------------\n")

    except ValueError:
        console.print("[red]❌ Invalid input! Please enter numeric values only.[/red]")

if __name__ == "__main__":
    main()
