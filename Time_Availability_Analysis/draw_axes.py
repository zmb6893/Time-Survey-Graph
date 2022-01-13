"""
Draw the axes for the schedule graphing program.
@author: Zoe Bingham
"""

import turtle as t
from graph_settings import *

def draw_axes(bot_right, top_left):
    """
    Draw the axes with the provided labels
    """
    t.tracer(False)
    corners = [bot_right,top_left]
    for location in corners:
        t.penup()
        t.goto(ORIGIN)
        t.pendown()
        t.goto(location)
    t.penup()

def label_axes(horizontal, vertical):
    """
    Label the axes with the provided locations
    """
    # Horizontal axes
    for label in horizontal:
        t.goto(-350, horizontal[label])
        t.write(label)
    
    # Vertical axes
    for label in vertical:
        t.goto(vertical[label], -320)
        t.write(label)

def draw_and_label_axes(bot_right=BOT_RIGHT, top_left=TOP_LEFT, times=TIMES, days=DAYS):
    """
    Draws and labels the axes with the provided information.
    """
    draw_axes(bot_right, top_left)
    label_axes(times,days)

def main():
    draw_and_label_axes()
    input("")

if __name__ == "__main__":
    main()