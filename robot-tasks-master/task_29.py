#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    filled_cell_in_a_row=0
    while not wall_is_on_the_right():
        if cell_is_filled():
            filled_cell_in_a_row+=1
        elif not cell_is_filled():
            filled_cell_in_a_row=0
        if filled_cell_in_a_row==3:
            break
        move_right()
        
            
            


if __name__ == '__main__':
    run_tasks()
