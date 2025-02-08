import networkx as nx
import matplotlib.pyplot as plt

# Define adjacency list for the graph
g = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

# Create a NetworkX graph and add edges
G = nx.Graph()
for node in g:
    for neighbor in g[node]:
        G.add_edge(node, neighbor)

# Draw the graph
plt.figure(figsize=(6, 4))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
plt.show()

# DFS function
def dfs(visited, g, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in g[node]:
            dfs(visited, g, neighbour)

# Driver Code
print("Following is the Depth-First Search:")
visited = set()  # Ensure a fresh visited set
dfs(visited, g, '5')
