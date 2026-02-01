from rich.layout import Layout
from dashboard.panels.picca import create_picca_panel

def create_footer():
    return Layout(create_picca_panel(), name="footer", size=6)
