import calendar
from datetime import datetime

from rich import box
from rich.align import Align
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

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