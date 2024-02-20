# Program to multiply two matrices using nested loops
import random
import numpy as np
N = 250

@profile
def generate_matrix(N, M):
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(M)])
    return X

@profile
def generate_matrix2(N, M):
    return 100.0*np.random.randint(0,100,(N,M))

@profile
def matrix_mult(X, Y, result):
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

@profile
def matrix_mult2(X, Y, result):
    # iterate through rows of X
    for i, xrow in enumerate(X):
        # iterate through columns of Y
        for j, ycol in enumerate(Y):
            # iterate through rows of Y
            for k, yrow in enumerate(Y):
                result[i][j] += xrow[k] * yrow[j]
    return result


@profile
def matrix_mult3(X, Y, result):
    X_arr = np.asarray(X)
    Y_arr = np.asarray(Y)
    result_arr = X_arr @ Y_arr
    return result_arr

"""
for r in result:
    print(r)
"""
@profile
def main():

    X = generate_matrix(N, N)
    Y = generate_matrix(N, N+1)
    X2 = generate_matrix2(N, N)
    Y2 = generate_matrix2(N, N+1)

    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))

    result = matrix_mult(X, Y, result)
    result = matrix_mult2(X, Y, result) # neglible difference to original
    result = matrix_mult3(X, Y, result) # extremely much faster

# if __name__ == "main":
#     main()

main()