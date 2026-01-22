import calendar
import time
from datetime import datetime
import json
from pathlib import Path
import getpass

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
EVENTS_FILE =  Path(__file__).with_name("events.json")
CURRENTLY_FILE =  Path(__file__).with_name("currently.json")


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
                day_label.stylize("light_yellow3 on dark_red")
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
    
    for task in tasks:
        status = "✓" if task["done"] else " "
        table.add_row(Text(f"- {task['task']} {status}"))
    
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

    def load_current():
        if CURRENTLY_FILE.exists():
            return json.loads(CURRENTLY_FILE.read_text())
        return {}

    current_data = load_current()

    reading_progress = Progress(
        TextColumn("{task.description}"),
        BarColumn(complete_style="light_goldenrod3", style="light_yellow3", bar_width=15),
        TextColumn("{task.percentage:.1f}%")
    )

    for book in current_data["books"]:
        reading_progress.add_task(book["name"], completed = book["pages_read"], total = book["total_pages"])

    currently_content = Group(
        Text("Reading:", style="light_goldenrod3"),
        reading_progress,
        Text(""),
        Text("Listening to:", style="light_goldenrod3"),
        Text(f"{current_data["music"]}", style="italic"),
        Text(""),
        Text("Working on:", style="light_goldenrod3"),
        Text(f"{current_data["working_on"]}")
    )

    return Panel(
        currently_content,
        title="CURRENTLY",
        border_style="orange3",
        padding=(1, 1)
    )


def create_upcoming_panel():
    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column(header="event")
    table.add_column(header="date")

    def load_events():
        if EVENTS_FILE.exists():
            return json.loads(EVENTS_FILE.read_text())
        return []

    events = load_events()
    
    for event in events:
        table.add_row(Text(f"- {event['event']}"), Text(event['date'], style="light_goldenrod3"))
    
    return Panel(
        table,
        title="UPCOMING",
        border_style="orange3",
        padding=(1, 1)
    )

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

def create_ascii_panel_2():

    ascii_art = r"""


   |\---/|
   | ,_, |
    \_`_/-..----.
 ___/ `   ' ,""+ \  sk
(__...'   __\    |`.___.';
  (_,...'(_,.`__)/'.....+
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
        Layout(name="footer", size=6)
    )

    layout["header"].update(
        Panel(
            Align.center(f"[bold]{getpass.getuser()}'s dashboard [/bold]"),
            border_style="orange3",
            padding=(1)
        )
    )

    layout["body"].split_row(
        Layout(name="left"),
        Layout(name="mid"),
        Layout(name="right")
    )
    
    layout["left"].split_column(
        Layout(create_todo_panel()),
        Layout(create_ascii_panel_2())
    )
      
 
    layout["mid"].split_column(
        Layout(create_calendar_panel()),
        Layout(create_time_panel(), size=5),
        Layout(create_ascii_panel())
    )
    
    layout["right"].split_column(
        Layout(create_currently_panel()),
        Layout(create_upcoming_panel())
    )

    layout["footer"].update(
        create_picca_panel()
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