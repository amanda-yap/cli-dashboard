import getpass
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align


def create_header():
    return Layout(
        Panel(
            Align.center(f"[bold]{getpass.getuser()}'s dashboard[/bold]"),
            border_style="orange3",
            padding=1
        ),
        name="header",
        size=5
    )
