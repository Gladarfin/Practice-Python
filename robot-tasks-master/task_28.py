#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    filled_cell_count=0
    while filled_cell_count<5:
        if cell_is_filled():
            filled_cell_count+=1
        if filled_cell_count<5:
            move_right()
        



if __name__ == '__main__':
    run_tasks()
