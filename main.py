from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


from board import Board 

backgColor = [0.0, 0.0, 0.0, 0.0]

HEIGHT = 500
WIDTH = HEIGHT

board  = Board(dim_size=10,num_bombs=5,width=WIDTH)
   
def showScreen():
    global  backgColor
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(*backgColor)
    board.renderBoard()
    glFlush()

def init():
    glViewport(0, 0, HEIGHT, WIDTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WIDTH,  0,HEIGHT)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    
def mouseListener(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        y= HEIGHT - y
        board.click(click_x=x,click_y=y) 
        glutPostRedisplay()
       
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(WIDTH, HEIGHT)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutMouseFunc(mouseListener)
init()
glutMainLoop()












