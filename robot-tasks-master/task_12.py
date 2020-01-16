#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
    while True:
        if wall_is_beneath()==True and wall_is_above()==False:
            fill_cell()
        if wall_is_on_the_right()==True:
            break
        move_right()


if __name__ == '__main__':
    run_tasks()
