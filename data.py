import random
import time
import graph

from brute_force import brute_force
from greedy import greedy
from edge_opt import edge_opt
from point_opt import point_opt

start = time.time()
file1 = open("data/edge_opt.txt", "a")
file2 = open("data/point_opt.txt", "a")
vmin = 52
vmax = 100
dt = 60

for n in range(vmin, vmax+1):
    for k in range(2, 3):
        c = 0
        t = time.time()
        while time.time() - t < dt and c < 100:
            s = random.random()
            graph.generate_random_graph(n, seed = s)
            st = time.time()
            path, length_history = edge_opt(k)
            file1.write(str(s)+" "+str(n)+" "+str(k)+" "+str(time.time()-st)+" "+",".join(str(d) for d in length_history)+"\n")
            st = time.time()
            c += 1
        c = 0
        print(n, ":", k, "completed in", time.time()-t, "seconds.")
        t = time.time()
        while time.time() - t < dt and c < 100:
            s = random.random()
            graph.generate_random_graph(n, seed = s)
            st = time.time()
            path, length_history = point_opt(k)
            file2.write(str(s)+" "+str(n)+" "+str(k)+" "+str(time.time()-st)+" "+",".join(str(d) for d in length_history)+"\n")
            c += 1
        print(n, ":", k, "completed in", time.time()-t, "seconds.")
file1.close()
file2.close()
print("Completed in", time.time()-start, "seconds.")
