def warshall_algorithm(graph):
    n = len(graph)
    # Create a copy of the original graph
    transitive_closure = [row[:] for row in graph]
    
    # Compute the transitive closure using Warshall's algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                transitive_closure[i][j] = transitive_closure[i][j] or (transitive_closure[i][k] and transitive_closure[k][j])
    
    return transitive_closure

# Example graph represented as an adjacency matrix
graph = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

# Run the algorithm and print the result
result = warshall_algorithm(graph)
for row in result:
    print(row)
