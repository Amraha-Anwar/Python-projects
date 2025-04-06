import random
from rich.console import Console

console = Console()

words = [
    "python", "developer", "hangman", "coding", "project", "function", "variable",
    "keyboard", "internet", "software", "hardware", "laptop", "network", "browser",
    "terminal", "program", "compile", "debug"
]

word = random.choice(words)
guessed = set()
attempts = 6

console.print("\n🎮 [bold cyan]Welcome to Hangman Game![/bold cyan]")
console.print(f"[bold yellow]The word has {len(word)} letters.[/bold yellow]\n")

while attempts > 0:
    display = " ".join([letter if letter in guessed else "_" for letter in word])
    console.print(f"[bold green]Word:[/bold green] {display}")
    console.print(f"[bold red]Attempts left:[/bold red] {attempts}")

    guess = console.input("[bold magenta]Guess a letter: [/bold magenta]").lower()

    if not guess.isalpha() or len(guess) != 1:
        console.print("[bold red]⚠️ Please enter a valid single letter.[/bold red]\n")
        continue

    if guess in guessed:
        console.print("[bold yellow]🔁 You already guessed that letter.[/bold yellow]\n")
        continue

    guessed.add(guess)

    if guess in word:
        console.print("[bold green]✅ Good guess!\n[/bold green]")
    else:
        console.print("[bold red]❌ Wrong guess!\n[/bold red]")
        attempts -= 1

    if all(letter in guessed for letter in word):
        console.print(f"\n🎉 [bold green]Congrats! You guessed the word: {word}[/bold green]")
        break
else:
    console.print(f"\n😢 [bold red]Game Over! The word was: {word}[/bold red]")
