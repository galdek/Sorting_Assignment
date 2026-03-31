# Data Structures - Python Assignment 1 - Sorting Algorithms

# Students:
Gal Dekel & Ziv Goldstein 

# Selected Algorithms:
- Insertion Sort  
- Merge Sort  
- Selection Sort  

## Results – Part B (Random Arrays)

![Result 1](result1.png)

### Explanation of graph results

The graph shows the running times of the three algorithms on random arrays of increasing sizes.  
Each experiment was repeated multiple times for every array size, and the average running time and standard deviation were calculated.

- **Insertion Sort** and **Selection Sort** both grow much faster than Merge Sort as the input size increases.  
  This is expected because their time complexity is \(O(n^2)\).

- **Merge Sort** grows much more slowly than the other two algorithms.  
  Its time complexity is \(O(n \log n)\), making it significantly better for large inputs.


