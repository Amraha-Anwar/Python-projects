# PROBLEM STATEMENT:

# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!
# Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.
# Here's a sample run (user input is in bold italics):
# Please type an adjective and press enter. tiny
# Please type a noun and press enter. plant
# Please type a verb and press enter. fly
# Code in Place is fun. I learned to program and used Python to make my tiny plant fly!


# SOLUTION👇
from rich.console import Console

SENTENCE_START = "Panaversity is fun! I learned to program and used Python to make my"

def main():
    console = Console()

    adjective = input("Enter an adjective (e.g., tiny, enormous, colorful): ").strip()
    noun = input("Enter a noun (e.g., cat, spaceship, mountain): ").strip()
    verb = input("Enter a verb (e.g., jump, fly, dance): ").strip()

    final_sentence = f"{SENTENCE_START} {adjective} {noun} {verb}!"
    
    console.print("\n[bold cyan]Here's your fun Mad Libs sentence![/bold cyan]")
    console.print(f"[bold green]{final_sentence}[/bold green]")

if __name__ == "__main__":
    main()
