#!/home/axel/miniconda3/envs/icetray-env/bin/python
import numpy as np


# a)
a = np.zeros(10)
a[4] = 1
print(a)

# b)
b = np.arange(10,50)
print(b)

# c)
# c = np.flip(b)
c = b[::-1]
print(c)

# d)
d = np.arange(0,9).reshape((3,3))
print(d)

# e)
e = np.asarray([1,2,0,0,4,0])
e = np.where(e != 0)[0]
print(e)

# f)
f = np.random.random(30)
print(f)
print("Mean:", f.mean())

# g)
N, M = 5,6
g = np.zeros((N,M))
g[:, 0] = 1
g[:,-1] = 1
g[0, :] = 1
g[-1,:] = 1
print(g)

# h)
N, M = 8, 8
h = np.zeros((N,M), dtype=np.int32)
even_indices = np.arange(0, M, 2)
odd_indices  = np.arange(1, M, 2)
h[0::2, even_indices] = 1
h[1::2, odd_indices] = 1
print(h)

# i)
import math
N, M = 8, 8
i = np.array([[1,0],[0,1]])
i = np.tile(i, (math.ceil(N/2), math.ceil(M/2)))[:N,:M] # slice in case of odd N or M
print(i)

# j)
def negate_range(arr: np.ndarray, range_cut: tuple) -> np.ndarray:
    return np.where((range_cut[0] < arr) & (arr < range_cut[1]), -arr, arr)
j = np.arange(11)
print(j)
j = negate_range(j, (3,8))
print(j)

# maybe better way is this
j = np.arange(11)
minval, maxval = 3, 8
j[(minval < j) & (j < maxval)] *= -1
print(j)

# k)
k = np.random.random(10)
k.sort()
print(k)

# l)
for i in range(128):
    l1 = np.random.randint(0,2,5)
    l2 = np.random.randint(0,2,5)
    # equal = all(l1 == l2)
    equal = np.array_equal(l1, l2) # maybe better way
    if not equal:
        continue
    print("trial",i)
    print(l1)
    print(l2)
    print(equal)

# m)
m = np.arange(10, dtype=np.int32)
print(m)
# which one?
m = m.astype(np.float32, copy = False)
#m = np.array(m, dtype=np.float32)
print(m)

# n)
n1 = np.arange(9).reshape(3,3)
n2 = n1 + 1
n3 = np.dot(n1, n2)
n4 = np.diag(n3)

print(n1)
print(n2)
print(n3)
print(n4)