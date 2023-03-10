import random
import matplotlib.pyplot as plt
import numpy as np

# Class for generating data points
class DataGenerator:
    def __init__(self, num_points):
        # Number of data points to generate
        self.num_points = num_points

    def generate_data(self):
        # Generates x values in the range of 0 to 10, spaced self.num_points apart
        x = np.linspace(0, 10, self.num_points)
        # Generates y values as 2 * x + 1 with some random noise
        y = 2 * x + 1 + np.random.normal(0, 1, self.num_points)
        return x, y
    
# Class for linear regression model
class LinearRegression:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.b0 = 0
        self.b1 = 0

    def fit(self):
        # Calculate the mean of x and y values
        x_mean = np.mean(self.x)
        y_mean = np.mean(self.y)
        # Calculate the numerator and denominator for regression coefficients b0 and b1
        numerator = 0
        denominator = 0
        for i in range(len(self.x)):
            numerator += (self.x[i] - x_mean) * (self.y[i] - y_mean)
            denominator += (self.x[i] - x_mean) ** 2
        # Calculate b1 and b0
        self.b1 = numerator / denominator
        self.b0 = y_mean - self.b1 * x_mean

    def predict(self, x):
        # Predict y values based on the regression coefficients and input x values
        return self.b0 + self.b1 * x

    def score(self, x, y):
        # Predict y values based on the input x values
        y_pred = self.predict(x)
        # Calculate residual sum of squares
        u = ((y - y_pred) ** 2).sum()
        # Calculate total sum of squares
        v = ((y - y.mean()) ** 2).sum()
        # Calculate the R^2 score
        return 1 - u/v

    def mean_squared_error(self, x, y):
        # Predict y values based on the input x values
        y_pred = self.predict(x)
        # Calculate the mean squared error
        mse = ((y - y_pred) ** 2).mean()
        return mse

    def mean_absolute_error(self, x, y):
        # Predict y values based on the input x values
        y_pred = self.predict(x)
        # Calculate the mean absolute error
        mae = np.abs(y - y_pred).mean()
        return mae

def main():
    num_points = 50
    # Generate data points
    data_gen = DataGenerator(num_points)
    x, y = data
