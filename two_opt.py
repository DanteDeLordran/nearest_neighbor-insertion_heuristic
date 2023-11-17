import numpy as np

matrix = np.array([
    [0, 89, 87, 38, 33, 71, 59, 54],
    [89, 0, 32, 59, 65, 39, 45, 61],
    [87, 32, 0, 50, 75, 17, 64, 79],
    [38, 59, 50, 0, 40, 33, 50, 56],
    [33, 65, 75, 40, 0, 62, 26, 21],
    [71, 39, 17, 33, 62, 0, 57, 70],
    [59, 45, 64, 50, 26, 57, 0, 16],
    [54, 61, 79, 56, 21, 70, 16, 0]
])

init_tour = [0,1,2,3,4,5,6,7]

def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i+1]]
    total_distance += distance_matrix[route[-1]][route[0]]
    return total_distance

def two_opt(route, distance_matrix):
    best_route = route
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]
                if calculate_total_distance(new_route, distance_matrix) < calculate_total_distance(best_route, distance_matrix):
                    best_route = new_route
                    improvement = True
        route = best_route
    return best_route

# Test the function with a random distance matrix

print("Initial tour:", init_tour)
print("Initial distance:", calculate_total_distance(init_tour, matrix))

optimized_route = two_opt(init_tour, matrix)

print("Optimized route:", optimized_route)
print("Optimized total distance:", calculate_total_distance(optimized_route, matrix))
