import numpy as np

# 3 samples, 2 output classes (Shape: 3, 2)
predictions = np.array([
    [2.0, 3.0],  # Sample 0 predictions
    [1.5, -1.0], # Sample 1 predictions
    [0.5, 0.5]   # Sample 2 predictions
])

# 1 bias value per output class (Shape: 2,)
bias = np.array([0.5, -0.5])

# NumPy magically applies the [0.5, -0.5] to EVERY row
final_output = predictions + bias

print("Predictions + Bias:")
print(final_output)
# [[ 2.5  2.5]   <- (2.0+0.5), (3.0-0.5)
#  [ 2.   -1.5]  <- (1.5+0.5), (-1.0-0.5)
#  [ 1.    0. ]] <- (0.5+0.5), (0.5-0.5)

# 3 houses. Features: [Price, Bedrooms] (Shape: 3, 2)
X = np.array([
    [200, 2],
    [300, 3],
    [400, 4]
])

# The average Price is 300, average Bedrooms is 3 (Shape: 2,)
mean = np.array([300, 3])

# Subtract the [300, 3] from EVERY house
X_centered = X - mean

print("Centered Features:")
print(X_centered)
# [[-100   -1]  <- 100k below average, 1 bed below average
#  [   0    0]  <- Exactly average
#  [ 100    1]] <- 100k above average, 1 bed above average

# 2 image pixels (Shape: 1, 2)
pixels = np.array([255.0, 127.5])

# Broadcasting a single number (scalar) across the array
normalized_pixels = pixels / 255.0

print("Normalized Pixels:")
print(normalized_pixels)
# [1.  0.5]