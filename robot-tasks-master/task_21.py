#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    iteration = 1
    while True:
        if wall_is_on_the_left() and wall_is_beneath():
            move_right()
            break
        elif wall_is_on_the_left() and not wall_is_beneath():
            move_down()
            for i in range(iteration):
                move_right()
                fill_cell()
            move_right()
            iteration+=1
        else:
            move_down()
            for i in range(iteration):
                if not wall_is_beneath():
                    fill_cell()
                move_left()
            iteration+=1           
        

        
        
        

if __name__ == '__main__':
    run_tasks()
