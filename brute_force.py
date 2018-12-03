import sys
from itertools import permutations
import graph

def brute_force(display=False):

    n = graph.size()
    best_path = [i for i in range(n - 1)]
    best_path_length = n

    for path in permutations(best_path):

        # avoids duplicates
        if path[0] > path[-1]:
            continue

        # measures length
        path = list(path) + [n - 1]
        length = graph.path_length(path)

        # check / replace
        if length < best_path_length:
            best_path = path
            best_path_length = length

        # display
        if display:
            graph.display_refresh()
            graph.display_path(best_path, (0,255,0))
            graph.display_path(path, (255,255,255))
            graph.display_update()

    if display:
        graph.display_refresh()
        graph.display_path(best_path, (0,255,0))
        graph.display_update()
    return best_path, best_path_length

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except:
        n = 9
    try:
        graph.generate_random_graph(n, display=True, seed=int(sys.argv[2]))
    except:
        graph.generate_random_graph(n, display=True)
    path, length = brute_force(display=True)
    print(path, length)
