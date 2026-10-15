import numpy as np

#4 samples (rows) with 2 features columns: age, weight
dataset = np.array([
    [25, 60], # Person 0
    [30, 75], # Person 1
    [22, 55], # Person 2
    [35, 80]  # Person 3
])

#splitting horizontally (across rows) at row index 3
train_data , test_data = np.split(dataset, [3])

print("Train data (first 3 rows)")
print(train_data)

print("\nTest data (from row 3 onwards)")
print(test_data)

#----------------------------------------------

# 5 samples, 1 feature
X = np.array([10, 20, 30, 40, 50])

# Split into 3 batches
batches = np.array_split(X, 3)

print("Batch 1:", batches[0]) # [10 20]  (Size 2)
print("Batch 2:", batches[1]) # [30 40]  (Size 2)
print("Batch 3:", batches[2]) # [50]     (Size 1 - taking the leftover)

#-----------------------------------------------------

# 3 samples, 3 columns total
raw_data = np.array([
    [25, 60, 1], 
    [30, 75, 0], 
    [22, 55, 1]  
])

# Split vertically (across columns) at column index 2
X, y = np.hsplit(raw_data, [2])

print("Features (X):")
print(X)
# [[25 60]
#  [30 75]
#  [22 55]]

print("\nLabels (y):")
print(y)
# [[1]
#  [0]
#  [1]]