from datetime import datetime

from rich.align import Align
from rich.panel import Panel

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

def create_time_panel():
    return Panel(
        Align.center(f"[bold]{get_current_time()}[/]"),
        title="TIME",
        border_style="orange3",
        padding=(1, 2)
    )