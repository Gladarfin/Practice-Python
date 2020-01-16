#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    while True:
        if wall_is_above()==False:
            move_up()
            fill_cell()
            move_down()
        if wall_is_beneath()==False:
            move_down()
            fill_cell()
            move_up()
        if wall_is_beneath()==wall_is_above()==True:
            fill_cell()
        if wall_is_on_the_right()==True:
            break
        move_right()


if __name__ == '__main__':
    run_tasks()
