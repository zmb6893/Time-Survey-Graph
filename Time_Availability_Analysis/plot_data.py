"""
Plots the availability by the likeliehood of attending a session.
@author Zoe Bingham
"""

import turtle as t
from draw_axes import draw_and_label_axes
from process_data import read_availability
from graph_settings import *

def plot_data(schedule):
    """
    Draws circles of specified radius for each day
    """
    print("Graphing...")
    for day in schedule:
        x_cor = DAYS[day]
        times = schedule[day]
        for time in times:
            y_cor = TIMES[time]
            radius = times[time]
            t.goto(x_cor,y_cor-(.5*radius))
            draw_circle(times[time]/2.25)
            t.goto(x_cor,y_cor-(.5*radius))
            t.write(radius, font=FONT)
            
    print("Graph Complete.")

def draw_circle(radius, fill_color=COLOR):
    """
    Draws the circle to visualize likely attendance
    """
    t.fillcolor(fill_color)
    t.begin_fill()
    t.pendown()
    t.circle(radius)
    t.end_fill()
    t.penup()

def format_results(schedule):
    """
    Prints nicely formatted results
    """
    for day in schedule:
        print(day)
        times = schedule[day]
        for time in times:
            print(time + ": \t" + str(times[time]))
        print()

def main():
    schedule = read_availability()
    draw_and_label_axes()
    plot_data(schedule)
    format_results(schedule)
    input("Press enter to end program.")

if __name__ == "__main__":
    main()