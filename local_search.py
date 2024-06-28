import numpy as np

data = np.array([
    [0, 89, 87, 38, 33, 71, 59, 54],
    [89, 0, 32, 59, 65, 39, 45, 61],
    [87, 32, 0, 50, 75, 17, 64, 79],
    [38, 59, 50, 0, 40, 33, 50, 56],
    [33, 65, 75, 40, 0, 62, 26, 21],
    [71, 39, 17, 33, 62, 0, 57, 70],
    [59, 45, 64, 50, 26, 57, 0, 16],
    [54, 61, 79, 56, 21, 70, 16, 0]
])

init_tour = [0, 1, 2, 3, 4, 5, 6, 7]


def calculate_distance(tour: list, distance_matrix: np.ndarray) -> int:
    return sum(distance_matrix[tour[i - 1]][tour[i]] for i in range(len(tour)))


def local_search(tour: list, matrix: np.ndarray, strategy='best') -> list:
    while True:
        best_distance = calculate_distance(tour, matrix)
        for i in range(len(tour) - 1):
            for j in range(i + 2, len(tour) + (i > 0)):
                if j == len(tour):
                    j = 0
                new_tour = tour.copy()
                new_tour[i + 1:j + 1] = reversed(tour[i + 1:j + 1])  # this creates a new tour by reversing a section
                new_distance = calculate_distance(new_tour, matrix)
                if new_distance < best_distance:
                    tour = new_tour  # make this the new current tour
                    best_distance = new_distance
                    if strategy == 'first':
                        break  # if strategy is first found, break the loop after finding an improvement
            if strategy == 'first' and calculate_distance(tour.copy(), matrix) < best_distance:
                break
        if best_distance == calculate_distance(tour, matrix):
            break  # if no improvement was found, end the algorithm
    return tour


print("Initial tour:", init_tour)
print("Initial distance:", calculate_distance(init_tour, data))

best_found = local_search(init_tour, data, 'best')
print("Best found tour:", best_found)
print("Best found distance:", calculate_distance(best_found, data))

first_found = local_search(init_tour, data, 'first')
print("First found tour:", first_found)
print("First found distance:", calculate_distance(first_found, data))
