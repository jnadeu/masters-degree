# Importing pandas, scikit-learn, numpy and matplotlib
import pandas as pd
import numpy as np
from sklearn import datasets, preprocessing
import matplotlib.pyplot as plt


# Load the California Housing dataset
california_housing = datasets.fetch_california_housing()

# Display basic information about the dataset
print(f"Features: {california_housing.feature_names}")
print(f"Target: {california_housing.target_names}")
print(f"Shape of data: {california_housing.data.shape}")
print(f"Shape of target: {california_housing.target.shape}")


# Prepare the data
X = california_housing.data
y = california_housing.target

# Normalize the features
scaler = preprocessing.StandardScaler()
X = scaler.fit_transform(X)

# Add a column of ones to X for the intercept term
X = np.c_[np.ones(X.shape[0]), X]
# X.shape[0] is the number of rows (i.e. number of datapoints)

# Initialize parameters
theta = np.zeros(X.shape[1])
# X.shape[1] is the number of columns (i.e. number of features)
#np.zeros(X.shape[1]) will create an array [0, 0,..., 0] as long as the number of columns
# we initialise all weights as 0


# Experiment with different learning rates
learning_rates = [0.001, 0.01, 0.1, 0.5, 1]
# Hyperparameters
learning_rate = 0.1
num_iterations = 1000

# Gradient Descent Function
def gradient_descent(X, y, theta, learning_rate, num_iterations):
    # Number of datapoints
    m = len(y) #m: The number of training examples (length of y, or number of rows in X)
    cost_history = [] #will store the error at each iteration
    
    for i in range(num_iterations):
        predictions = X.dot(theta) #dot product of X and theta, gives a prediction for each datapoint in X
        errors = predictions - y
        #gradient: dot product of the transpose of X and of the error vector (you can check manually why this corresponds to the sum formula seen in the slides)
        gradients = (2/m) * X.T.dot(errors)
        #update weights
        theta -= learning_rate * gradients
        #cost: squared mean errors
        cost = (1/m) * np.sum(errors ** 2)
        cost_history.append(cost) #store cost
        if i % 100 == 0:
            # print cost every 100 iterations
            print(f"Iteration {i}: Cost {cost}")
    
    return theta, cost_history

if __name__ == "__main__":
    # Run gradient descent
    theta, cost_history = gradient_descent(X, y, theta, learning_rate, num_iterations)

    # Plotting the cost function history
    plt.plot(range(num_iterations), cost_history, 'b-')
    plt.xlabel('Iterations')
    plt.ylabel('Cost')
    plt.title('Cost Function History')
    plt.show()

    # Make predictions
    predictions = X.dot(theta)

    # Display the first 5 predictions
    print("First 5 predictions:", predictions[:5])
    print("First 5 actual values:", y[:5])


