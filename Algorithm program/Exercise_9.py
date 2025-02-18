INF = float('inf')

def floyd_algorithm(graph):
    n = len(graph)
    dist = [[INF for j in range(n)] for i in range(n)]
    
    # Initialize the distance matrix
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# Sample input
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

# Run the algorithm and print the result
result = floyd_algorithm(graph)
for row in result:
    print(row)
