import itertools
import math
import time

# Function to calculate the distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Function to find the optimal solution using brute force
def tsp_brute_force(cities):
    # Calculate all possible permutations of the cities
    permutations = itertools.permutations(cities)
    # Initialize the shortest path to infinity
    shortest_path = float('inf')
    
    # Iterate over all permutations to find the shortest path
    for permutation in permutations:
        path_length = 0
        for i in range(len(permutation)-1):
            path_length += distance(permutation[i], permutation[i+1])
        path_length += distance(permutation[-1], permutation[0])  # Return to the starting city
        # Update the shortest path if the current path is shorter
        if path_length < shortest_path:
            shortest_path = path_length
            shortest_path_order = permutation
    
    return shortest_path, shortest_path_order

# Function to find the approximate solution using the nearest neighbor algorithm
def tsp_nearest_neighbor(cities):
    # Start with the first city in the list as the current city
    current_city = cities[0]
    visited_cities = [current_city]
    
    # Iterate over all cities to find the nearest neighbor
    while len(visited_cities) < len(cities):
        nearest_neighbor = None
        nearest_distance = float('inf')
        for city in cities:
            if city not in visited_cities:
                distance_to_city = distance(current_city, city)
                if distance_to_city < nearest_distance:
                    nearest_distance = distance_to_city
                    nearest_neighbor = city
        # Add the nearest neighbor to the visited cities
        visited_cities.append(nearest_neighbor)
        current_city = nearest_neighbor
    
    # Calculate the total distance of the path
    total_distance = 0
    for i in range(len(visited_cities)-1):
        total_distance += distance(visited_cities[i], visited_cities[i+1])
    total_distance += distance(visited_cities[-1], visited_cities[0])  # Return to the starting city
    
    return total_distance, visited_cities

# Generate a list of random cities
cities = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6),
          (7, 7), (8, 8), (9, 9)]

# Find the optimal solution using brute force
start_time = time.time()
optimal_path_length, optimal_path_order = tsp_brute_force(cities)
end_time = time.time()
print("Optimal path length:", optimal_path_length)
print("Optimal path order:", optimal_path_order)
print("Time taken (brute force):", end_time - start_time, "seconds")

# Find the approximate solution using the nearest neighbor algorithm
start_time = time.time()
approximate_path_length, approximate_path_order = tsp_nearest_neighbor(cities)
end_time = time.time()
print("Approximate path length:", approximate_path_length)
print("Approximate path order:", approximate_path_order)
print("Time taken (nearest neighbor):", end_time - start_time, "seconds")
