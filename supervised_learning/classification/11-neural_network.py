#!/usr/bin/env python3
"""Defines a neural network with one hidden layer
performing binary classification"""

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
