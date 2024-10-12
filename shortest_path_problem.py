import math

# Example distances between cities (city names: A, B, C, D, E, F)
distances = {
    'A': {'A': 0, 'B': 10, 'C': 19, 'D': 22, 'E': 5, 'F': 12},
    'B': {'A': 10, 'B': 0, 'C': 16, 'D': 20, 'E': 17, 'F': 14},
    'C': {'A': 19, 'B': 16, 'C': 0, 'D': 11, 'E': 18, 'F': 15},
    'D': {'A': 22, 'B': 20, 'C': 11, 'D': 0, 'E': 8, 'F': 10},
    'E': {'A': 5, 'B': 17, 'C': 18, 'D': 8, 'E': 0, 'F': 6},
    'F': {'A': 12, 'B': 14, 'C': 15, 'D': 10, 'E': 6, 'F': 0},
}

# Nearest neighbor algorithm to solve TSP (greedy approximation)
def nearest_neighbor_tsp(start_city, distances):
    visited = {start_city}  # Start by visiting the starting city
    route = [start_city]
    current_city = start_city
    total_distance = 0

    while len(visited) < len(distances):
        nearest_city = None
        # Initialize the nearest distance to an infinite value
        # This is so that the first city we check will always be closer than this
        nearest_distance = math.inf

        # Find the nearest unvisited city
        for city, distance in distances[current_city].items():
            if city not in visited and distance < nearest_distance:
                nearest_city = city
                nearest_distance = distance

        # Visit the nearest city
        if nearest_city:
            route.append(nearest_city)
            visited.add(nearest_city)
            total_distance += nearest_distance
            current_city = nearest_city

    # Return to the starting city
    total_distance += distances[current_city][start_city]
    route.append(start_city)

    return route, total_distance

# Main function
def main():
    start_city = 'A'
    route, total_distance = nearest_neighbor_tsp(start_city, distances)
    print(f"Route: {' --> '.join(route)}")
    print(f"Total distance: {total_distance}")

# Run the main function
main()
