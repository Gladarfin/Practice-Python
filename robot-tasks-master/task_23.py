#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    steps_to_right=1
    move_right()
    while True:
        if not wall_is_above():
            move_and_fill_up()
        if not wall_is_on_the_right():
            move_right()
            steps_to_right+=1
        if wall_is_on_the_right():
            break
    if not wall_is_above():
        move_and_fill_up()
    move_left(steps_to_right)
         
def move_and_fill_up():
    while not wall_is_above():
            move_up()
            fill_cell()
    while not wall_is_beneath():
            move_down()

if __name__ == '__main__':
    run_tasks()
