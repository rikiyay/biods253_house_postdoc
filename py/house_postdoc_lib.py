#!/usr/bin/env python3
# Copyright (c) rikiya@stanford.edu 2021
# Autogenerated by SWE for Science kickstart generator - www.sweforscience.com - www.twitter.com/sweforscience

''' This is the python file that contains functions and most code for house_postdoc '''

from datetime import datetime
import logging
import math
import subprocess
import turtle

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
        self.my_turtle.hideturtle() # hide turtle to increase drawing speed; avoid presence of turtle shadow over
        self.my_turtle.speed(draw_speed) # 0: fastest, 1: slowest, 6: normal, 10: second fastest

    def set_position(self, x, y):
        '''set turtle position at (x, y) without drawing a line'''
        self.my_turtle.penup()
        self.my_turtle.setposition(x, y)
        self.my_turtle.pendown()
        log.debug(f'set turtle position at ({x, y})')

    def draw_rectangle(self, x_length=150, y_length=120, line_color='blue', fill_color='cadet blue'):
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

    def draw_triangle(self, base_length=150, line_color='magenta', fill_color='pink'):
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

    def draw_circle(self, base_radius, line_color='LimeGreen', fill_color='DarkGreen'):
        '''draw a circle with a designated radius '''
        self.my_turtle.color(line_color, fill_color)
        self.my_turtle.begin_fill()
        self.my_turtle.circle(base_radius)
        self.my_turtle.end_fill()
        log.debug(f'draw a dot with a base radius of {base_radius}')

    def draw_dot(self, base_diameter, dot_color='SkyBlue'):
        '''draw a circle with a designated diameter using the turtle dot function '''
        self.my_turtle.dot(base_diameter, dot_color)
        log.debug(f'draw a dot with a base diameter of {base_diameter}')

    def draw_window(self, window_size=40):
        '''draw a 2x2 window'''
        _pos = self.my_turtle.position()
        self.my_turtle.setheading(0)
        self.draw_rectangle(window_size, window_size, 'green', 'gainsboro')
        self.draw_rectangle(window_size/2, window_size/2, 'green', 'gainsboro')
        self.set_position(_pos[0]+window_size/2, _pos[1]-window_size/2)
        self.draw_rectangle(window_size/2, window_size/2, 'green', 'gainsboro')
        log.debug(f'draw a 2x2 window with a size of {window_size}')

    def draw_windows(self, num_windows, pos_house, window_size=40):
        '''draw arbitrary number of windows'''
        if num_windows < int(200/window_size):
            offset = (240-window_size*num_windows)/(num_windows+1)
            for i in range(num_windows):
                self.set_position(pos_house[0]+(i+1)*offset+i*window_size, pos_house[1]-40)
                self.draw_window(window_size)
        else:
            for i in range(int(200/window_size)-1):
                offset = (240-window_size*(int(200/window_size)-1))/((int(200/window_size)-1)+1)
                self.set_position(pos_house[0]+(i+1)*offset+i*window_size, pos_house[1]-40-80/3)
                self.draw_window(window_size)
            for i in range(num_windows-(int(200/window_size)-1)):
                offset = (240-window_size*(num_windows-(int(200/window_size)-1)))/((num_windows-(int(200/window_size)-1))+1)
                self.set_position(pos_house[0]+(i+1)*offset+i*window_size, pos_house[1]-40/3)
                self.draw_window(window_size)

    def draw_door(self, x_length=40, y_length=80):
        '''draw a door and a door knob'''
        _pos = self.my_turtle.position()
        self.my_turtle.setheading(0)
        self.draw_rectangle(x_length, y_length, 'dark goldenrod', 'gold')
        self.set_position(_pos[0]+(x_length*(3/8)), _pos[1]-(y_length/2))
        self.my_turtle.color('tomato')
        self.my_turtle.begin_fill()
        self.my_turtle.circle(x_length/8)
        self.my_turtle.end_fill()
        log.debug(f'draw a door and a door knob')

    def draw_doors(self, num_doors, pos_house, x_length=40, y_length=80):
        '''draw arbitrary number of doors'''
        offset = (240-x_length*num_doors)/(num_doors+1)
        for i in range(num_doors):
            self.set_position(pos_house[0]+(i+1)*offset+i*x_length, pos_house[1]-120)
            self.draw_door(x_length=x_length, y_length=y_length)
        log.debug(f'draw arbitrary number of doors')

    def draw_garage(self, pos_house, x_length=180, y_length=135):
        '''draw a garage door'''
        self.set_position(x=pos_house[0]-205, y=pos_house[1]-65)
        _pos = self.my_turtle.position()
        self.my_turtle.setheading(0)
        self.draw_rectangle(x_length/2, y_length, 'green', 'light yellow')
        self.set_position(_pos[0]+x_length/2, _pos[1])
        self.draw_rectangle(x_length/2, y_length, 'green', 'light yellow')
        log.debug(f'draw two garage doors with a size of ({x_length, y_length})')

    def draw_cloud(self): # Binglan to implement
        '''draw one could'''
        _could_crown_size = 30
        _pos = self.my_turtle.position()
        self.draw_dot(_could_crown_size, 'Turquoise')
        self.set_position(_pos[0]+20, _pos[1])
        self.draw_dot(_could_crown_size, 'Turquoise')
        self.set_position(_pos[0]+10, _pos[1]+10)
        self.draw_dot(_could_crown_size, 'Turquoise')
        self.set_position(_pos[0]+30, _pos[1]+10)
        self.draw_dot(_could_crown_size, 'Turquoise')
        log.debug(f'draw one cloud')

    def draw_clouds(self, num_clouds): # Binglan to implement
        '''draw clouds'''
        offset_x, offset_y = 420/num_clouds, 45
        for i in range(num_clouds):
            self.set_position(-150+offset_x*i, 260) if i % 2 == 1 else self.set_position(-150+offset_x*i, 260-offset_y)
            self.draw_cloud()
        log.debug(f'draw a designated number of clouds')

    def draw_tree(self):
        '''draw one tree'''
        _tree_crown_size = 50
        _tree_width, _tree_height = 25, 70
        _pos = self.my_turtle.position()
        self.draw_rectangle(_tree_width, _tree_height, 'Black', 'SaddleBrown')
        self.set_position(_pos[0], _pos[1]-_tree_crown_size/2)
        self.draw_circle(25, 'LimeGreen', 'DarkGreen')
        self.set_position(_pos[0]+_tree_width, _pos[1]-_tree_crown_size/2)
        self.draw_circle(25, 'LimeGreen', 'DarkGreen')
        self.set_position(_pos[0]+_tree_width/2, _pos[1]-_tree_crown_size/2+_tree_crown_size/2+5)
        self.draw_circle(25, 'LimeGreen', 'DarkGreen')
        log.debug(f'draw a tree')

    def draw_trees(self, num_trees):
        '''draw a designated number of trees'''
        offset = 120/num_trees
        for i in range(num_trees):
            self.set_position(-365+offset*i, -145)
            self.draw_tree()
        log.debug(f'draw arbitrary number of doors')

    def draw_house(self, pos_house):
        '''draw a house'''
        self.set_position(x=pos_house[0], y=pos_house[1])
        self.draw_rectangle(x_length=240, y_length=200)
        self.set_position(x=pos_house[0]-40, y=pos_house[1])
        self.draw_triangle(base_length=320)
        self.set_position(x=pos_house[0]-230, y=pos_house[1]-40)
        self.draw_rectangle(x_length=230, y_length=160)
        log.debug(f'draw a house')

    def draw_sun(self, pos_sun):
        '''draw the sun'''
        self.set_position(x=pos_sun[0], y=pos_sun[1])
        self.my_turtle.color('tomato', 'gold')
        self.my_turtle.begin_fill()
        for _ in range(36):
            self.my_turtle.forward(100)
            self.my_turtle.left(170)
        self.my_turtle.end_fill()
        log.debug(f'draw the sun')

    def save_image(self, object_name, image_type, save_path):
        '''save the drawing as a jpg image'''
        '''this function is designed in a way that the program has to be run from the repo root directory'''
        file_name = f'{save_path}/{image_type}_{object_name}'
        canvas = self.screen.getcanvas()
        canvas.postscript(file= file_name+'.eps', width=800, height=600)
        img = Image.open(file_name+'.eps')
        img.save(file_name+'.jpg')
        subprocess.run(['rm', f'{file_name}.eps'])
        log.debug(f'save the drawing as an image in jpg format')
