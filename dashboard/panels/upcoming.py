import json
from pathlib import Path

from rich.table import Table
from rich.text import Text
from rich.panel import Panel


PROJECT_ROOT = Path(__file__).resolve().parents[2]
EVENTS_FILE = PROJECT_ROOT / "data" / "events.json"

def create_upcoming_panel():
    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column(header="event")
    table.add_column(header="date")

    def load_events():
        try:
            if EVENTS_FILE.exists():
                return json.loads(EVENTS_FILE.read_text())
            else:
                raise FileNotFoundError(
                    "File not found. Make sure you have copied data/events.example.json to events/todo.json."
                )
        except json.JSONDecodeError:
            print("Invalid JSON formatting.")
            return []

    events = load_events()

    if len(events) == 0:
        table.add_row(Text("No upcoming events.", style="light_goldenrod3"))
    else:
        for event in events:
            table.add_row(Text(f"- {event['event']}"), Text(event['date'], style="light_goldenrod3"))
    
    return Panel(
        table,
        title="UPCOMING",
        border_style="orange3",
        padding=(1, 1)
    )