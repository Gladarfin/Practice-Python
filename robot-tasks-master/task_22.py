#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    even_or_odd_row = 1
    while True:
        if wall_is_on_the_left() and wall_is_beneath() and cell_is_filled():
            break
        elif even_or_odd_row % 2 !=0:
            while not wall_is_on_the_right():
                fill_cell()
                move_right()
            fill_cell()
            if not wall_is_beneath():
                move_down()
        even_or_odd_row=2
        while not wall_is_on_the_left():
            fill_cell()
            move_left()
        fill_cell()
        if not wall_is_beneath():
            move_down()
        even_or_odd_row = 1


if __name__ == '__main__':
    run_tasks()
