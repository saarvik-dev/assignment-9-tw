from concurrent.futures import ProcessPoolExecutor
import os

def add_elements(pair):
    return pair[0] + pair[1]

def main():
    n = int(input("Enter size of vectors: "))

    print("Enter first vector:")
    a = [int(input("Enter element: ")) for _ in range(n)]

    print("Enter second vector:")
    b = [int(input("Enter element: ")) for _ in range(n)]

    # Determine number of CPU cores available
    num_workers = os.cpu_count() or 1

    # Calculate an optimal chunk size to minimize process communication overhead
    chunk_size = max(1, n // (num_workers * 4))

    # Required guard for multiprocessing in Python
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        # zip(a, b) pairs elements together: (a[0], b[0]), (a[1], b[1]), ...
        c = list(executor.map(add_elements, zip(a, b), chunksize=chunk_size))

    print("Resultant vector:", c)

if __name__ == "__main__":
    main()
