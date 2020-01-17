#!/usr/bin/python3
"""Криво-косо но работает"""
from pyrob.api import *


@task
def task_8_29():
    escaped=False
    while not wall_is_on_the_left():
        if not wall_is_above():
            move_up()
            escaped=True
            break
        move_left()       
    else:
        while not wall_is_on_the_right():
            if not wall_is_above():
                move_up()
                escaped=True
                break
            if wall_is_on_the_right():
                break
            move_right()
        while not wall_is_above():
            move_up()
            escaped=True
        if escaped:   
            while not wall_is_on_the_left():
                move_left()
    


if __name__ == '__main__':
    run_tasks()
