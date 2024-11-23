import numpy as np
from sklearn.metrics import precision_score, recall_score


def read_number(prompt, invalid_prompt, dtype, test=None):
    while True:
        try:
            n = dtype(input(prompt))
            if not test or test(n):
                return n
            else:
                print(invalid_prompt)
        except ValueError:
            print(invalid_prompt)


# Ask the user for input N
N = read_number("Enter N (positive integer): ", "N needs to be a positive integer", int, lambda num: num >= 0)

# Initialize numpy arrays for X (ground truth) and Y (predicted classes)
x = np.zeros(N, dtype=int)
y = np.zeros(N, dtype=int)

# Read N points from the user
for i in range(N):
    x[i] = read_number(f"Enter x value for point {i + 1} (0 or 1): ",
                       "x needs to be a 0 or 1",
                       int,
                       lambda num: num == 0 or num == 1)
    y[i] = read_number(f"Enter y value for point {i + 1} (0 or 1): ",
                       "x needs to be a 0 or 1",
                       int,
                       lambda num: num == 0 or num == 1)

# Compute Precision and Recall using Scikit-learn
precision = precision_score(x, y)
recall = recall_score(x, y)

# Output the Precision and Recall
print(f"Precision: {precision}")
print(f"Recall: {recall}")
