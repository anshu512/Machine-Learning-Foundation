import numpy as np

# 4 samples (rows), 2 features (columns: Age, Income in $1000s)
X = np.array([
    [25.0, 50.0],
    [30.0, np.nan], # Missing Income
    [np.nan, 60.0], # Missing Age
    [40.0, 80.0]
])

# See exactly where the missing values are
print(np.isnan(X))
# [[False False]
#  [False  True]
#  [ True False]
#  [False False]]

# Count missing values per feature (axis=0)
print(np.sum(np.isnan(X), axis=0))
# [1 1] <- 1 missing Age, 1 missing Income 

# Calculate the average Age and Income of the available data
safe_means = np.nanmean(X, axis=0)

print("Safe Means:", safe_means)
# [31.66666667 63.33333333] 
# (Average of 25, 30, 40) and (Average of 50, 60, 80)

# 1. Isolate the Age column (column 0)
age_col = X[:, 0]

# 2. Find the average Age (ignoring the NaN)
age_mean = np.nanmean(age_col) # 31.66

# 3. Create a mask for just the missing Ages
missing_age_mask = np.isnan(age_col)

# 4. Overwrite the NaNs with the mean
X[missing_age_mask, 0] = age_mean

print("Dataset after Age Imputation:")
print(X)
# [[25.   50. ]
#  [30.    nan]
#  [31.66  60. ] <- NaN is now the average age
#  [40.   80. ]]