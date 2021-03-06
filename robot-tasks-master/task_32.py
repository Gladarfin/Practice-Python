#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    colored_cells=0
    while not wall_is_on_the_right():
        if wall_is_above() and wall_is_beneath():
           fill_cell()
        move_right()
        if not wall_is_above() and not wall_is_on_the_right():
            while not wall_is_above():
                move_up()
                if cell_is_filled():
                    colored_cells+=1
                else:
                    fill_cell()
            while not wall_is_beneath():
                move_down()
    mov('ax',colored_cells)


if __name__ == '__main__':
    run_tasks()
