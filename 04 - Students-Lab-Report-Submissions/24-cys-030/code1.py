import numpy as np

arr = np.array([[0, 1], [2, 3]])
print("Original flattened array:")
print(arr)

flattened = arr.flatten()

max_val = np.max(flattened)
min_val = np.min(flattened)

print("Maximum value of the above flattened array:", max_val)
print("Minimum value of the above flattened array:", min_val)