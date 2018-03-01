#!/usr/bin/python3
import numpy as np


# Set seed so that consecutive runs are the same weighting
np.random.seed(1)
# initialize weights randomly with mean 0
syn0 = 2 * np.random.random((3, 1)) - 1


def game():
    board = createemptyboard()
    return


def getbestmove(board):
    return


def playmove(x, y, symbol):
    return board


def getresult(board):
    return result


def createemptyboard():
    board = np.empty((3, 3))
    return board


# sigmoid function
def nonlin(x, deriv=False):
    if deriv:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))