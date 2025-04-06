import random
import string
from rich.console import Console

console = Console()

console.print("\n\t\t[bold cyan]🔐 Welcome to the Password Generator![/bold cyan]\n")

chars = string.ascii_letters + string.digits + "!@#$%^&*()-"

numbers = int(input("🔢 How many passwords would you like to generate? "))
length = int(input("🔑 What should be the length of each password? "))

console.print("\n[bold green]Here are your generated passwords:[/bold green]\n")

for password in range(numbers):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    console.print(f"[yellow]{passwords}[/yellow]")
