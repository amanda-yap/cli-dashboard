import time
from rich.console import Console
from rich.layout import Layout
from rich.live import Live

from dashboard.layout.header import create_header
from dashboard.layout.body import create_body
from dashboard.layout.footer import create_footer

console = Console()

def create_dashboard():
    layout = Layout()
    layout.split_column(
        create_header(),
        create_body(),
        create_footer()
    )
    return layout


def run_dashboard():
    with Live(create_dashboard(), refresh_per_second=1, screen=True) as live:
        while True:
            time.sleep(0.5)
            live.update(create_dashboard())


def main():
    try:
        run_dashboard()
    except KeyboardInterrupt:
        console.print("\n[bold orange3]Dashboard closed.[/]\n")


if __name__ == '__main__':
    main()