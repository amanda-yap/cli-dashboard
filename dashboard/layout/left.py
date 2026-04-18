from rich.layout import Layout
from dashboard.panels.goals import create_goals_panel
from dashboard.panels.todo import create_todo_panel
from dashboard.panels.ascii_2 import create_ascii_panel_2


def create_left_column():
    layout = Layout(name="left")
    layout.split_column(
        Layout(create_todo_panel()),
        Layout(create_goals_panel())
    )
    return layout
