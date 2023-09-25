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

# Creating a list of size of points in matrix full of False to track visited points
visited = [False] * num_points
start_point = 0
current_point = start_point

# Marking first visited array value as True because it is our starting point
visited[current_point] = True
path = [current_point]

# Loops while there are not visited points
while False in visited:
    nearest_neighbor = None
    min_distance = float('inf')

    for neighbor in range(num_points):
        print('Neighbor number ' + str(neighbor))
        if not visited[neighbor] and matrix[current_point][neighbor] < min_distance:
            nearest_neighbor = neighbor
            print('Nearest neighbor ' + str(nearest_neighbor))
            min_distance = matrix[current_point][neighbor]
            print('Shortest distance ' + str(min_distance))

    if nearest_neighbor is not None:
        current_point = nearest_neighbor
        print('Point ' + str(current_point) + ' is the nearest')
        visited[current_point] = True
        path.append(current_point)
        print('Current path ', " -> ".join(map(str, path)))

path.append(start_point)
print("Final path :", " -> ".join(map(str, path)))
