import calendar
import time
from datetime import datetime

from rich import box
from rich.align import Align
from rich.console import Console
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
        style="rosy_brown",
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
            day_label = Text(str(day or ""), style="rosy_brown")
            if index in (5, 6): # Different colour for weekends
                day_label.stylize("grey63")
            if day and (day, month, year) == today_tuple:
                day_label.stylize("white on deep_pink4")
            days.append(day_label)
        table.add_row(*days)

    return Panel(
        Align.center(table),
        title="CALENDAR",
        border_style="rosy_brown",
        padding=(1,1)
    )


def create_time_panel():
    return Panel(
        f"{get_current_time()}",
        title="TIME",
        border_style="rosy_brown",
        padding=(1, 2)
    )

def create_tasks_panel():
    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column()
    
    # Change to json file
    tasks = [
        "• Work on dashboard",
        "• Read",
        "• Exercise"
    ]
    
    for task in tasks:
        table.add_row(task)
    
    return Panel(
        table,
        title="📋 TODAY'S TASKS",
        border_style="rosy_brown",
        padding=(1, 1)
    )

def create_habits_panel():
    progress = Progress(
        TextColumn("{task.description}"),
        BarColumn(bar_width=15),
        TextColumn("{task.completed}/{task.total}"),
        expand=False
    )
    
    progress.add_task("Coding", completed=5, total=7)
    progress.add_task("Reading", completed=3, total=7)
    progress.add_task("Exercise", completed=2, total=7)
    
    return Panel(
        progress,
        title="PROGRESS",
        border_style="rosy_brown",
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
            "[bold] Welcome, Amanda [/bold]",
            border_style="rosy_brown",
            padding=(1)
        )
    )

    layout["body"].split_row(
        Layout(name="left"),
        Layout(create_calendar_panel()),
        Layout(name="right")
    )
    
    layout["left"].split_column(
        Layout(create_time_panel(), size=7),
        Layout(create_tasks_panel())
    )
    
    layout["right"].split_column(
        Layout(create_habits_panel())
    )

    layout["footer"].update(
        Panel(
            "[dim]Ctrl+C to exit[/dim]",
            border_style="rosy_brown"
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
        console.print("\n[bold rosy_brown]Dashboard closed.[/]\n")

if __name__ == "__main__":
    main()