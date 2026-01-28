import json
from pathlib import Path

from rich.table import Table
from rich.text import Text
from rich.panel import Panel


EVENTS_FILE = Path(__file__).parent.parent / "data" / "events.json"

def create_upcoming_panel():
    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column(header="event")
    table.add_column(header="date")

    def load_events():
        if EVENTS_FILE.exists():
            return json.loads(EVENTS_FILE.read_text())
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