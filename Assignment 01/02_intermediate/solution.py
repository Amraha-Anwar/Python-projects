import random
from rich.console import Console
from rich.prompt import Prompt

console = Console()

ROUNDS: int = 5

def main():
    console.print("\n[bold cyan underline]Welcome to My Python Game[/bold cyan underline]\n")

    score = 0 
    for i in range(ROUNDS):
        console.rule(f"[bold yellow]Round {i + 1}[/bold yellow]", style="green")

        computer_num = random.randint(1, 100)
        player_num = random.randint(1, 100)
        console.print(f"[bold magenta]Your Number is:[/bold magenta] [yellow]{player_num}[/yellow]")

        response = Prompt.ask("[bold cyan]What do you think? Will the computer's number be [green]higher[/green] or [red]lower[/red]?[/bold cyan]", choices=["higher", "lower"])

        higher_and_correct = response == 'higher' and computer_num > player_num
        lower_and_correct = response == 'lower' and computer_num < player_num

        if higher_and_correct or lower_and_correct:
            console.print(f"[bold green]🎉 You were right![/bold green] [italic]Computer's number was[/italic] [yellow]{computer_num}[/yellow]")
            score += 1
        else:
            console.print(f"[bold red]😢 Awwww! That's incorrect.[/bold red] The computer's number was: [yellow]{computer_num}[/yellow]")

        console.print(f"[bold blue]Your score is now:[/bold blue] [bold white on green] {score} [/bold white on green]\n")

    console.rule("[bold magenta]Game Over[/bold magenta]")
    console.print(f"\n[bold cyan]Your final score is:[/bold cyan] [bold white on purple] {score} [/bold white on purple]")

    if score == ROUNDS:
        console.print("[bold green]🏆 Wohoo! You've played perfectly![/bold green]")
    elif score > ROUNDS // 2:
        console.print("[bold yellow]👏 Good job! You've played really well![/bold yellow]")
    else:
        console.print("[bold red]💔 Uh! Better luck next time :([/bold red]")

if __name__ == '__main__':
    main()
