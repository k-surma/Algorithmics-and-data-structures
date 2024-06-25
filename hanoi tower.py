import time

# Wieża hanoi rekurencyjnie
def hanoi_recursion(n, source, destination, buff, moves=0):
    if n==1 :
        #print("Move disk 1 from source", source, "to destination", destination)
        return moves + 1
    moves=hanoi_recursion (n-1, source, buff, destination, moves)
    #print("Move disk", n, "from source", source, "to destination", destination)
    moves=hanoi_recursion (n-1, buff, destination, source, moves+1)
    return moves


# Wieża hanoi iteracyjnie
def hanoi_iterative(n):
    source = list(range(n, 0, -1))
    destination = []
    buff = []
    moves = 0
    total_moves = 2 ** n - 1

    if n % 2 == 0:
        source, destination = destination, source

    while moves < total_moves:

        move_disk(source, destination, 'source', 'destination')
        moves += 1
        if moves >= total_moves: break

        move_disk(source, buff, 'source', 'buff')
        moves += 1
        if moves >= total_moves: break

        move_disk(buff, destination, 'buff', 'destination')
        moves += 1

    print(f"Wymagana liczba kroków: {moves}")


def move_disk(source, target, source_name, target_name):
    if source and (not target or source[-1] < target[-1]):
        disk = source.pop()
        target.append(disk)
        #print(f"Przenieś krążek {disk} z {source_name} do {target_name}")
    elif target and (not source or target[-1] < source[-1]):
        disk = target.pop()
        source.append(disk)
        #print(f"Przenieś krążek {disk} z {target_name} do {source_name}")


def main():

    # komentarz: zahashowałam printy w powyższych funkcjach, żeby czas kompilacji był krótszy
    # (przy bardzo dużych liczbach bardzo długi czas oczekiwania)
    # oraz aby łatwiej można było porównać wyniki
    n=10
    start1=time.time()
    print(f"Wymagana liczba kroków {hanoi_recursion(n,"A","C","B")}")
    end1=time.time()
    print(f"Szybkość działania rekurencyjnie: {end1 - start1}")
    start2=time.time()
    hanoi_iterative(n)
    end2=time.time()
    print(f"Szybkość działania iteracyjnie: {end2 - start2}")



if __name__ == "__main__":
    main()