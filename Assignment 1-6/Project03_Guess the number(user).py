from rich.console import Console
import time

console = Console()

def guess_the_number():
    console.print("\n\t\t[bold green]Welcome to the Number Guessing Game[/bold green]\n")
    console.print("\n[bold cyan]Think of a number between 1 and 50, and I'll guess it![/bold cyan]\n")
    time.sleep(2)

    low, high = 1, 50
    attempts = 0

    while True:
        guess = (low + high) // 2
        attempts += 1

        user_feedback = console.input(f"[bold yellow]Is your number {guess}? (higher/lower/correct): [/bold yellow]").strip().lower()

        if user_feedback == 'higher':
            low = guess + 1
            console.print("[bold magenta]🔼 Okay, I'll guess higher![/bold magenta]")
        elif user_feedback == 'lower':
            high = guess - 1
            console.print("[bold magenta]🔽 Okay, I'll guess lower![/bold magenta]")
        elif user_feedback == 'correct':
            console.print(f"\n🎉 [bold green]Yes! I guessed your number {guess} in {attempts} attempts![/bold green] 🎉")
            break
        else:
            console.print("[bold red]⚠️ Invalid response! Please type 'higher', 'lower', or 'correct'.[/bold red]")

while True:
    guess_the_number()
    again = console.input("\n[bold magenta]Do you want to play again? (yes/no): [/bold magenta]").strip().lower()
    if again != "yes":
        console.print("[bold blue]Thanks for playing! 🎊[/bold blue]")
        break