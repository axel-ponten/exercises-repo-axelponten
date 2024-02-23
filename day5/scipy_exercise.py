from scipy import linalg, stats
import matplotlib.pyplot as plt
import numpy as np

##### LINALG #####
A = np.array([[1, -2, 3], [4, 5, 6], [7, 1, 9]])

b = np.array([1, 2, 3])

x = linalg.solve(A, b)

print("solution", x)
print("check solution", A @ x - b)

B = np.random.randint(0, 9, (3, 3))

x2 = linalg.solve(A, B)
print("solution", x2)
print("check solution", A @ x2 - B)

# eigenvectors
w, vr = linalg.eig(A)
print(w, vr)

print("test eigenvectors", A @ vr - w * vr)
print(
    "close enough to zero?",
    np.allclose(A @ vr - w * vr, np.zeros((A @ vr - w * vr).shape)),
)

# inverse and determinant
Ainv = linalg.inv(A)
print("Inverse of A", Ainv)
print("test inv", A @ Ainv, Ainv @ A)
print("Determinant of A", linalg.det(A))

# norm of matrix, -1st 1st and 2nd order
print(linalg.norm(A, -1))
print(linalg.norm(A, 1))
print(linalg.norm(A, 2))


##### STATS #####
mu = 5
prv = stats.poisson(mu)
x = np.arange(0,20)
plt.figure()
plt.plot(x,prv.pmf(x))

plt.figure()
plt.plot(x,prv.cdf(x))

plt.figure()
plt.hist(prv.rvs(1000))

mu = 5
std = 2
x = np.linspace(0,20,50)
grv = stats.norm(mu, std)
plt.figure()
plt.plot(x,grv.pdf(x))

plt.figure()
plt.plot(x,grv.cdf(x))

plt.figure()
plt.hist(grv.rvs(1000))
plt.show()

# test if from same distribution
x1 = grv.rvs(10)
x2 = grv.rvs(10)

t, pval = stats.ttest_ind(x1,x2)
print(t, pval)
