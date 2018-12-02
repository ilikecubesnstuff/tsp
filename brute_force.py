from itertools import permutations
import graph
import time

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
        # print(path, length)

        # check / replace
        if length < best_path_length:
            best_path = path
            best_path_length = length

        # display
        graph.display_refresh()
        graph.display_path(best_path, (0,255,0))
        graph.display_path(path, (255,255,255))
        graph.display_update()
        # time.sleep(2)

    graph.display_refresh()
    graph.display_path(best_path, (0,255,0))
    graph.display_update()
    return best_path

if __name__ == "__main__":
    graph.generate_random_graph(9, display=True, seed=3198)
    p = brute_force(display=True)
    print(p, graph.path_length(p))
    graph.display_stick()
