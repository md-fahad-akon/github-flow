from adventure.utils import read_events_from_file
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
import random

console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."

def left_path(event):
    return f"[cyan]You walk left. {event}[/cyan]"

def right_path(event):
    return f"[magenta]You walk right. {event}[/magenta]"

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    # Intro in styled text
    intro = Text("You wake up in a dark forest.", style="bold bright_white")
    intro.append("\nYou can go ", style="white")
    intro.append("left", style="cyan bold")
    intro.append(" or ", style="white")
    intro.append("right", style="magenta bold")
    intro.append(".", style="white")
    console.print(intro)

    while True:
        # Styled input prompt
        choice = Prompt.ask(
            "[bold yellow]Which direction do you choose?[/bold yellow]",
            choices=["left", "right", "exit"],
            default="exit",
            show_choices=True
        )
        choice = choice.strip().lower()

        if choice == 'exit':
            console.print("[red]You decide to stop your journey. The forest grows silent...[/red]")
            break

        result = step(choice, events)
        console.print(result)
