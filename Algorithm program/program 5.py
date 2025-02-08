import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency list for the graph
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

# Create a NetworkX graph and add edges
G = nx.Graph()
for node in graph:
    for neighbor in graph[node]:
        G.add_edge(node, neighbor)

# Draw the graph
plt.figure(figsize=(6, 4))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
plt.show()

# BFS function
def bfs(graph, start_node):
    visited = []  # List for visited nodes
    queue = []  # Initialize a queue

    visited.append(start_node)
    queue.append(start_node)

    print("Breadth-First Search Traversal:")

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Run BFS
bfs(graph, '5')
