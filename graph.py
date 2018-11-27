# Imports
import os

class Graph:

    distance = lambda x, y: sqrt(x**2 + y**2)

    def __init__(self):
        pass

_inst = Graph()

if hasattr(os, "fork"):
    os.register_at_fork(after_in_child = _inst.start)
