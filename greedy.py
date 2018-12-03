import sys
import graph

def greedy(display=False):

    n = graph.size()
    path = [0, 0]
    path_length = 0
    vertices = [i for i in range(1, n)]

    for i in range(n - 1):
        min_node = 0
        min_dist = 1.5

        # searches for closes vertex
        for j in vertices:
            length = graph.edge_length(path[-1], j)
            if length < min_dist:
                min_node = vertices.index(j)
                min_dist = length

            # display
            if display:
                graph.display_refresh()
                graph.display_path(path, (0,255,0))
                graph.display_path([path[-1], j], (255,255,255))
                graph.display_update()

        # appends closest distance to path list
        path.append(vertices.pop(min_node))
        path_length += min_dist

    return path, path_length + graph.edge_length(path[-1], path[0])

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except:
        n = 80
    try:
        graph.generate_random_graph(n, display=True, seed=int(sys.argv[2]))
    except:
        graph.generate_random_graph(n, display=True)
    path, length = greedy(display=True)
    print(path, length)
    graph.display_stick()
