import numpy as np

# 3 samples (houses) and 2 features (Price in $1000s, Age in years)
X = np.array([
    [200,  10],  # House 0: Cheap, New
    [300,  50],  # House 1: Average, Old
    [1000, 30]   # House 2: Mansion (Outlier), Middle-aged
])

print(np.mean(X, axis=0))
# [500.  30.] <- Average price is 500k, average age is 30

print(np.median(X, axis=0))
# [300.  30.] <- Median price is 300k, a much better representation of a "typical" house here.

print(np.var(X, axis=0))
# [126666.67    266.67] <- The spread in price is massive compared to the spread in age.

print(np.std(X, axis=0))
# [355.9   16.33]