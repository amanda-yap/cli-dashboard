from rich.layout import Layout
from layout.left import create_left_column
from layout.mid import create_mid_column
from layout.right import create_right_column


def create_body():
    layout = Layout(name="body")
    layout.split_row(
        create_left_column(),
        create_mid_column(),
        create_right_column()
    )
    return layout
