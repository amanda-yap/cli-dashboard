import time
from rich.console import Console
from rich.live import Live

from dashboard import create_dashboard


console = Console()

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