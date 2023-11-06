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

def calculate_distance(tour, distance_matrix):
    """Calculate the total distance of the tour."""
    return sum(distance_matrix[tour[i-1]][tour[i]] for i in range(len(tour)))

def two_opt(tour, distance_matrix, strategy='best'):
    """Apply 2-OPT to improve the tour."""
    while True:
        best_distance = calculate_distance(tour, distance_matrix)
        for i in range(len(tour) - 1):
            for j in range(i+2, len(tour) + (i>0)):
                if j == len(tour): j = 0  # wrap around to the beginning
                new_tour = tour[:]
                new_tour[i+1:j+1] = reversed(tour[i+1:j+1])  # this creates a new tour by reversing a section
                new_distance = calculate_distance(new_tour, distance_matrix)
                if new_distance < best_distance:  # if the new tour is shorter
                    tour = new_tour  # make this the new current tour
                    best_distance = new_distance
                    if strategy == 'first':
                        break  # if strategy is first found, break the loop after finding an improvement
            if strategy == 'first' and new_distance < best_distance:
                break
        if best_distance == calculate_distance(tour, distance_matrix):
            break  # if no improvement was found, end the algorithm
    return tour

print("Initial tour:", init_tour)
print("Initial distance:", calculate_distance(init_tour, matrix))

bf_tour = two_opt(init_tour, matrix, 'best')
print("Best found tour:", bf_tour)
print("Best found distance:", calculate_distance(bf_tour, matrix))

ff_tour = two_opt(init_tour, matrix, 'first')
print("First found tour:", ff_tour)
print("First found distance:", calculate_distance(ff_tour, matrix))
