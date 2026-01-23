import json
from pathlib import Path

from rich.table import Table
from rich.text import Text
from rich.panel import Panel

TODO_FILE = Path(__file__).parent.parent / "data" / "todo.json"

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
