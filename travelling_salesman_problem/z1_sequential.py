import numpy as np
#Podstawowa funkcja do wczytywania danych i obliczania długości ścieżki
#jest to tez algorytm zgodny z kolejnością występowania danych
def load_cities(filename):
    cities = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            city_id = int(parts[0])
            x = float(parts[1])
            y = float(parts[2])
            cities.append((city_id, x, y))
    return cities

def euclidean_distance(city1, city2):
    return np.sqrt((city1[1] - city2[1])**2 + (city1[2] - city2[2])**2)

def path_length(path, cities):
    total_distance = 0
    for i in range(len(path) - 1):
        city1 = cities[path[i] - 1]
        city2 = cities[path[i + 1] - 1]
        total_distance += euclidean_distance(city1, city2)

    city1 = cities[path[-1] - 1]
    city2 = cities[path[0] - 1]
    total_distance += euclidean_distance(city1, city2)
    return total_distance

def main():
    cities = load_cities('TSP.txt')
    sample_path = list(range(1, 101))

    length = path_length(sample_path, cities)
    print(f"Długość ścieżki: {length}")

if __name__ == '__main__':
    main()
