# Imports
import os
from random import seed, random
from math import sqrt
# import pygame
# from pygame.locals import *

distance = lambda x, y: sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

class Graph:

    # Graph Methods

    def generate_random_graph(self, n, **kwargs):
        try:
            seed(kwargs["seed"])
        except:
            print("CAUTION: No seed used for random graph generation. (Graph data may be lost)")
        self.vertices = [[random(), random()] for i in range(n)]
        self.d_matrix = [[distance(i, j) for j in self.vertices] for i in self.vertices]

    def size(self):
        return len(self.vertices)

    def path_length(self, path):
        return sum(self.d_matrix[path[i]][path[i + 1]] for i in range(-1, len(path) - 2))

    # Display Methods

    def display_refresh(self):
        # make screen blank
        pass

    def display_path(self):
        # draw path by connecting dots
        # pygame.draw.lines
        pass

    def display_update(self):
        # pygame.display.flip()
        pass

    def display_stick(self):
        # insert game loop
        pass

_inst = Graph()
generate_random_graph = _inst.generate_random_graph
size = _inst.size
path_length = _inst.path_length

if hasattr(os, "fork"):
    os.register_at_fork(after_in_child = _inst.start)
