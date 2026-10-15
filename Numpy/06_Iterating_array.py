import numpy as np

# 3 samples (rows) with 2 features (columns)
X = np.array([
    [10, 20],  # Sample 0
    [30, 40],  # Sample 1
    [50, 60]   # Sample 2
])

# Iterates over axis=0 (rows)
for sample in X:
    print("Feeding to model:", sample)

# Output:
# Feeding to model: [10 20]
# Feeding to model: [30 40]
# Feeding to model: [50 60]

for index, sample in enumerate(X):
    # Imagine passing 'sample' to a model here
    print(f"Finished processing Sample ID {index}: {sample}")

# Output:
# Finished processing Sample ID 0: [10 20]
# Finished processing Sample ID 1: [30 40]
# Finished processing Sample ID 2: [50 60]

# Efficiently prints 10, 20, 30, 40, 50, 60
# print every element one by one using nditer
for value in np.nditer(X):
    print("Value:", value)