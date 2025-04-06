# PROBLEM STATEMENT:
# Simulate rolling two dice, and prints results of each roll as well as the total.

import random
from rich.console import Console

DIE_SIDES = 6

def main():
    console = Console()

    console.print("-" * 50, style="bold cyan")
    console.print("🎲 Rolling Two Dice... 🎲", style="bold yellow")
    console.print("-" * 50, style="bold cyan")

    die1 = random.randint(1, DIE_SIDES)
    die2 = random.randint(1, DIE_SIDES)
    total = die1 + die2

    console.print(f"🟢 Die 1: [bold green]{die1}[/bold green]")
    console.print(f"🔵 Die 2: [bold blue]{die2}[/bold blue]")
    console.print(f"✨ Total: [bold magenta]{total}[/bold magenta]")

if __name__ == "__main__":
    main()