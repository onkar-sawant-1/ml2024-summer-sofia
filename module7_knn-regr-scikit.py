import numpy as np
from sklearn.neighbors import KNeighborsRegressor


class KNNRegression:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.points = np.zeros((n, 2))
        self.knn = None

    def insert_point(self, index, x, y):
        self.points[index] = [x, y]

    def train(self):
        x_train = self.points[:, 0].reshape(-1, 1)
        y_train = self.points[:, 1]

        self.knn = KNeighborsRegressor(n_neighbors=self.k)
        self.knn.fit(x_train, y_train)

    def knn_regression(self, X):
        return self.knn.predict(np.array([[X]]))[0]


def read_number(prompt, invalid_prompt, type, test = None):
    while True:
        try:
            n = type(input(prompt))
            if not test or test(n):
                return n
            else:
                print(invalid_prompt)
        except ValueError:
            print(invalid_prompt)


def main():
    # Read input N (number of points)
    n = read_number("Enter number of points: ",
                    "Error: N must be a positive integer.",
                    int,
                    lambda num: num > 0)

    # Read input k (number of neighbors)
    k = read_number("Enter k (number of neighbors): ",
                    f"Error: k must be between 1 and {n}.",
                    int,
                    lambda num: 0 < num <= n)

    knn_regr = KNNRegression(n, k)

    # Read N (x, y) points
    for i in range(n):
        x = read_number(f"Enter x for point {i + 1}: ",
                        "Error: x must be a real number.",
                        float)
        y = read_number(f"Enter y for point {i + 1}: ",
                        "Error: x must be a real number.",
                        float)
        knn_regr.insert_point(i, x, y)

    # Compute and display variance of labels
    y_labels = knn_regr.points[:, 1]
    variance = np.var(y_labels)
    print(f"The variance of the labels in the training dataset is: {variance}")


    # Train the KNN model
    knn_regr.train()

    # Read input X and calculate the result
    test_x = read_number("Enter X value to predict Y: ",
                         "Error: X must be a real number.",
                         float)

    predict_y = knn_regr.knn_regression(test_x)
    print(f"Predicted Y value: {predict_y}")


if __name__ == "__main__":
    main()
