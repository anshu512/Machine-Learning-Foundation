import numpy as np

# 3 samples (rows) and 2 features (columns)
X = np.array([
    [10, 2],  # Sample 0
    [5,  8],  # Sample 1
    [15, 4]   # Sample 2
])

# Max value per feature (column)
print(np.max(X, axis=0)) 
# [15  8]  <- 15 is max of column 1, 8 is max of column 2

# Min value per feature (column)
print(np.min(X, axis=0)) 
# [5  2]

# Global max (rarely used in ML)
print(np.max(X)) 
# 15

# Sum across columns to get a total per sample (row)
print(np.sum(X, axis=1)) 
# [12 13 19] <- (10+2), (5+8), (15+4)

# Sum across rows to get a total per feature (column)
print(np.sum(X, axis=0)) 
# [30 14]

# Total sum of the entire batch
print(np.sum(X)) 
# 44

# Multiply elements in each row (e.g., combining probabilities per sample)
print(np.prod(X, axis=1))
# [20 40 60] <- (10*2), (5*8), (15*4)