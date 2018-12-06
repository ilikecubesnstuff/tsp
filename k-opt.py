import sys
from itertools import permutations, cycle
from math import factorial
import graph

k = 0
ncr = lambda x, y: factorial(x)//(factorial(y)*factorial(x - y))

def rev(s, n):
    adj = lambda x: 1 - 2*x
    b = [adj(int(i)) for i in bin(n)[2:]]
    return [-1]*(s-len(b)) + b

def shortest(best, shortest, paths, display=False):
    global k
    start = paths.pop(0)
    for path in permutations(paths):
        for i in range(2**(k - 1)):
            r = rev(k - 1, i)
            path_list = [path[i][::r[i]] for i in range(len(path))]
            current = start + [subpath for path in path_list for subpath in path]

            # if display:
            #     graph.display_refresh()
            #     graph.display_path(best, (0, 255, 0))
            #     graph.display_path(current, (255, 255, 255))
            #     graph.display_path([start[0], path[-1][-1]], (0, 0, 255))
            #     graph.display_path([start[-1], path[0][0]], (0, 0, 255))
            #     for i in range(len(path)-1):
            #         graph.display_path([path[i][-1], path[i+1][0]], (0, 0, 255))
            #     graph.display_update()

            if graph.path_length(current) < shortest:
                best = current
                shortest = graph.path_length(current)
    return best, shortest

def subpaths(path, edges):
    global k
    paths = []
    temp = []
    for node in 2*path:
        temp.append(node)
        if not all(node != edge for edge in edges):
            paths.append(temp)
            temp = []
            continue
    return paths[1:k+1]

def edgefunc(n, k, num, shift = 0):
    if k == 1:
        return [num + shift]
    new_num = num
    edge = 0
    edge_list = [ncr(i, k - 1) for i in range(n - k, k - 2, -1)]
    if shift == 0:
        edge_list[0] = ncr(n - k - 1, k - 1)
    counter = 0
    for i in edge_list:
        if new_num - i > -1:
            new_num -= i
            counter += 1
        else:
            edge = counter
            break
    if edge == 0 and shift == 0:
        return [edge] + edgefunc(n - edge - 3, k - 1, new_num, shift = shift + edge + 2)
    return [shift + edge] + edgefunc(n - edge - 2, k - 1, new_num, shift = shift + edge + 2)

def k_opt(k_in, display=False):

    n = graph.size()
    global k
    k = k_in
    best_path = []
    best_path_length = n
    current_best = [i for i in range(n)]

    while best_path != current_best:
        best_path = current_best
        for i in range(ncr(n - k + 1, k) - ncr(n - k - 1, k - 2)):
            paths = subpaths(current_best, edgefunc(n, k, i))
            path, length = shortest(current_best, best_path_length, paths, display)
            if length < best_path_length:
                current_best = path
                best_path_length = length

            # display
            if display:
                graph.display_refresh()
                graph.display_path(best_path, (0,255,0))
                graph.display_path(current_best, (255,255,255))
                graph.display_update()

        if display:
            graph.display_refresh()
            graph.display_path(best_path, (0,255,0))
            graph.display_update()
            print(current_best, best_path_length)
    return best_path, best_path_length

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except:
        n = 100
    try:
        graph.generate_random_graph(n, display=True, seed=int(sys.argv[2]))
    except:
        graph.generate_random_graph(n, display=True)
    path, length = k_opt(2, display=True)
    print(path, length)
    graph.display_stick()
