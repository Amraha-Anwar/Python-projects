from rich.console import Console
import random

console = Console()

def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    user_choice = console.input("[bold yellow]Choose rock, paper, or scissors: [/bold yellow]").strip().lower()

    if user_choice not in choices:
        console.print("[bold red]⚠️ Invalid choice! Please choose rock, paper, or scissors.[/bold red]")
        return get_user_choice()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def declaring_winner(user, computer):
    if user == computer:
        return 'draw'
    elif(user == 'scissors' and computer == 'paper') or \
        (user == 'rock' and computer == 'scissors') or \
        (user == 'paper' and computer == 'rock'):
        return 'win'
    else:
        return 'lose'
    
def play_game():
    console.print("\n[bold cyan]🎮 Rock, Paper, Scissors - Let's Play! 🎮[/bold cyan]\n")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    console.print(f"\n🧑 You chose: [bold green]{user_choice}[/bold green]")
    console.print(f"🤖 Computer chose: [bold blue]{computer_choice}[/bold blue]\n")

    result = declaring_winner(user_choice, computer_choice)

    if result == "win":
        console.print("[bold green]🎉 You win! 🎉[/bold green]")
    elif result == "lose":
        console.print("[bold red]😢 You lose! Try again.[/bold red]")
    else:
        console.print("[bold yellow]😑 It's a draw![/bold yellow]")

while True:
    play_game()
    again = console.input("\n[bold magenta]Do you want to play again? (yes/no): [/bold magenta]").strip().lower()
    if again != "yes":
        console.print("[bold blue]Thanks for playing! 🎊[/bold blue]")
        break
