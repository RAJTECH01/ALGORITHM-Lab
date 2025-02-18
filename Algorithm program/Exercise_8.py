import matplotlib.pyplot as plt
import networkx as nx
import pylab
G = nx.Graph()
nodes_list = [1, 2, 3, 4, 5,6, 7]
G.add_nodes_from(nodes_list)
edges_list = [(1, 2, 1), (1, 4, 4), (2, 3, 2), (2, 4, 6), (2, 5, 4), (3, 5, 5),
(3, 6, 6), (4, 5, 3), (4, 7, 4), (5, 6, 8), (5, 7, 7), (6, 7, 3)]
G.add_weighted_edges_from(edges_list)
pos=nx.spring_layout(G)
pylab.figure(1)
nx.draw(G,pos, with_labels= 'true')
nx.draw_networkx_edge_labels(G,pos)
mst = nx.minimum_spanning_tree(G, algorithm='prim')
print(sorted(mst.edges(data=True)))
