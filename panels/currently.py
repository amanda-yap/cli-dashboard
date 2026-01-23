import json
from pathlib import Path

from rich.console import Group
from rich.text import Text
from rich.panel import Panel
from rich.progress import BarColumn, Progress, TextColumn


CURRENTLY_FILE = Path(__file__).parent.parent / "data" / "currently.json"

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
