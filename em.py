from numpy import hstack
from numpy.random import normal
import matplotlib.pyplot as plt
 
sample1 = normal(loc=20, scale=5 , size=4000)
sample2 = normal(loc=40, scale=5 , size=8000)
sample = hstack((sample1,sample2))
plt.hist(sample, bins=50, density=True)
plt.show()


# example of fitting a gaussian mixture model with expectation maximization
from numpy import hstack
from numpy.random import normal
from sklearn.mixture import GaussianMixture
# generate a sample
sample1 = normal(loc=20, scale=5, size=4000)
sample2 = normal(loc=40, scale=5, size=8000)
sample = hstack((sample1, sample2))
# reshape into a table with one column
sample = sample.reshape((len(sample), 1))
# fit model
model = GaussianMixture(n_components=2, init_params='random')
model.fit(sample)
# predict latent values
yhat = model.predict(sample)
# check latent value for first few points
print(yhat[:80])
# check latent value for last few points
print(yhat[-80:])
