from PIL import Image
import cmath
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
screenwidth = int(16000)#1920
screenheight = int(screenwidth/1.777777777777777777777)
img  = Image.new( mode = "RGB", size = (screenwidth, screenheight), color = (0, 255, 100) )
imagoffset = 0
realoffset = -0.76
density = int(35* screenwidth/111)


graph = []
index = 0
for r in range(screenwidth):
    r = (r-(screenwidth/2))/density
    for i in range(screenheight):
        index+=1
        i = (i-(screenheight/2))/density
        output = mandelbrot(complex(r+realoffset,i+imagoffset),100)
        if cmath.isnan(output[0]):
            color = colorsys.hsv_to_rgb(output[1]*3.6,1,1)
            color = [math.ceil(color[0])*200,math.ceil(color[1])*130,math.ceil(color[2])*180]
            graph.append((color[0],color[1],color[2]))

        else:
            graph.append((0,0,0))
print(1)
pixels = img.load() # create the pixel map
index = 0
for i in range(img.size[0]): # for every pixel:
    for j in range(img.size[1]):

        pixels[i,j] = (graph[index])
        index+=1
img.show()
