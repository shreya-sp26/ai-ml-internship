import numpy as np

# Create arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("Array 1:", arr1)
print("Array 2:", arr2)

# Indexing
print("First element:", arr1[0])
print("Last element:", arr1[-1])

# Mathematical operations
print("Addition:", arr1 + arr2)
print("Subtraction:", arr2 - arr1)
print("Multiplication:", arr1 * arr2)
print("Division:", arr2 / arr1)

# Other calculations
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Maximum:", np.max(arr1))
print("Minimum:", np.min(arr1))