from rich.layout import Layout
from panels.todo import create_todo_panel
from panels.ascii_2 import create_ascii_panel_2


def create_left_column():
    layout = Layout(name="left")
    layout.split_column(
        Layout(create_todo_panel()),
        Layout(create_ascii_panel_2())
    )
    return layout
