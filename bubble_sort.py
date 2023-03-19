from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

class BubbleSortVisualizer:
    def __init__(self, N):
        self.N = N
        self.data = []
        self.i = 0
        self.j = 0
        self.swapping = False
        self.sorting_completed = False
        self.reset = False
        self.bar_width = 0.8

    def init(self):
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glColor3f(1.0, 1.0, 1.0)
        gluOrtho2D(0, self.N, 0, 1)
        self.generate_data()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        if self.reset:
            self.generate_data()
            self.reset = False
        self.draw_data()
        glutSwapBuffers()

    def draw_data(self):
        for k in range(self.N):
            x = k + 0.1
            y = self.data[k]
            if self.sorting_completed or k >= self.N - self.i:
                glColor3f(0.0, 1.0, 0.0)
            elif self.swapping and (k == self.j or k == self.j + 1):
                glColor3f(1.0, 0.0, 0.0)
            else:
                glColor3f(1.0, 1.0, 1.0)
            glRectf(x, 0, x + self.bar_width, y)


    def generate_data(self):
        self.data = [random.uniform(0, 1) for _ in range(self.N)]

    def bubble_sort(self):
        if self.i < self.N - 1:
            if self.j < self.N - self.i - 1:
                if self.data[self.j] > self.data[self.j + 1]:
                    self.data[self.j], self.data[self.j + 1] = self.data[self.j + 1], self.data[self.j]
                    self.swapping = True
                self.j += 1
            else:
                self.i += 1
                self.j = 0
            time.sleep(0.05)
        else:
            self.swapping = False
            self.sorting_completed = True
            glutSetWindowTitle("Bubble Sort Complete")
            glutIdleFunc(None)  
            self.draw_data() 
        glutPostRedisplay()

    def keyboard(self, key, x, y):
        if key == b'a' and not self.swapping:
            self.i = self.j = 0
            glutIdleFunc(self.bubble_sort)
        elif key == b'r':
            self.reset = True
            self.swapping = False
            glutPostRedisplay()

def main():
    N = 20
    visualizer = BubbleSortVisualizer(N)
    glutInit()
    glutInitWindowSize(700, 700)
    glutCreateWindow("Bubble Sort")
    visualizer.init()
    glutDisplayFunc(visualizer.display)
    glutKeyboardFunc(visualizer.keyboard)
    glutMainLoop()

if __name__ == '__main__':
    main()
