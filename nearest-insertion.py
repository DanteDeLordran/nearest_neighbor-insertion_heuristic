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

num_points = len(matrix)
start_point = 0
path = [start_point]
unvisited = list(range(1, num_points))

while unvisited:
    best_insertion = None
    min_insertion_cost = float('inf')

    for neighbor in unvisited:
        for i in range(len(path)):
            current_point = path[i]

            next_point = path[(i + 1) % len(path)]
            print('Next point ' + str(next_point))
            insertion_cost = (matrix[current_point][neighbor] +
                              matrix[neighbor][next_point] -
                              matrix[current_point][next_point])
            print('Current cost ' + str(insertion_cost))

            if insertion_cost < min_insertion_cost:
                min_insertion_cost = insertion_cost
                best_insertion = (neighbor, i)
                print('Current minimum insertion cost ' + str(insertion_cost)) 

    # Insert the point with the minimum insertion cost
    path.insert(best_insertion[1] + 1, best_insertion[0])
    print('Current path ', " -> ".join(map(str, path)))
    unvisited.remove(best_insertion[0])

path.append(start_point)
print("Final path :", " -> ".join(map(str, path)))