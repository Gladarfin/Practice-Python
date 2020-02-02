#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_down(3)
    fill_even_row()
    fill_odd_row()
    fill_even_row()
    move_left(2)
    move_down()

def fill_even_row():
    while not wall_is_on_the_right():
        move_right()
        fill_cell()
        move_right()
        if wall_is_on_the_right():
            move_up()
            break
        move_right(2)

def fill_odd_row():
    while not wall_is_on_the_left():
        for i in range(3):
            fill_cell()
            move_left()
            if wall_is_on_the_left():
                fill_cell()
                move_up()
                break
        if not wall_is_on_the_left():
            move_left()

if __name__ == '__main__':
    run_tasks()
