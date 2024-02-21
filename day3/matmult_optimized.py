# Program to multiply two matrices using nested loops
import random
import numpy as np
N = 250


def generate_matrix2(N, M):
    return np.random.randint(0,100,(N,M))

def matrix_mult2(X, Y):
    return X @ Y

def main():
    X2 = generate_matrix2(N, N)
    Y2 = generate_matrix2(N, N+1)
    result = matrix_mult2(X, Y) # neglible difference to original

if __name__ == "main":
    main()