#!/usr/bin/env python3
# Copyright (c) rikiya@stanford.edu 2021
# Autogenerated by SWE for Science kickstart generator - www.sweforscience.com - www.twitter.com/sweforscience 

''' This is the python file that contains functions and most code for house_postdoc '''

import logging
import math
import turtle

log = logging.getLogger(__name__)

def _check_integer(n):
    if not isinstance(n, int):
        raise TypeError('Only integers are supported')

class My_turtle():
    def __init__(self):
        turtle.title("This is my house!")
        self.screen = turtle.getscreen()
        self.my_turtle = turtle.Turtle()
        self.my_turtle.shape('turtle')
        self.my_turtle.speed(0) # 0: fastest, 1: slowest, 6: normal, 10: second fastest

    def set_position(self, x, y):
        '''set turtle position at (x, y) without drawing a line'''
        # _check_integer(x)
        # _check_integer(y)
        self.my_turtle.penup()
        self.my_turtle.setposition(x, y)
        self.my_turtle.pendown()
        log.debug(f'set turtle position at ({x, y})')

    def draw_rectangle(self, x_length, y_length, line_color='blue', fill_color='cadet blue'):
        '''draw a rectangle with arbitrary size'''
        # _check_integer(x_length)
        # _check_integer(y_length)
        self.my_turtle.setheading(0)
        self.my_turtle.color(line_color, fill_color)
        self.my_turtle.begin_fill()
        self.my_turtle.forward(x_length)
        self.my_turtle.right(90)
        self.my_turtle.forward(y_length)
        self.my_turtle.right(90)
        self.my_turtle.forward(x_length)
        self.my_turtle.right(90)
        self.my_turtle.forward(y_length)
        self.my_turtle.end_fill()
        log.debug(f'draw a rectangle with a size of ({x_length, y_length})')

    def draw_triangle(self, base_length, line_color='magenta', fill_color='pink'):
        '''draw a triangle with arbitrary size'''
        # _check_integer(base_length)
        self.my_turtle.setheading(0)
        self.my_turtle.color(line_color, fill_color)
        self.my_turtle.begin_fill()
        self.my_turtle.forward(base_length)
        self.my_turtle.left(135)
        self.my_turtle.forward(math.sqrt(2)*base_length/2)
        self.my_turtle.left(90)
        self.my_turtle.forward(math.sqrt(2)*base_length/2)
        self.my_turtle.end_fill()
        log.debug(f'draw a triangle with a base length of {base_length}')

    def draw_window(self, window_size):
        '''draw 2x2 windows'''
        # _check_integer(window_size)
        _pos = self.my_turtle.position()
        self.my_turtle.setheading(0)
        self.draw_rectangle(window_size, window_size, 'green', 'gainsboro')
        self.draw_rectangle(window_size/2, window_size/2, 'green', 'gainsboro')
        self.set_position(_pos[0]+window_size/2, _pos[1]-window_size/2)
        self.draw_rectangle(window_size/2, window_size/2, 'green', 'gainsboro')
        log.debug(f'draw a 2x2 window with a size of {window_size}')

    def draw_door(self, x_length, y_length):
        '''draw a door and a door knob'''
        _pos = self.my_turtle.position()
        self.my_turtle.setheading(0)
        self.draw_rectangle(x_length, y_length, 'blue', 'plum')
        self.set_position(_pos[0]+15, _pos[1]-(y_length/2))
        self.my_turtle.color('tomato')
        self.my_turtle.begin_fill()
        self.my_turtle.circle(5)
        self.my_turtle.end_fill()
        log.debug(f'draw a door and a door knob')

    def draw_garage(self, x_length, y_length):
        _pos = self.my_turtle.position()
        self.my_turtle.setheading(0)
        self.draw_rectangle(x_length/2, y_length, 'green', 'light yellow')
        self.set_position(_pos[0]+x_length/2, _pos[1])
        self.draw_rectangle(x_length/2, y_length, 'green', 'light yellow')
        log.debug(f'draw a garage door with a size of ({x_length, y_length})')

    def draw_cloud(self): # Binglan to implement
        raise NotImplementedError

    def draw_tree(self): # Binglan to implement
        raise NotImplementedError

    def draw_house(self): # Rikiya to implement
        raise NotImplementedError
