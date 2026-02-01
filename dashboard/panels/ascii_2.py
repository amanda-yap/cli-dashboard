from rich.align import Align
from rich.panel import Panel

def create_ascii_panel_2():

    ascii_art = r"""


   |\---/|
   | ,_, |
    \_`_/-..----.
 ___/ `   ' ,""+ \  sk
(__...'   __\    |`.___.';
  (_,...'(_,.`__)/'.....+
    """
    
    return Panel(
        Align.center(ascii_art),
        border_style="orange3",
        padding=(1, 1)
    )