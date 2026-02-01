from rich.console import Group
from rich.panel import Panel
from rich.text import Text


def create_picca_panel():
    picca_content = Group(
        Text("        Picca:", style="bold light_goldenrod3"),
        Text("(>'')>  Hello, friend!")
    )

    return Panel(
        picca_content,
        border_style="orange3",
        padding=(1, 1)
    )