from rich.console import Console
import random 

console = Console()

def number_guessing():
    console.print("\n\t\t[bold green]Welcome to the Number Guessing Game[/bold green]\n")
    secret_number: int = random.randint(1, 50)
    attempt = 0

    while True:
        try:
            guessed_number = int(console.input("[brown]Enter your guessed number between [1-50]: [/brown]"))
            attempt += 1

            if guessed_number < secret_number:
                console.print("[bold red]Too low! Try again. 🔻[/bold red]")
            elif guessed_number > secret_number:
                console.print("[bold red]Too high! Try again. 🔺[/bold red]")
            else:
                console.print(f"\n\t[bold cyan]Congratulations! You guessed the number {secret_number} in {attempt} attempts! [/bold cyan]✨\n")
                break
        except ValueError:
            console.print("\n\t[bold red]⚠️ Invalid input! Please enter a number.[/bold red]\n")

while True:
    number_guessing()
    again = console.input("\n[blue]Do you wanna play again : (y/n)? [/blue]")
    if again != 'y':
        console.print("\n\t\t[bold yellow]Thanks for playing :) [/bold yellow]\n")
        break