"""
File: draw_line.py
Name: Evie
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# constant
SIZE = 10

# Global variables
window = GWindow()
circle_object = GOval(SIZE, SIZE)
odd_click = True


def draw(mouse):
    global odd_click, circle_object
    if odd_click:
        circle = GOval(SIZE, SIZE)
        circle.filled = False
        circle.color = 'darkblue'
        window.add(circle, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        circle_object = circle
        odd_click = False
    else:
        line = GLine(circle_object.x, circle_object.y, mouse.x, mouse.y)
        window.remove(circle_object)
        window.add(line)
        odd_click = True


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


if __name__ == "__main__":
    main()
