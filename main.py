import calendar
import time
from datetime import datetime
import json
from pathlib import Path

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.progress import BarColumn, Progress, TextColumn
from rich.table import Table
from rich.text import Text

TODO_FILE =  Path(__file__).with_name("todo.json")

console = Console()

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

def create_calendar_panel():
    today = datetime.today()
    year = today.year
    month = today.month
    day = today.day
    cal = calendar.Calendar()
    today_tuple = (day, month, year)

    table = Table(
        title=f"{calendar.month_name[month]} {year}",
        style="orange3",
        box=box.SIMPLE,
        padding=0
    )

    for week_day in cal.iterweekdays():
        table.add_column(
            "{:.3}".format(calendar.day_name[week_day]), justify="right"
        )

    month_days = cal.monthdayscalendar(year, month)
    for weekdays in month_days:
        days = []
        for index, day in enumerate(weekdays):
            day_label = Text(str(day or ""), style="light_goldenrod3")
            if index in (5, 6): # Different colour for weekends
                day_label.stylize("light_yellow3")
            if day and (day, month, year) == today_tuple:
                day_label.stylize("white on dark_red")
            days.append(day_label)
        table.add_row(*days)

    return Panel(
        Align.center(table),
        title="CALENDAR",
        border_style="orange3",
        padding=(1,1)
    )


def create_time_panel():
    return Panel(
        Align.center(f"[bold]{get_current_time()}[/]"),
        title="TIME",
        border_style="orange3",
        padding=(1, 2)
    )


def create_todo_panel():
    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column()

    def load_todo():
        if TODO_FILE.exists():
            return json.loads(TODO_FILE.read_text())
        return []

    tasks = load_todo()
    
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else " "
        table.add_row(Text(f"{i}. {task['task']} {status}"))
    
    return Panel(
        table,
        title="TO DO",
        border_style="orange3",
        padding=(1, 1)
    )


def create_timetable_panel():
    return Panel(
        "timetable",
        title="TIMETABLE",
        border_style="orange3",
        padding=(1, 1)
    )


def create_currently_panel():
    reading_progress = Progress(
        TextColumn("{task.description}"),
        BarColumn(complete_style="light_goldenrod3", style="light_yellow3", bar_width=15),
        TextColumn("{task.percentage:.1f}%")
    )

    reading_progress.add_task("[italic]The Great Gatsby[/]", completed=10, total=150)

    currently_content = Group(
        Text("Reading:", style="light_goldenrod3"),
        reading_progress,
        Text(""),
        Text("Listening to:", style="light_goldenrod3"),
        Text("The Nat King Cole Story", style="italic"),
        Text(""),
        Text("Working on:", style="light_goldenrod3"),
        Text("Various projects")
    )

    return Panel(
        currently_content,
        title="CURRENTLY",
        border_style="orange3",
        padding=(1, 1)
    )


def create_pica_panel():
    pica_content = Group(
        Text("        Pica:", style="bold light_goldenrod3"),
        Text("(>'')>  You are going to win Monopoly Deal today!")
    )

    return Panel(
        pica_content,
        border_style="orange3",
        padding=(1, 1)
    )


def create_ascii_panel():

    ascii_art = r"""
        _,--',   _._.--._____
 .--.--';_'-.', ";_      _.,-'
.'--'.  _.'    {`'-;_ .-.>.'
      '-:_      )  / `' '=.
        ) >     {_/,     /~)
snd     |/               `^ .'
    """
    
    return Panel(
        Align.center(ascii_art),
        border_style="orange3",
        padding=(1, 1)
    )


def create_dashboard():
    layout = Layout()

    layout.split_column(
        Layout(name="header", size=5),
        Layout(name="body"),
        Layout(name="bottom", size=6),
        Layout(name="footer", size=3)
    )

    layout["header"].update(
        Panel(
            Align.center("[bold] Welcome, Amanda [/bold]"),
            border_style="orange3",
            padding=(1)
        )
    )

    layout["body"].split_row(
        Layout(name="left"),
        Layout(name="mid"),
        Layout(name="right")
    )
    
    layout["left"].split_row(
        Layout(create_timetable_panel()),
    )
      
 
    layout["mid"].split_column(
        Layout(create_calendar_panel()),
        Layout(create_time_panel(), size=5),
        Layout(create_ascii_panel())
    )
    
    layout["right"].split_column(
        Layout(create_currently_panel()),
        Layout(create_todo_panel())
    )

    layout["bottom"].update(
        create_pica_panel()
    )

    layout["footer"].update(
        Panel(
            "[dim]Ctrl+C to exit[/dim]",
            border_style="orange3"
        )
    )

    return layout

def main():
    try:
        with Live(create_dashboard(), refresh_per_second=1, screen=True) as live:
            while True:
                time.sleep(0.5)
                live.update(create_dashboard())
      
    except KeyboardInterrupt:
        console.print("\n[bold orange3]Dashboard closed.[/]\n")

if __name__ == "__main__":
    main()