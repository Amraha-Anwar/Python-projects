import time
from rich.console import Console


console = Console()

def mad_libs():
    console.print("\n[bold cyan]Welcome to the Mad Libs Game! 🎭[/bold cyan]\n")

    # Asking for user inputs with colors
    adjective = console.input("[bold yellow]Enter an adjective:[/bold yellow] ")
    noun = console.input("[bold green]Enter a noun:[/bold green] ")
    verb = console.input("[bold magenta]Enter a verb:[/bold magenta] ")
    
    # Story
    story = f"""
    One day, a [bold yellow]{adjective}[/bold yellow] [bold green]{noun}[/bold green] 
    decided to [bold magenta]{verb}[/bold magenta] all day long. 
    It was the most unexpected adventure ever! 🌟
    """

    console.print("\n[bold cyan]Generating your Mad Libs story...[/bold cyan]\n")
    time.sleep(2)  # Adding suspense 
    console.print(story)

# Playing the game in a loop
while True:
    mad_libs()
    again = console.input("\n[bold red]Do you want to play again? (y/n): [/bold red]").strip().lower()
    if again != "y":
        console.print("[bold green]Thanks for playing! 🎉[/bold green]")
        break
