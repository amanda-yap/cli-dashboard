from rich.layout import Layout
from panels.calendar import create_calendar_panel
from panels.time import create_time_panel
from panels.ascii import create_ascii_panel


def create_mid_column():
    layout = Layout(name="mid")
    layout.split_column(
        Layout(create_calendar_panel()),
        Layout(create_time_panel(), size=5),
        Layout(create_ascii_panel())
    )
    return layout
