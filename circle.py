from pixel import draw_pixel

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_circle(r, c_x, c_y,color):
    x = 0
    y = r
    d = 1-r
    while(x<= y):
        if (d<0):
            x += 1
            d = d+ 2*x + 3
        else:
            x = x+1
            y =y-1
            d = d + 2*x -2*y + 5
        #print(x,y)
        glColor3f(*color)
        draw_pixel(x+ c_x,y+ c_y,2,color)
        draw_pixel(y+ c_x,x+ c_y,2,color)
        draw_pixel(y+ c_x,-x+ c_y,2,color)
        draw_pixel(x+ c_x,-y+ c_y,2,color)
        draw_pixel(-x+ c_x,-y+ c_y,2,color)
        draw_pixel(-y+ c_x,-x+ c_y,2,color)
        draw_pixel(-y+ c_x,x+ c_y,2,color)
        draw_pixel(-x+ c_x,y+ c_y,2,color)