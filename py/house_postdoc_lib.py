#!/usr/bin/env python3
# Copyright (c) rikiya@stanford.edu 2021
# Autogenerated by SWE for Science kickstart generator - www.sweforscience.com - www.twitter.com/sweforscience

''' This is the python file that contains functions and most code for house_postdoc '''

from datetime import datetime
import logging
import math
import subprocess
import turtle

import numpy as np
from PIL import Image


log = logging.getLogger(__name__)


def _check_integer(value):
    if not isinstance(value, int):
        raise TypeError('Only integers are supported')
    return True

class MyTurtle():
    """
    Our own turtle class
    """
    def __init__(self, draw_speed):
        self.screen = turtle.Screen()
        self.screen.title("This is my house!")
        self.screen.bgcolor('honeydew') # options: 'honeydew', 'pale green', 'light green', 'green yellow'
        self.my_turtle = turtle.Turtle()
        self.my_turtle.shape('turtle')
        self.my_turtle.speed(draw_speed) # 0: fastest, 1: slowest, 6: normal, 10: second fastest

    def set_position(self, x, y):
        '''set turtle position at (x, y) without drawing a line'''
        self.my_turtle.penup()
        self.my_turtle.setposition(x, y)
        self.my_turtle.pendown()
        log.debug(f'set turtle position at ({x, y})')

    def draw_rectangle(self, x_length, y_length, line_color='blue', fill_color='cadet blue'):
        '''draw a rectangle with arbitrary size'''
        self.my_turtle.setheading(0)
        self.my_turtle.color(line_color, fill_color)
        self.my_turtle.begin_fill()
        for _ in range(2):
            self.my_turtle.forward(x_length)
            self.my_turtle.right(90)
            self.my_turtle.forward(y_length)
            self.my_turtle.right(90)
        self.my_turtle.end_fill()
        log.debug(f'draw a rectangle with a size of ({x_length, y_length})')

    def draw_triangle(self, base_length, line_color='magenta', fill_color='pink'):
        '''draw a triangle with arbitrary size'''
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
        '''draw a 2x2 window'''
        _pos = self.my_turtle.position()
        self.my_turtle.setheading(0)
        self.draw_rectangle(window_size, window_size, 'green', 'gainsboro')
        self.draw_rectangle(window_size/2, window_size/2, 'green', 'gainsboro')
        self.set_position(_pos[0]+window_size/2, _pos[1]-window_size/2)
        self.draw_rectangle(window_size/2, window_size/2, 'green', 'gainsboro')
        log.debug(f'draw a 2x2 window with a size of {window_size}')

    def draw_windows(self, num_windows):
        '''draw arbitrary number of windows'''
        if num_windows < 5:
            offset = (240-40*(num_windows))/(num_windows+1)
            for i in range(num_windows):
                self.set_position(40+(i+1)*offset+i*40, -60)
                self.draw_window(40)
        else:
            for i in range(4):
                offset = 16
                self.set_position(40+(i+1)*offset+i*40, -60-80/3)
                self.draw_window(40)
            for i in range(num_windows-4):
                offset = (240-40*(num_windows-4))/((num_windows-4)+1)
                self.set_position(40+(i+1)*offset+i*40, -20-40/3)
                self.draw_window(40)

    def draw_door(self, x_length, y_length):
        '''draw a door and a door knob'''
        _pos = self.my_turtle.position()
        self.my_turtle.setheading(0)
        self.draw_rectangle(x_length, y_length, 'dark goldenrod', 'gold')
        self.set_position(_pos[0]+15, _pos[1]-(y_length/2))
        self.my_turtle.color('tomato')
        self.my_turtle.begin_fill()
        self.my_turtle.circle(5)
        self.my_turtle.end_fill()
        log.debug(f'draw a door and a door knob')

    def draw_doors(self, num_doors):
        '''draw arbitrary number of doors'''
        offset = (240-40*num_doors)/(num_doors+1)
        for i in range(num_doors):
            self.set_position(40+(i+1)*offset+i*40, -140)
            self.draw_door(x_length=40, y_length=80)
        log.debug(f'draw arbitrary number of doors')

    def draw_garage(self, x_length=180, y_length=135):
        '''draw a garage door'''
        self.set_position(x=-165, y=-85)
        _pos = self.my_turtle.position()
        self.my_turtle.setheading(0)
        self.draw_rectangle(x_length/2, y_length, 'green', 'light yellow')
        self.set_position(_pos[0]+x_length/2, _pos[1])
        self.draw_rectangle(x_length/2, y_length, 'green', 'light yellow')
        log.debug(f'draw a garage door with a size of ({x_length, y_length})')

    def draw_clouds(self, num_clouds): # Binglan to implement
        raise NotImplementedError

    def draw_trees(self, num_trees): # Binglan to implement
        raise NotImplementedError

    def draw_house(self):
        '''draw a house'''
        self.set_position(x=40, y=-20)
        self.draw_rectangle(x_length=240, y_length=200)
        self.set_position(x=0, y=-20)
        self.draw_triangle(base_length=320)
        self.set_position(x=-190, y=-60)
        self.draw_rectangle(x_length=230, y_length=160)
        log.debug(f'draw a house')

    def draw_sun(self):
        '''draw the sun'''
        self.my_turtle.color('tomato', 'gold')
        self.set_position(x=-320, y=180)
        self.my_turtle.begin_fill()
        for _ in range(36):
            self.my_turtle.forward(100)
            self.my_turtle.left(170)
        self.my_turtle.end_fill()
        log.debug(f'draw the sun')

    def save_image(self, object_name, image_type):
        '''save the drawing as a jpg image'''
        file_name = f'tmp/{image_type}_{object_name}'
        canvas = self.screen.getcanvas()
        canvas.postscript(file= file_name+'.eps', width=800, height=600)
        img = Image.open(file_name+'.eps')
        img.save(file_name+'.jpg')
        subprocess.run(['rm', '-f', file_name+'.eps'])
        log.debug(f'save the drawing as an image in jpg format')
