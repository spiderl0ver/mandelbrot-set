import cmath
from graphics import *
import colorsys
import math
def mandelbrot(c,iterations=1):
    f = 0**2 + c
    t = 0
    for i in range(iterations):
        f = f*f + c
        if not cmath.isnan(f):
            t +=1
    return f,t/iterations
screenwidth = 444
screenheight = 444
density = 100
win = GraphWin("mandelbrot",screenwidth,screenheight)
win.setCoords(screenwidth/-2,screenheight/-2,screenwidth/2,screenheight/2)
for r in range(screenwidth):
    r = (r-(screenwidth/2))/density
    for i in range(screenheight):
        i = (i-(screenheight/2))/density
        output = mandelbrot(complex(r,i),100)
        if cmath.isnan(output[0]):
            color = colorsys.hsv_to_rgb(output[1]*3.6,1,1)
            color = [math.ceil(color[0])*255,math.ceil(color[1])*255,math.ceil(color[2])*255]
            win.plot(r*density,i*density,color_rgb(color[0],color[1],color[2]))

        else:
            win.plot(r*density,i*density,"black")
