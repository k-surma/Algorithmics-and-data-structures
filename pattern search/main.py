import csv
from time import time
from naive_pattern import naive_pattern_search
from rabin_karp_pattern import rabin_karp_pattern_matching


def find_A_coordinates_and_count(pattern_matches, pattern, sample_data):
    coordinates = []
    for match in pattern_matches:
        i, j = match
        for k in range(len(pattern)):
            for m in range(len(pattern[0])):
                if pattern[k][m] == 'A' and sample_data[i + k][j + m] == 'A':
                    coordinates.append((i + k, j + m))
    return coordinates, len(pattern_matches)


def main():
    pattern = ['ABC', 'B??', 'C??']
    f = open('results2.csv', 'w')
    header = ['N', 'naive', 'fabin_f', 'rabin_hash', 'A_coordinates', 'pattern_count']
    writer = csv.writer(f, dialect='excel')
    writer.writerow(header)

    for data_size in [1000, 2000, 3000, 4000, 5000, 8000]:
        sample_data = [char for char in open(f'{data_size}_pattern.txt', 'r').read().splitlines()]

        naive_start = time()
        naive_matches = naive_pattern_search(sample_data, pattern)
        naive_end = time()
        naive_A_coords, naive_count = find_A_coordinates_and_count(naive_matches, pattern, sample_data)

        hash_time = rabin_karp_pattern_matching(sample_data, pattern)[-1]
        rabin_end = time()
        rabin_A_coords, rabin_count = find_A_coordinates_and_count(
            rabin_karp_pattern_matching(sample_data, pattern)[:-1], pattern, sample_data)

        # Print the count of coordinates and the first 10 coordinates for each file
        print(f'Data size: {data_size}')
        print(
            f'Naive pattern search found {naive_count} patterns, A coordinates count: {len(naive_A_coords)}, first 10 coordinates: {naive_A_coords[:10]}')
        print(
            f'Rabin-Karp pattern search found {rabin_count} patterns, A coordinates count: {len(rabin_A_coords)}, first 10 coordinates: {rabin_A_coords[:10]}')

        writer.writerow(
            [data_size, naive_end - naive_start, rabin_end - naive_end, hash_time, naive_A_coords[:10], naive_count])
        print(f'{data_size} processed')


if __name__ == '__main__':
    main()
