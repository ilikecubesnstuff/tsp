import sys
from itertools import permutations
from math import factorial
import graph

k = 0
ncr = lambda x, y: factorial(x)//(factorial(y)*factorial(x - y))

def shortest(best, shortest, vertices, display=False):
    path_vertices = [best[i] for i in vertices]
    for case in permutations(path_vertices):
        current = best[:]
        for i in range(len(vertices)):
            current[vertices[i]] = case[i]

        if display:
            graph.display_refresh()
            graph.display_path(best, (0, 255, 0))
            graph.display_path(current, (255, 255, 255))
            graph.display_update()

        if graph.path_length(current) < shortest:
            best = current
            shortest = graph.path_length(current)
    return best, shortest

def choose(n, k, num, shift = 0):
    if k == 1:
        return [num + shift]
    edge_list = [ncr(i, k - 1) for i in range(n - 1, k - 2, -1)]
    edge = 0
    for i in edge_list:
        if num - i < 0:
            break
        num -= i
        edge += 1
    return [shift + edge] + choose(n - edge - 1, k - 1, num, shift = shift + edge + 1)

def k_point_opt(k_in, display=False):

    n = graph.size()
    global k
    k = k_in
    best_path = []
    best_path_length = n
    current_best = [i for i in range(n)]
    while best_path != current_best:
        best_path = current_best
        for i in range(ncr(n, k)):
            vertices = choose(n, k, i)
            path, length = shortest(current_best, best_path_length, vertices, display)
            if length < best_path_length:
                current_best = path
                best_path_length = length
        if display:
            graph.display_refresh()
            graph.display_path(best_path, (0, 255, 0))
            graph.display_path(current_best, (0, 0, 255))
            graph.display_update()
            print(current_best, best_path_length)
    return best_path, best_path_length

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except:
        n = 50
    try:
        graph.generate_random_graph(n, display=True, seed=int(sys.argv[2]))
    except:
        graph.generate_random_graph(n, display=True)
    path, length = k_point_opt(2, display=True)
    print(path, length)
    graph.display_stick()
