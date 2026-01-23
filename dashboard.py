from rich.layout import Layout
from layout.header import create_header
from layout.body import create_body
from layout.footer import create_footer


def create_dashboard():
    layout = Layout()
    layout.split_column(
        create_header(),
        create_body(),
        create_footer()
    )
    return layout
