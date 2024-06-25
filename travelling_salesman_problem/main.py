from z1_sequential import *
from greedy import *
from simulated_annealing import *
import time
def main():
    cities = load_cities('TSP.txt')

    print("Algorytm zgodny z kolejnością w pliku z danymi")
    start_time = time.time()
    sequential_path = list(range(1, len(cities) + 1))
    sequential_path_length = path_length(sequential_path, cities)
    end_time = time.time()
    print(f"Długość ścieżki zgodnej z kolejnością w pliku: {sequential_path_length}")
    print(f"Czas wykonania: {end_time - start_time} sekund")

    print("Algorytm zachłanny:")
    start_time = time.time()
    greedy_path = greedy_tsp(cities)
    greedy_path_length = path_length(greedy_path, cities)
    end_time = time.time()
    print(f"Długość ścieżki algorytmu zachłannego: {greedy_path_length}")
    print(f"Czas wykonania: {end_time - start_time} sekund")

    print("Algorytm probabilistyczny Symulowanego Wyżarzania:")
    initial_temp = 10000
    cooling_rate = 0.995
    max_iter = 10000
    start_time = time.time()
    best_path, best_length = simulated_annealing(cities, initial_temp, cooling_rate, max_iter)
    end_time = time.time()
    print(f"Długość ścieżki algorytmu wyżarzania: {best_length}")
    print(f"Czas wykonania: {end_time - start_time} sekund")

if __name__ == '__main__':
    main()