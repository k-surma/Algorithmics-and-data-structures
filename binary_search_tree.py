import time
import random
import numpy as np
import math

class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if not self.value:
            self.value = value
            return
        if self.value == value:
            return
        if value < self.value:
            if self.left:
                self.left.insert(value)
                return
            self.left = Node(value)
            return
        if self.right:
            self.right.insert(value)
            return
        self.right = Node(value)

    def min(self):
        node = self
        while node.left is not None:
            node = node.left
        return node.value

    def max(self):
        node = self
        while node.right is not None:
            node = node.right
        return node.value

    def search(self, value):
        if value == self.value:
            return True
        if value < self.value:
            if self.left is None:
                return False
            return self.left.search(value)
        if self.right is None:
            return False
        return self.right.search(value)

    def printer(self, level=0, is_right=False):
        if is_right:
            print(' ' * 4, (level - 1) * 5 * ' ', end='', sep='')
        print('-' * level, self.value, end='', sep='')
        if len(str(self.value).split('.')[1]) == 1:
            print(' ', end='', sep='')
        if self.left:
            self.left.printer(level + 1)
        if self.right:
            self.right.printer(level + 1, is_right=self.left is not None)
        if not self.left and not self.right:
            print()

class TreeArray:
    def __init__(self, length=11):
        self.length = length
        self.array = [Node(i) for i in np.arange(start=0.5, stop=length + 0.5, step=1)]

    def insert(self, value):
        return self.array[math.floor(value)].insert(value)

    def minimum(self, value):
        return self.array[math.floor(value)].min()

    def maximum(self, value):
        return self.array[math.floor(value)].max()

    def check(self, value):
        return self.array[math.floor(value)].search(value)

    def print_trees(self):
        for node in self.array:
            if node.left is not None or node.right is not None:
                node.printer()

def main():
    elements_to_insert = [1.3, 1.5, 1.6, 3.7, 4.0, 4.99, 7.3, 7.7, 7.6, 7.9, 9.3]
    tree_array = TreeArray()
    for element in elements_to_insert:
        tree_array.insert(element)
    tree_array.print_trees()

    num_elements = [5, 10, 25, 50, 100, 500, 1000]
    for number in num_elements:
        elements = [random.uniform(0.5, 10.5) for _ in range(number)]

        start_time = time.perf_counter()
        for element in elements:
            tree_array.minimum(element)
        end_time = time.perf_counter()
        print(f"Czas potrzebny na funkcje min dla {number} elementow: {end_time - start_time} sekund")

        start_time = time.perf_counter()
        for element in elements:
            tree_array.maximum(element)
        end_time = time.perf_counter()
        print(f"Czas potrzebny na funkcje max dla {number} elementow: {end_time - start_time} sekund")

        start_time = time.perf_counter()
        for element in elements:
            tree_array.check(element)
        end_time = time.perf_counter()
        print(f"Czas potrzebny na funkcje search dla {number} elementow: {end_time - start_time} sekund")
        print("---------------------------------------------------------")

if __name__ == '__main__':
    main()
