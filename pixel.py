from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



def draw_pixel(x, y,size,lineColor):
    glColor3f(*lineColor)
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()