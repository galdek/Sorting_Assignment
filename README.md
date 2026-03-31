# Data Structures - Python Assignment 1 - Sorting Algorithms

# Students:
Gal Dekel & Ziv Goldstein 

# Selected Algorithms:
- Insertion Sort  
- Merge Sort  
- Selection Sort  

## Results – Part B (Random Arrays)

![Result 1](result1.png)

### Explanation

The graph shows the running times of the three algorithms on random arrays of increasing sizes.

- **Insertion Sort** and **Selection Sort** both grow much faster than Merge Sort as the input size increases.  
  This is expected because their time complexity is \(O(n^2)\).

- **Merge Sort** grows much more slowly.  
  Its time complexity is \(O(n \log n)\), making it more efficient for larger inputs.

- Between the two quadratic algorithms, **Insertion Sort** is usually slightly faster than Selection Sort in practice, especially for smaller inputs.

---
