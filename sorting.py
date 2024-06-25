import random
import time



#algorytm sortowania przez wstawianie
def InsertionSort(A: list) -> list:
    for i in range(len(A)):
        x: int = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j + 1] = A[j]
            j-=1
        A[j + 1] = x
    return A


#algorytm sortowania przez scalanie
def merge(A: list, B: list) -> list:
    i, j =0, 0
    result: list=[]
    while (i < len(A) and j < len(B)):
        if B[j]>A[i]:
            result.append(A[i])
            i+=1
        else:
            result.append(B[j])
            j+=1
    while i<len(A):
        result.append(A[i])
        i+=1
    while j<len(B):
        result.append(B[j])
        j+=1

    return result


def MergeSort(L) -> list:
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = MergeSort(L[:mid])
    right = MergeSort(L[mid:])

    return merge(left,right)


def time_complexity(algorithm, iterations, length, max_number) ->None:
    start = time.time()
    max_time=0
    min_time=0
    sorted_array=[]
    for i in range(iterations):
        arr=[random.randint(0, max_number) for _ in range(length)]
        start_1 = time.time()
        exec=algorithm(arr)
        end_1 = time.time()
        max_time=max(max_time, end_1 - start_1)
        min_time=min(min_time, end_1 - start_1)
        if i==0:
            sorted_array=exec
    end=time.time()
    full_time=end-start
    avg_time=full_time/iterations

    print(f"""
For algorithm: {algorithm.__name__}
- Execution time of all iterations: {full_time}
- Time of the slowest iteration: {max_time}
- Time of the fastest iteration: {min_time}
- Average time of an iteration: {avg_time}""")



def main():
    n=10
    max_nr=100
    i=10000
    time_complexity(algorithm=MergeSort, iterations=i, length=n, max_number=max_nr)
    time_complexity(algorithm=InsertionSort, iterations=i, length=n, max_number=max_nr)




if __name__ == '__main__':
    main()