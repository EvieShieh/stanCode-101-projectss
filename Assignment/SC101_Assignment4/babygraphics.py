"""
File: babygraphics.py
Name: Evie
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    interval = width / len(YEARS)
    x_coordinate = year_index * interval
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # top line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       GRAPH_MARGIN_SIZE)
    # bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    for index in range(len(YEARS)):
        x_dis = get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, index)
        canvas.create_line(GRAPH_MARGIN_SIZE + x_dis, GRAPH_MARGIN_SIZE,
                           GRAPH_MARGIN_SIZE + x_dis, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
        canvas.create_text(GRAPH_MARGIN_SIZE + x_dis, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[index], anchor='nw')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #
    y_interval = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE) / MAX_RANK
    color_index = 0
    for name in lookup_names:
        if name in name_data:
            color = COLORS[color_index]
            color_index += 1
            if color_index >= len(COLORS):
                color_index = 0  # loop color
            d = name_data[name]
            x_start = 0
            y_start = 0
            for year_index in range(len(YEARS)):
                x_end = GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, year_index)
                year = str(YEARS[year_index])
                if year in d:
                    rank = int(d[year])
                    text = name + " " + str(rank)
                    y_end = GRAPH_MARGIN_SIZE + y_interval * (rank - 1)
                else:
                    rank = MAX_RANK
                    text = name + " *"
                    y_end = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                if year_index != 0:
                    # not the 1st index in YEARS, draw line
                    canvas.create_line(x_start, y_start, x_end, y_end, fill=color)
                canvas.create_text(x_end, y_end, text=text, anchor='sw', fill=color)
                # save the start position
                x_start = x_end
                y_start = y_end


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
