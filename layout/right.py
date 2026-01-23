from rich.layout import Layout
from panels.currently import create_currently_panel
from panels.upcoming import create_upcoming_panel


def create_right_column():
    layout = Layout(name="right")
    layout.split_column(
        Layout(create_currently_panel()),
        Layout(create_upcoming_panel())
    )
    return layout
