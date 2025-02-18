import networkx as nx
import matplotlib.pyplot as plt

# Create an empty Undirected Weighted Graph
G = nx.Graph()

# Add nodes
nodes_list = [1, 2, 3, 4, 5, 6, 7]
G.add_nodes_from(nodes_list)

# Add weighted edges
edges_list = [(1, 2, 13), (1, 4, 4), (2, 3, 2), (2, 4, 6), (2, 5, 4),
              (3, 5, 5), (3, 6, 6), (4, 5, 3), (4, 7, 4), (5, 6, 8), 
              (5, 7, 7), (6, 7, 3)]
G.add_weighted_edges_from(edges_list)

# Plot the graph using a spring layout
plt.figure()
pos = nx.spring_layout(G)
weight_labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, font_color='white', node_shape='s', with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weight_labels)

# Plot the graph using a planar layout
plt.figure()
pos = nx.planar_layout(G)
nx.draw(G, pos, font_color='white', node_shape='s', with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weight_labels)

# Compute shortest paths from node 1 using the weights of edges
p1 = nx.shortest_path(G, source=1, weight="weight")

# Shortest path from node 1 to node 6
p1to6 = nx.shortest_path(G, source=1, target=6, weight="weight")

# Length of the shortest path from node 1 to node 6
length = nx.shortest_path_length(G, source=1, target=6, weight="weight")

# Print the results
print("All shortest paths from 1: ", p1)
print("Shortest path from 1 to 6: ", p1to6)
print("Length of the shortest path: ", length)

# Show the plots
plt.show()
