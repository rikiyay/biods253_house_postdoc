#!/usr/bin/env python3
# Copyright (c) rikiya@stanford.edu 2021
# Autogenerated by SWE for Science kickstart generator - www.sweforscience.com - www.twitter.com/sweforscience 

''' This is the main command line interface for house_postdoc. '''

import argparse
import logging
import sys
import time

import house_postdoc_lib

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='house_postdoc')
    # parser.add_argument('-i', '--interactive', default=False, action='store_true', help='enable interactive mode')
    parser.add_argument('-w', '--num_windows', default=4, choices=range(1, 9), type=int, help='number of the windows')
    # parser.add_argument('-g', '--num_garages', default=1, choices=[1], type=int, help='number of the garage doors')
    parser.add_argument('-d', '--num_doors', default=1, choices=range(1, 6), type=int, help='number of the doors')
    parser.add_argument('-t', '--num_trees', default=3, choices=range(1, 6), type=int, help='number of the trees')
    parser.add_argument('-c', '--num_clouds', default=5, choices=range(1, 10), type=int, help='number of the clouds')
    parser.add_argument('-s', '--draw_speed', default=0, choices=range(0, 11), type=int, help='0: fastest, 1: slowest, 3: slow, 6: normal, 10: fast')
    parser.add_argument('-v', '--verbose', default=False, action="store_true",
                        help="print details")
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.INFO if not args.verbose else logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("debug.log"),
            logging.StreamHandler()
        ]
    )

    # if args.interactive:
    #     answer1 = input('would you like to start? (y/n)')
    #     if answer1 = 'yes' or answer1 == 'y':

    logging.info('starting up!')
    logging.debug(f'n_window is {args.num_windows}, n_door is {args.num_doors}, \
        n_tree is {args.num_trees}, n_cloud is {args.num_clouds}')

    # initialize My_turtle class object
    my_turtle = house_postdoc_lib.My_turtle(draw_speed=args.draw_speed)
    # set up window and screen to draw a house
    WIDTH, HEIGHT = 800, 600
    my_turtle.screen.setup(WIDTH + 8, HEIGHT + 8)

    # house
    my_turtle.draw_house()
    # windows
    my_turtle.draw_windows(args.num_windows)
    # door
    my_turtle.draw_doors(args.num_doors)
    # garage
    my_turtle.draw_garage()
    # tree
    # my_turtle.draw_trees(args.num_trees)
    # cloud
    # my_turtle.draw_clouds(args.num_clouds)
    # sun
    my_turtle.draw_sun()

    my_turtle.my_turtle.hideturtle()
    time.sleep(5)
    sys.exit(0)