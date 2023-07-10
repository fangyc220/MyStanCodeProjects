"""
File: babygraphics.py
Name: Steven
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
    count_width = width - GRAPH_MARGIN_SIZE*2
    each_step = count_width / len(YEARS)

    return each_step * year_index + GRAPH_MARGIN_SIZE


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=2, fill='black')  # 頂端的線
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=2, fill='black')  # 底端的線

    for i in range(len(YEARS)):
        get_x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(get_x, 0, get_x, CANVAS_HEIGHT, width=2, fill='black')
        canvas.create_text(get_x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW,
                           fill='black', font='15')


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
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    get_color_index = 0
    for name in lookup_names:
        for i in range(len(YEARS)-1):
            text = ''
            # 得到線段的第1個點, 確認某名字在某年份是否有rank, 若沒有, 則在線上的y座標應為最底端(設為CANVAS_HEIGHT-GRAPH_MARGIN_SIZE）
            # 得到每個年份的資料text, 並且把text使用canvas.create_text新增標籤
            if str(YEARS[i]) in name_data[name]:
                # 若某名字在某年份有rank(<1000), 則抓取它的rank並且轉換成canvas的比例
                get_rank = (int(name_data[name][str(YEARS[i])]) *
                            (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/MAX_RANK) + GRAPH_MARGIN_SIZE
                text = str(name) + ' ' + str(name_data[name][str(YEARS[i])])
            else:
                get_rank = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                text = str(name) + ' *'

            # 得到x座標(年份)
            get_x = get_x_coordinate(CANVAS_WIDTH, i)

            # 新增標籤
            canvas.create_text(get_x + TEXT_DX, get_rank, text=text, anchor=tkinter.SW,
                               fill=COLORS[get_color_index], font='10')

            # 得到線段的第2個點, 確認某名字在某年份是否有rank, 若沒有則在線上的y應為最底端(設為CANVAS_HEIGHT-GRAPH_MARGIN_SIZE）
            if str(YEARS[i+1]) in name_data[name]:
                # 若某名字在某年份有rank(<1000), 則抓取它的rank並且轉換成canvas的比例尺
                get_rank_next_point = (int(name_data[name][str(YEARS[i+1])]) *
                                       (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/MAX_RANK) + GRAPH_MARGIN_SIZE
            else:
                get_rank_next_point = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            # 得到x座標(年份)
            get_x_next_point = get_x_coordinate(CANVAS_WIDTH, i+1)

            # 集合第1點與第2點，劃出線
            canvas.create_line(get_x, get_rank, get_x_next_point, get_rank_next_point, width=LINE_WIDTH,
                               fill=COLORS[get_color_index])

            # 處理最後一個年份(最後一個年份的資料標籤要額外新增一次)
            if i == len(YEARS)-2:
                if str(YEARS[i]) in name_data[name]:
                    text = str(name) + ' ' + str(name_data[name][str(YEARS[i+1])])
                else:
                    text = str(name) + ' *'
                canvas.create_text(get_x_next_point+TEXT_DX, get_rank_next_point, text=text, anchor=tkinter.SW,
                                   fill=COLORS[get_color_index], font='10')

        if get_color_index == len(COLORS)-1:
            get_color_index = 0
        else:
            get_color_index += 1


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
