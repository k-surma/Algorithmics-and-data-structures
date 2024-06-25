#alg zachłanny
from z1_sequential import load_cities, euclidean_distance, path_length


def greedy_tsp(cities):
    num_cities = len(cities)
    visited = [False] * num_cities
    path = [0]
    visited[0] = True

    for _ in range(num_cities - 1):
        last_city = path[-1]
        next_city = None
        min_distance = float('inf')
        for i in range(num_cities):
            if not visited[i]:
                distance = euclidean_distance(cities[last_city], cities[i])
                if distance < min_distance:
                    min_distance = distance
                    next_city = i
        path.append(next_city)
        visited[next_city] = True

    return [city + 1 for city in path]

