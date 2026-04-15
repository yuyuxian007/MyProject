"""
File: Steeplechase.py
Name: Haoyu Wang
---------------------------------
Haoyu Wang
"""

from karel.stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()

def jump():
    up()
    move()
    down()

def up():
    """
    Pre:Karel faces east.
    Post:Karel faces east.
    """
    turn_left()
    while not right_is_clear():
        move()
    turn_right()

def down():
    """
    Pre:Karel faces east.
    Post:Karel faces east.
    """
    turn_right()
    while front_is_clear():
        move()
    turn_left()


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
