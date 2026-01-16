import calendar
import time
from datetime import datetime

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.progress import BarColumn, Progress, TextColumn
from rich.table import Table
from rich.text import Text

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


def create_agenda_panel():
    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column()
    
    # Change to json file
    tasks = [
        "• Work on dashboard",
        "• Exercise"
    ]
    
    for task in tasks:
        table.add_row(task)
    
    return Panel(
        table,
        title="AGENDA",
        border_style="orange3",
        padding=(1, 1)
    )


def create_done_panel():
    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column()
    
    # Change to json file
    finished_tasks = [
        "• Read",
        "• Practise piano"
    ]
    
    for task in finished_tasks:
        table.add_row(task)
    
    return Panel(
        table,
        title="DONE",
        border_style="orange3",
        padding=(1, 1)
    )


def create_currently_panel():
    reading_progress = Progress(
        TextColumn("{task.description}"),
        BarColumn(complete_style="light_goldenrod3", style="light_yellow3", bar_width=15),
        TextColumn("{task.percentage:.1f}%")
    )

    reading_progress.add_task("[italic]The Iliad[/]", completed=406, total=429)
    reading_progress.add_task("[italic]The Great Gatsby[/]", completed=0, total=150)

    currently_content = Group(
        Text("Reading:", style="light_goldenrod3"),
        reading_progress,
        Text(""),
        Text("Listening to:", style="light_goldenrod3"),
        Text("The Nat King Cole Story", style="italic"),
        Text(""),
        Text("Working on:", style="light_goldenrod3"),
        Text("Brushing up my coding skills")
    )

    return Panel(
        currently_content,
        title="CURRENTLY",
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
    
    layout["left"].split_column(
        Layout(create_agenda_panel()),
        Layout(create_done_panel())
    )
 
    layout["mid"].split_column(
        Layout(create_calendar_panel()),
        Layout(create_time_panel(), size=5),
        Layout(create_ascii_panel())
    )
    
    layout["right"].split_column(
        Layout(create_currently_panel())
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