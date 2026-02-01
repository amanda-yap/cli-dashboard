from rich.align import Align
from rich.panel import Panel


def create_ascii_panel():

    ascii_art = r"""
        _,--',   _._.--._____
 .--.--';_'-.', ";_      _.,-'
.'--'.  _.'    {`'-;_ .-.>.'
      '-:_      )  / `' '=.
        ) >     {_/,     /~)
snd     |/               `^ .'
    """
    
    return Panel(
        Align.center(ascii_art),
        border_style="orange3",
        padding=(1, 1)
    )