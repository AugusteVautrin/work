from graph import Graph, graph_from_file, kruskal
import time
data_path = "input/"
file_name = "network.02.in"
#t0=time.perf_counter()
g = graph_from_file(data_path + file_name)
#q10
print(kruskal(g))