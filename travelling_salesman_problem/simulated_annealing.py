#alg probabilistyczny
import random
import math
from z1_sequential import load_cities, euclidean_distance, path_length

def simulated_annealing(cities, initial_temp, cooling_rate, max_iter):
    def get_neighbor(path):
        new_path = path.copy()
        i, j = random.sample(range(len(new_path)), 2)
        new_path[i], new_path[j] = new_path[j], new_path[i]
        return new_path

    current_path = list(range(1, len(cities) + 1))
    current_length = path_length(current_path, cities)
    best_path = current_path
    best_length = current_length
    temperature = initial_temp

    for iteration in range(max_iter):
        new_path = get_neighbor(current_path)
        new_length = path_length(new_path, cities)
        if new_length < current_length or random.uniform(0, 1) < math.exp((current_length - new_length) / temperature):
            current_path = new_path
            current_length = new_length
            if new_length < best_length:
                best_path = new_path
                best_length = new_length
        temperature *= cooling_rate

    return best_path, best_length

