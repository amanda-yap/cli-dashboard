import json
from pathlib import Path

from rich.table import Table
from rich.text import Text
from rich.panel import Panel

PROJECT_ROOT = Path(__file__).resolve().parents[2]
GOALS_FILE = PROJECT_ROOT / "data" / "goals.json"

def create_goals_panel():
    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column()

    def load_goals():
        try:
            if GOALS_FILE.exists():
                return json.loads(GOALS_FILE.read_text())
            else:
                raise FileNotFoundError(
                    "File not found. Make sure you have copied data/goals.example.json to data/goals.json."
                )
        except json.JSONDecodeError:
            print("Invalid JSON formatting.")
            return []

    goals = load_goals()

    if len(goals) == 0:
        table.add_row(Text("No goals.", style="light_goldenrod3"))
    else:
        for goal in goals:
            row = Text()
            row.append("★ ", style="light_goldenrod3")
            row.append(goal)
            table.add_row(row)
    
    return Panel(
        table,
        title="GOALS",
        border_style="orange3",
        padding=(1, 1)
    )
