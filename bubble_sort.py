from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GLUT.fonts import GLUT_BITMAP_HELVETICA_12
import random
import time
import numpy as np
import winsound

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
        self.num_comparisons = 0
        self.start_time = 0
        self.end_time = 0
        self.time_taken = 0
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
        self.draw_stats()
        glutSwapBuffers()

    def draw_data(self):
        for k in range(self.N):
            x = k + 0.1
            y = self.data[k]
            if self.sorting_completed or k >= self.N - self.i:
                glColor3f(0.0, 1.0, 0.0)
            elif self.swapping and (k == self.j or k == self.j + 1):
                glColor3f(1.0, 0.0, 0.0)
            elif self.sorting_completed is False or self.reset:
                glColor3f(1.0, 1.0, 1.0)
            glRectf(x, 0, x + self.bar_width, y)

    def draw_stats(self):
        glColor3f(1.0, 1.0, 1.0)
        text = "Time taken: {:.2f}s, Comparisons: {}".format(self.time_taken, self.num_comparisons)
        glRasterPos2f(0.5, 0.95)
        for char in text:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))

    def generate_data(self):
        self.data = [random.uniform(0.1, 1) for _ in range(self.N)]
        self.sorting_completed = False
        self.num_comparisons = 0

    def bubble_sort(self):
            if self.i == 0 and self.j == 0:
                self.start_time = time.time()  # start time calculation

            if self.i < self.N - 1:
                if self.j < self.N - self.i - 1:
                    self.num_comparisons += 1
                    if self.data[self.j] > self.data[self.j + 1]:
                        self.data[self.j], self.data[self.j +
                                                    1] = self.data[self.j + 1], self.data[self.j]
                        self.swapping = True
                        freq = 1000 + int(self.data[self.j] * 500)  # calculate frequency based on bar height
                        duration = 100  # in milliseconds
                        winsound.Beep(freq, duration)  # play sound
                    self.j += 1
                else:
                    self.i += 1
                    self.j = 0
                time.sleep(0.05)
            else:
                self.swapping = False
                self.sorting_completed = True
                self.end_time = time.time()  # end time calculation
                self.time_taken = round(self.end_time - self.start_time, 2)
                glutSetWindowTitle(
                    "Bubble Sort Complete (Time Taken: {} s)".format(self.time_taken))
                glutIdleFunc(None)
                self.draw_data()
            glutPostRedisplay()


    def keyboard(self, key, x, y):
        if key == b'a' and not self.swapping:
            self.i = self.j = 0
            glutIdleFunc(self.bubble_sort)
        elif key == b'r':
            self.reset = True
            self.i = self.j = 0
            self.swapping = False
            self.sorting_completed = False
            glutSetWindowTitle("Bubble Sort")
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
