import pandas as pd
import random
import math
import time
import matplotlib.pyplot as plt

def load_data(file_path):
    data = pd.read_csv(file_path, skiprows=1)
    items = data[['width', 'height', 'value']].values.tolist()
    return items

capacities = {
    "20_items": (20, 20),
    "100_items": (100, 100),
    "500_items": (500, 500),
    "1000_items": (1000, 1000)
}

datasets = {
    "20_items": (capacities["20_items"], load_data(r"C:\Users\User\Desktop\sem2\aisd\problem plecakowy\packages20.txt")),
    "100_items": (capacities["100_items"], load_data(r"C:\Users\User\Desktop\sem2\aisd\problem plecakowy\packages100.txt")),
    "500_items": (capacities["500_items"], load_data(r"C:\Users\User\Desktop\sem2\aisd\problem plecakowy\packages500.txt")),
    "1000_items": (capacities["1000_items"], load_data(r"C:\Users\User\Desktop\sem2\aisd\problem plecakowy\packages1000.txt"))
}

def greedy_knapsack_2d(capacity, items):
    capacity_width, capacity_height = capacity
    items_sorted = sorted(items, key=lambda item: item[2] / (item[0] * item[1]), reverse=True)
    total_value = 0
    used_width = 0
    used_height = 0

    for item in items_sorted:
        for rotation in [(item[0], item[1]), (item[1], item[0])]:
            width, height = rotation
            if used_width + width <= capacity_width and used_height + height <= capacity_height:
                total_value += item[2]
                used_width += width
                used_height += height
                break

    return total_value

def genetic_algorithm_2d(capacity, items, population_size=50, generations=100, mutation_rate=0.01):
    capacity_width, capacity_height = capacity

    def initialize_population():
        return [[random.choice([0, 1]) for _ in items] for _ in range(population_size)]

    def fitness(individual):
        total_value = 0
        total_width = 0
        total_height = 0

        for i, selected in enumerate(individual):
            if selected:
                for rotation in [(items[i][0], items[i][1]), (items[i][1], items[i][0])]:
                    width, height = rotation
                    if total_width + width <= capacity_width and total_height + height <= capacity_height:
                        total_width += width
                        total_height += height
                        total_value += items[i][2]
                        break

        return total_value

    def crossover(parent1, parent2):
        crossover_point = random.randint(0, len(parent1) - 1)
        return parent1[:crossover_point] + parent2[crossover_point:]

    def mutate(individual):
        for i in range(len(individual)):
            if random.random() < mutation_rate:
                individual[i] = 1 - individual[i]

    population = initialize_population()

    for generation in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        next_population = population[:population_size // 2]

        for i in range(population_size // 2):
            parent1 = random.choice(next_population)
            parent2 = random.choice(next_population)
            offspring = crossover(parent1, parent2)
            mutate(offspring)
            next_population.append(offspring)

        population = next_population

    best_individual = max(population, key=fitness)
    return fitness(best_individual)

def simulated_annealing_2d(capacity, items, initial_temp=1000, cooling_rate=0.95, max_iterations=1000):
    capacity_width, capacity_height = capacity

    def fitness(individual):
        total_value = 0
        total_width = 0
        total_height = 0

        for i, selected in enumerate(individual):
            if selected:
                for rotation in [(items[i][0], items[i][1]), (items[i][1], items[i][0])]:
                    width, height = rotation
                    if total_width + width <= capacity_width and total_height + height <= capacity_height:
                        total_width += width
                        total_height += height
                        total_value += items[i][2]
                        break

        return total_value

    def get_neighbor(individual):
        neighbor = individual[:]
        i = random.randint(0, len(neighbor) - 1)
        neighbor[i] = 1 - neighbor[i]
        return neighbor

    current_solution = [random.choice([0, 1]) for _ in items]
    current_fitness = fitness(current_solution)
    temp = initial_temp

    for iteration in range(max_iterations):
        new_solution = get_neighbor(current_solution)
        new_fitness = fitness(new_solution)

        if new_fitness > current_fitness:
            current_solution = new_solution
            current_fitness = new_fitness
        else:
            acceptance_probability = math.exp((new_fitness - current_fitness) / temp)
            if random.random() < acceptance_probability:
                current_solution = new_solution
                current_fitness = new_fitness

        temp *= cooling_rate

    return current_fitness

def visualize_results(results):
    for algorithm in ["Greedy", "Genetic Algorithm", "Simulated Annealing"]:
        values = [results[name][algorithm]["Value"] for name in results]
        times = [results[name][algorithm]["Time"] for name in results]
        plt.plot(list(results.keys()), values, label=f'{algorithm} Values')
        plt.plot(list(results.keys()), times, label=f'{algorithm} Times')

    plt.xlabel('Datasets')
    plt.ylabel('Values/Times')
    plt.title('Comparison of Algorithms')
    plt.legend()
    plt.show()

results = {}

for name, (capacity, items) in datasets.items():
    start_time = time.time()
    greedy_value = greedy_knapsack_2d(capacity, items)
    greedy_time = time.time() - start_time

    start_time = time.time()
    genetic_value = genetic_algorithm_2d(capacity, items)
    genetic_time = time.time() - start_time

    start_time = time.time()
    sa_value = simulated_annealing_2d(capacity, items)
    sa_time = time.time() - start_time

    results[name] = {
        "Greedy": {"Value": greedy_value, "Time": greedy_time},
        "Genetic Algorithm": {"Value": genetic_value, "Time": genetic_time},
        "Simulated Annealing": {"Value": sa_value, "Time": sa_time}
    }

results_df = pd.DataFrame(results).T

results_df.to_csv(r"C:\Users\User\Desktop\sem2\aisd\problem plecakowy\knapsack_results.csv", index=True)

print("Results saved to knapsack_results.csv")

visualize_results(results)
