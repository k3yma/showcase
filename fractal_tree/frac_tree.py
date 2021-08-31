#!/bin/python3
import pygame as pg
import math
import random

screen_res=[500,500]
max_depth=9
min_angle_os=15
max_angle_os=30

def drawTree(x, y, angle, depth):
    if depth:
        # calculate endpoints.
        depth_scaled = (screen_res[0]/(max_depth**2 - max_depth*2)) * depth
        x1 = x + int(depth_scaled * math.sin(math.radians(angle)))
        y1 = y - int(depth_scaled * math.cos(math.radians(angle)))

        # Draw the line
        pg.draw.line(screen,(130,60,20), (x,y), (x1,y1), depth)
        # Draw left and right
        drawTree(x1,y1,angle-random.randint(min_angle_os, max_angle_os),depth-1) # Left
        drawTree(x1,y1,angle+random.randint(min_angle_os, max_angle_os),depth-1) # Right

def generateTree():
    screen.fill([255,255,255])
    drawTree(screen_res[0]/2,screen_res[1],0,max_depth)
    pg.display.flip()
    
pg.init()
screen = pg.display.set_mode(screen_res)
pg.display.set_caption("Fractal Tree")
generateTree()

# Run until the user asks to quit
running = True
while running:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        running = False
      elif event.type == pg.MOUSEBUTTONUP:
        generateTree()
        
        
pg.quit()
