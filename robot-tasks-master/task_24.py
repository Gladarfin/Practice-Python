#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    move_down()
    move_right()
    cross_fill()

def cross_fill():
    for i in range(3):
        for j in range(3):
            if i%2==0 and j%2!=0:
                fill_cell()
            elif i%2!=0:
                fill_cell()
            move_right()
        move_left(j+1)
        move_down()
    move_up(i+1)
        
            

        
if __name__ == '__main__':
    run_tasks()
