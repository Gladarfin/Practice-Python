#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    while True:
        move_down()
        if wall_is_beneath():
            move_up()
            move_right()
            break
        move_up()
        if wall_is_on_the_left():
            move_right()
            while not wall_is_on_the_right():
                fill_cell()
                move_right()
        elif wall_is_on_the_right():
            move_left()
            while not wall_is_on_the_left():
                fill_cell()
                move_left()
        move_down()
            


if __name__ == '__main__':
    run_tasks()
