# Data structures - Python Assignment 1 - Sorting Algorithms
import matplotlib.pyplot as plt  # For Graph generation
import math  # For mathematical operations
import time  # For running time measurment of the algorthims
import random  # For random array generation
import argparse



# The Three sorting algorithms we compare: Insertion sort, Merge Sort and Selection Sort.

# ------------------------------ Part A: Algorithm Implementation -----------------------------------------------------
# This section implements the three algorithm's functions

# Insersion sort Algorithm--------------
def insertion_sort(arr):  # The insertion sort function, receives Array
    arr_copy = arr.copy()  # Create a copy so the original list doesn't change
    for i in range(1, len(arr_copy)):  # Loop from second element to the end and compare elements
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and arr_copy[
            j] > key:  # While we are not at start/numbers in array are bigger than the key - we shift numbers accordingly and place key
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    return arr_copy  # Returning the fully sorted array


# Merge sort Algorithm (Divide and conquer)-----------------
def merge_sort(arr):  # Divide
    if len(arr) <= 1:  # The Base case: If array is already sorted we return the same array
        return arr
    mid = len(arr) // 2  # Find middle index and recuresively sort halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)  # Merge the two sorted halves


def merge(left, right):  # Conquer
    result = []  # Resulting merged list
    i = j = 0  # Pointers for left and right arrays
    while i < len(left) and j < len(right):  # Comparing the elements from both lists and add smaller one
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])  # Add remaining elements from left (if any)
    result.extend(right[j:])  # Add remaining elements from right (if any)
    return result  # Return merged sorted final list


# Selection Sort Algorithm-----------------
def selection_sort(arr):
    arr_copy = arr.copy()  # Create a copy so the original list doesn't change
    n = len(arr_copy)
    for i in range(n):  # Loop over the array
        min_index = i  # We start with i as being the current minimum element
        for j in range(i + 1, n):  # Find the smallest element in the rest of array
            if arr_copy[j] < arr_copy[min_index]:
                min_index = j
        arr_copy[i], arr_copy[min_index] = arr_copy[min_index], arr_copy[i]  # Swap with the smallest element
    return arr_copy  # Returning the fully sorted array


# ------------------------------ Part B: Comparative Experiment - Random Arrays -----------------------------------------------------
# This section compares the behavior of the 3 chosen algorithms, and produces a plot for demonstration

def calculate_stats(data):  # Function that analyzes the average runtime + deviations for the algorithms
    n = len(data)  # Number of runs/measurements
    mean_val = sum(data) / n  # Compute mean/average runtime across all measurements
    variance = sum((x - mean_val) ** 2 for x in data) / n  # Computing the variance
    std_dev = math.sqrt(variance)  # Standard deviation = sqrt of variance
    return mean_val, std_dev  # Return both average and standard deviation

def get_algorithms_by_ids(algorithm_ids):
    algorithm_map = {
        1: ("Bubble Sort", None),          # not implemented
        2: ("Selection Sort", selection_sort),
        3: ("Insertion Sort", insertion_sort),
        4: ("Merge Sort", merge_sort),
        5: ("Quick Sort", None)            # not implemented
    }

    selected = []
    for alg_id in algorithm_ids:
        if alg_id in algorithm_map:
            name, func = algorithm_map[alg_id]
            if func is not None:
                selected.append((name, func))
            else:
                print(f"Algorithm ID {alg_id} ({name}) is not implemented, skipping.")

    return selected

def experiment_B(sizes,algorithms, reps=5):  # Function that runs the measurements for the algorithms for section B
    # Dictionary where we store results for each algorithm
    results = {name: {"avg": [], "std": []} for name, _ in algorithms}
    for n in sizes:  # We measure the stats for different input sizes n (100, 500, 1000, ect...)
        for name, func in algorithms:  # for each input size in wel oop over each algorithm
            times = []  # Initializing a list in order to store runtimes for this algorithm and this input size
            for _ in range(reps):  # Here we repeat for each n input size and each algorithm to get better results
                data = [random.randint(0, 10000) for _ in range(n)]  # Random array of size n
                start_time = time.perf_counter()  # Measuring the runtime of the algorithm
                func(data)  # Run the sorting algorithm
                end_time = time.perf_counter()
                times.append(end_time - start_time)  # Store the runtime for the plot later on
            avg, std = calculate_stats(
                times)  # Once the repetitions are over, we compute the average and standard deviation
            results[name]["avg"].append(avg)  # Now we store results for plotting on the graph
            results[name]["std"].append(std)
    return results  # Returning all collected results for plotting


def add_noise(arr, noise_level):
    arr_copy = arr.copy()
    n = len(arr_copy)
    num_swaps = int(n * noise_level)

    for _ in range(num_swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]

    return arr_copy


def experiment_C(sizes, algorithms, noise_level=0.05, reps=5):
    results = {name: {"avg": [], "std": []} for name, _ in algorithms}

    for n in sizes:
        for name, func in algorithms:
            times = []
            for _ in range(reps):
                data = list(range(n))
                noisy_data = add_noise(data, noise_level)

                start_time = time.perf_counter()
                func(noisy_data)
                end_time = time.perf_counter()

                times.append(end_time - start_time)

            avg, std = calculate_stats(times)
            results[name]["avg"].append(avg)
            results[name]["std"].append(std)

    return results
# The function that generates the plot for section B
def results_graph(sizes, results,title, filename="result1.png"):
    plt.figure(figsize=(10, 6))  # Create figure with size
    for name, data in results.items():  # The data for the plot for each algorithm
        avg = data["avg"]  # The Average runtimes of the algorithms
        std = data["std"]  # The Standard deviation of the algorithms
        plt.plot(sizes, avg, marker='o', label=name)
        lower_bound = [max(0, a - s) for a, s in zip(avg, std)]
        upper_bound = [a + s for a, s in zip(avg, std)]
        plt.fill_between(sizes, lower_bound, upper_bound, alpha=0.2)
    plt.title(title)
    plt.xlabel("Array size (n)")
    plt.ylabel("Runtime (seconds)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig(filename)
    print(f"Plot saved as {filename}")  # We save the plot as png file
    plt.show()


# ---------------------------------------------------------Main/Entry point--------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sorting Algorithms Experiments")

    parser.add_argument(
        "-a",
        nargs="+",
        type=int,
        default=[2, 3, 4],
        help="Algorithms to compare: 1-Bubble, 2-Selection, 3-Insertion, 4-Merge, 5-Quick"
    )

    parser.add_argument(
        "-s",
        nargs="+",
        type=int,
        default=[100, 500, 1000, 2000, 3000],
        help="Array sizes"
    )

    parser.add_argument(
        "-e",
        type=int,
        default=1,
        help="Experiment type / noise level: 1 = 5%% noise, 2 = 20%% noise"
    )

    parser.add_argument(
        "-r",
        type=int,
        default=5,
        help="Number of repetitions"
    )

    args = parser.parse_args()

    selected_algorithms = get_algorithms_by_ids(args.a)

    if not selected_algorithms:
        print("No valid implemented algorithms were selected.")
        exit()

    noise_level = 0.05 if args.e == 1 else 0.20

    # Part B
    experiment_results_B = experiment_B(args.s, selected_algorithms, reps=args.r)
    results_graph(
        args.s,
        experiment_results_B,
        "Runtime Comparison on Random Arrays",
        "result1.png"
    )

    # Part C
    experiment_results_C = experiment_C(
        args.s,
        selected_algorithms,
        noise_level=noise_level,
        reps=args.r
    )
    results_graph(
        args.s,
        experiment_results_C,
        f"Runtime Comparison on Nearly Sorted Arrays (noise={int(noise_level * 100)}%)",
        "result2.png"
    )
