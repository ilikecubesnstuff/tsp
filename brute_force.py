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
        length = graph.path_length(list(path) + [n - 1])

        # check / replace
        if length < best_path_length:
            best_path = path
            best_path_length = length

    return graph.path_length(best_path)

if __name__ == "__main__":
    p = brute_force(graph.generate_random_graph(10, display=True))
    print(p)
