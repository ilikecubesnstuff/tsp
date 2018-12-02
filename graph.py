# Imports
import os
from random import seed, random
from math import sqrt
import pygame
from pygame.locals import *

distance = lambda x, y: sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

class Graph:

    # Graph methods

    def generate_random_graph(self, n, display=False, **kwargs):

        try:
            seed(kwargs["seed"])
        except:
            print("CAUTION: No seed used for random graph generation. (Graph data may be lost)")

        self.vertices = [[random(), random()] for i in range(n)]
        self.d_matrix = [[distance(i, j) for j in self.vertices] for i in self.vertices]

        if display:
            pygame.init()
            self.screen = pygame.display.set_mode((500,500))
            pygame.display.set_caption("TSP - %s node graph"%(self.size()))

    def size(self):
        return len(self.vertices)

    def path_length(self, path):
        return sum(self.d_matrix[path[i]][path[i + 1]] for i in range(-1, len(path) - 1))

    # Display methods

    def display_refresh(self):
        self.screen.fill((0,0,0))
        for vertex in self.vertices:
            pygame.draw.circle(self.screen, (255, 255, 255), (int(vertex[0]*500), int(vertex[1]*500)), 5)

    def display_path(self, path, color, loop=True):
        pygame.draw.lines(self.screen, color, loop, [(int(self.vertices[i][0]*500), int(self.vertices[i][1]*500)) for i in path])

    def display_update(self):
        pygame.display.flip()

    def display_stick(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

_inst = Graph()
# Graph methods
generate_random_graph = _inst.generate_random_graph
size = _inst.size
path_length = _inst.path_length
# Display methods
display_refresh = _inst.display_refresh
display_path = _inst.display_path
display_update = _inst.display_update
display_stick = _inst.display_stick

if hasattr(os, "fork"):
    os.register_at_fork(after_in_child = _inst.start)
