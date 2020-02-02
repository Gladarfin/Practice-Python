#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    fill_cell()
    i = 0
    j = 0
    while not wall_is_on_the_right():
        if i < j:
            i += 1
            move_right()
        else:
            i = 0
            j += 1
            move_right()
            if not wall_is_on_the_right():
                fill_cell()


if __name__ == '__main__':
    run_tasks()
