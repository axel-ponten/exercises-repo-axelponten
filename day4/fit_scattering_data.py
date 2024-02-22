import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import minimize_scalar

# read in data
experiment_path = "I_q_IPA_exp.npy"
theory_path     = "I_q_IPA_model.npy"
data = np.load(experiment_path)
theory     = np.load(theory_path)


# create interp1d function from theory
theory_interp = interp1d(theory[:,0], theory[:,1])
x_for_plot    = np.linspace(0, 20, 70)

# plot theory and data
scale = 1/10000.
plt.figure()
plt.title("Before fitting: scale = {:f}".format(scale))
plt.plot(data[:,0], data[:,1], label="exp")
plt.plot(theory[:,0], scale*theory[:,1], label="theory")
plt.plot(x_for_plot, scale*theory_interp(x_for_plot), label="theory interp")
plt.xlim((0,20))
plt.legend()
plt.xlabel("scattering vector")
plt.ylabel("scattering strength")
plt.savefig("scattering_before_fitting.png")
plt.show()

# fit normalization of theory
def least_squares_from_scale(scale, x, y):
    return np.sum( (x - scale*y)**2 )
# clean from nan
data_clean = data[~np.isnan(data[:,1])]
# minimize
res = minimize_scalar(
    least_squares_from_scale,
    args = (data_clean[:,1], theory_interp(data_clean[:,0]) )
)
# print best scale
print("Normalization that gives best least squares:", "{:f}".format(res.x), "= 1/{:.1f}".format(1/res.x))

# plot with best fit
scale = res.x
plt.figure()
plt.title("After fitting: scale = {:f}".format(res.x))
plt.plot(data[:,0], data[:,1], label="exp")
plt.plot(theory[:,0], scale*theory[:,1], label="theory")
plt.plot(x_for_plot, scale*theory_interp(x_for_plot), label="theory interp")
plt.xlim((0,20))
plt.legend()
plt.xlabel("scattering vector")
plt.ylabel("scattering strength")
plt.savefig("scattering_after_fitting.png")
plt.show()
