from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

# global variables
data = []
N = 20  # size of data
i = j = 0
swapping = False
reset = False
bar_width = 0.8


def init():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glColor3f(1.0, 1.0, 1.0)
    gluOrtho2D(0, N, 0, 1)
    generate_data()


def display():
    global reset
    glClear(GL_COLOR_BUFFER_BIT)
    if reset:
        generate_data()
        reset = False
    draw_data()
    glutSwapBuffers()


def draw_data():
    for k in range(N):
        x = k + 0.1
        y = data[k]
        if swapping and (k == j or k == j+1):
            glColor3f(1.0, 0.0, 0.0)  # set color to red if being compared
        elif k > N - i - 1:
            glColor3f(0.0, 1.0, 0.0)  # set color to green if in final position
        else:
            glColor3f(1.0, 1.0, 1.0)  # set color to white otherwise
        glRectf(x, 0, x + bar_width, y)


def generate_data():
    global data
    data = [random.uniform(0, 1) for _ in range(N)]


def bubble_sort():
    global i, j, swapping
    if i < N - 1:
        if j < N - i - 1:
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapping = True
            j += 1
            glutPostRedisplay()
            time.sleep(0.05)
        else:
            i += 1
            j = 0
    else:
        swapping = False
        glutSetWindowTitle("Bubble Sort Complete")


def keyboard(key, x, y):
    global reset, swapping, i, j
    if key == b'a' and not swapping:
        i = j = 0
        glutIdleFunc(bubble_sort)
    elif key == b'r':
        reset = True
        swapping = False
        glutPostRedisplay()


def main():
    glutInit()
    glutInitWindowSize(700, 700)
    glutCreateWindow("Bubble Sort")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()


if __name__ == '__main__':
    main()
