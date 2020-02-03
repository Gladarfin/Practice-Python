#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    fill_rectangles()
    move_to_exit()


def get_width():
    width=0
    while not wall_is_on_the_right():
        move_right()
        if wall_is_on_the_right():
            break
        width+=1
    return width

def move_to_exit():
    while not wall_is_on_the_left():
        if wall_is_on_the_left():
            break
        move_left()
    while not wall_is_beneath():
        if wall_is_beneath():
            break
        move_down()


def fill_rectangles():
    field_width=get_width()
    while field_width>0:
        for i in range(field_width):
            move_down()
            fill_cell()
        if not wall_is_beneath():
            move_down()
        for i in range(field_width):
            move_left()
            fill_cell()
        if not wall_is_on_the_left():
            move_left()
        for i in range(field_width):
            move_up()
            fill_cell()
        if not wall_is_above():
            move_up()
        for i in range(field_width):
            move_right()
            fill_cell()
        if not wall_is_on_the_right():
            move_right()
        field_width-=2
        move_left()
        move_down()

if __name__ == '__main__':
    run_tasks()
