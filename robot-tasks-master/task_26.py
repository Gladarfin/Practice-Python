#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    while not wall_is_on_the_right() and not wall_is_beneath():
        fill_odd_row()
        fill_even_row()
        fill_odd_row()
        skip_row()
        if wall_is_on_the_left() and wall_is_beneath():
            move_up(2)
            break
        

def fill_odd_row():
    while not wall_is_on_the_right():
        move_right()
        fill_cell()
        move_right()
        if wall_is_on_the_right() and not wall_is_beneath():
            move_down()
            break
        elif wall_is_beneath() and wall_is_on_the_right():
            break
        move_right(2)

def fill_even_row():
    while not wall_is_on_the_left():
        for i in range(3):
            fill_cell()
            move_left()
            if wall_is_on_the_left():
                fill_cell()
                move_down()
                break
        if not wall_is_on_the_left():
            move_left()

def skip_row():
    while not wall_is_on_the_left():
        move_left()
        if wall_is_on_the_left() and not wall_is_beneath():
            move_down()
            break
        elif wall_is_on_the_left() and wall_is_beneath():
            break

        
if __name__ == '__main__':
    run_tasks()
