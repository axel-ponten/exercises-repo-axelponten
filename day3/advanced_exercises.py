#!/home/axel/miniconda3/envs/icetray-env/bin/python
import numpy as np

def id(x: np.ndarray):
    return x.__array_interface__["data"][0]


# a)
p = np.array([[1,2,10],
              [3,4,20],
              [5,6,30],
              [7,8,40]
              ], dtype=np.float64)

def normalize_z(arr):
    z = arr[:,-1]
    z = np.tile(z, (arr.shape[1],1))
    z = np.transpose(z)
    arr[:] = arr/z # in place
    return arr

pid = id(p)
p = normalize_z(p)
print(p, pid == id(p))

# b)
b = np.random.random((3,3))
print(b)
indices = np.arange(b.shape[0])
b_diag = b[indices, indices]
print(b_diag)

# c)
c = np.random.random((10,3))
print(c)
indices = np.argmax(-1*np.abs(c - 0.75), axis=1)
print(indices)
c_best = c[np.arange(c.shape[0]), indices] # NOTE, c[:, indices] does NOT work
print(c_best, c_best.shape)

# d)
x = np.empty((10, 8, 6))

idx0 = np.zeros((3, 8)).astype(int)
idx1 = np.zeros((3, 1)).astype(int)
idx2 = np.zeros((1, 1)).astype(int)

y = x[idx0, idx1, idx2]
# my prediction: y.shape -> (3,8) (I swear I didn't check before guessing)
print(y.shape)
# output: (3,8)

# e)
x = np.arange(12, dtype=np.int32).reshape((3, 4))
print(x)
print(x.strides)
stride_view = np.lib.stride_tricks.as_strided(x, shape = (2,3,2,2), strides = (16,4,16,4), writeable = False)
print(stride_view)