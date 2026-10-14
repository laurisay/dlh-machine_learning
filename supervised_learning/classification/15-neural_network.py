#!/usr/bin/env python3
"""Defines a neural network with one hidden layer
performing binary classification"""

import matplotlib.pyplot as plt
import numpy as np


class NeuralNetwork:
    """Neural network with one hidden layer
    performing binary classification"""

    def __init__(self, nx, nodes):
        """
        Class constructor

        nx: number of input features
        nodes: number of nodes found in the hidden layer
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """Getter for the weights of the hidden layer"""
        return self.__W1

    @property
    def b1(self):
        """Getter for the bias of the hidden layer"""
        return self.__b1

    @property
    def A1(self):
        """Getter for the activated output of the hidden layer"""
        return self.__A1

    @property
    def W2(self):
        """Getter for the weights of the output neuron"""
        return self.__W2

    @property
    def b2(self):
        """Getter for the bias of the output neuron"""
        return self.__b2

    @property
    def A2(self):
        """Getter for the activated output of the output neuron"""
        return self.__A2

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neural network

        X: numpy.ndarray with shape (nx, m) containing the input data

        Updates the private attributes __A1 and __A2
        Returns the private attributes __A1 and __A2, respectively
        """
        Z1 = np.matmul(self.__W1, X) + self.__b1
        self.__A1 = 1 / (1 + np.exp(-Z1))
        Z2 = np.matmul(self.__W2, self.__A1) + self.__b2
        self.__A2 = 1 / (1 + np.exp(-Z2))
        return self.__A1, self.__A2

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression

        Y: numpy.ndarray with shape (1, m) containing the correct labels
        A: numpy.ndarray with shape (1, m) containing the activated output

        Returns the cost
        """
        m = Y.shape[1]
        loss = -(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return np.sum(loss) / m

    def evaluate(self, X, Y):
        """
        Evaluates the neural network's predictions

        X: numpy.ndarray with shape (nx, m) containing the input data
        Y: numpy.ndarray with shape (1, m) containing the correct labels

        Returns the predicted labels and the cost, respectively
        """
        _, A2 = self.forward_prop(X)
        cost = self.cost(Y, A2)
        prediction = np.where(A2 >= 0.5, 1, 0)
        return prediction, cost

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """
        Calculates one pass of gradient descent on the neural network

        X: numpy.ndarray with shape (nx, m) containing the input data
        Y: numpy.ndarray with shape (1, m) containing the correct labels
        A1: output of the hidden layer
        A2: predicted output
        alpha: the learning rate

        Updates the private attributes __W1, __b1, __W2 and __b2
        """
        m = Y.shape[1]

        dZ2 = A2 - Y
        dW2 = np.matmul(dZ2, A1.T) / m
        db2 = np.sum(dZ2, axis=1, keepdims=True) / m

        dZ1 = np.matmul(self.__W2.T, dZ2) * A1 * (1 - A1)
        dW1 = np.matmul(dZ1, X.T) / m
        db1 = np.sum(dZ1, axis=1, keepdims=True) / m

        self.__W2 = self.__W2 - alpha * dW2
        self.__b2 = self.__b2 - alpha * db2
        self.__W1 = self.__W1 - alpha * dW1
        self.__b1 = self.__b1 - alpha * db1

    def train(self, X, Y, iterations=5000, alpha=0.05,
              verbose=True, graph=True, step=100):
        """
        Trains the neural network

        X: numpy.ndarray with shape (nx, m) containing the input data
        Y: numpy.ndarray with shape (1, m) containing the correct labels
        iterations: number of iterations to train over
        alpha: the learning rate
        verbose: whether to print information about the training
        graph: whether to graph information about the training
        step: interval (in iterations) between prints and plot points

        Updates the private attributes __W1, __b1, __A1,
        __W2, __b2 and __A2

        Returns the evaluation of the training data after
        iterations of training
        """
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations < 1:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        if verbose or graph:
            if not isinstance(step, int):
                raise TypeError("step must be an integer")
            if step < 1 or step > iterations:
                raise ValueError("step must be positive and <= iterations")

        costs = []
        steps = []

        for i in range(iterations + 1):
            A1, A2 = self.forward_prop(X)
            if i % step == 0 or i == iterations:
                cost = self.cost(Y, A2)
                if verbose:
                    print("Cost after {} iterations: {}".format(i, cost))
                if graph:
                    costs.append(cost)
                    steps.append(i)
            if i < iterations:
                self.gradient_descent(X, Y, A1, A2, alpha)

        if graph:
            plt.plot(steps, costs, "b")
            plt.xlabel("iteration")
            plt.ylabel("cost")
            plt.title("Training Cost")
            plt.show()

        return self.evaluate(X, Y)
