#!/usr/bin/env python3
"""Defines a single neuron performing binary classification"""

import numpy as np


class Neuron:
    """Single neuron performing binary classification"""

    def __init__(self, nx):
        """
        Class constructor

        nx: number of input features to the neuron
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be a integer")
        if nx < 1:
            raise ValueError("nx must be positive")

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Getter for the weights vector"""
        return self.__W

    @property
    def b(self):
        """Getter for the bias"""
        return self.__b

    @property
    def A(self):
        """Getter for the activated output"""
        return self.__A

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neuron

        X: numpy.ndarray with shape (nx, m) containing the input data

        Returns the private attribute __A
        """
        Z = np.matmul(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A

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
        Evaluates the neuron's predictions

        X: numpy.ndarray with shape (nx, m) containing the input data
        Y: numpy.ndarray with shape (1, m) containing the correct labels

        Returns the predicted labels and the cost, respectively
        """
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.where(A >= 0.5, 1, 0)
        return prediction, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
        Calculates one pass of gradient descent on the neuron

        X: numpy.ndarray with shape (nx, m) containing the input data
        Y: numpy.ndarray with shape (1, m) containing the correct labels
        A: numpy.ndarray with shape (1, m) containing the activated output
        alpha: the learning rate

        Updates the private attributes __W and __b
        """
        m = Y.shape[1]
        dZ = A - Y
        dW = np.matmul(dZ, X.T) / m
        db = np.sum(dZ) / m

        self.__W = self.__W - alpha * dW
        self.__b = self.__b - alpha * db
