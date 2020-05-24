import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zipf

x = np.arange(1, 1001)

plt.loglog(x, zipf.pmf(x, 1.07))
plt.show()

plt.plot(x, zipf.pmf(x, 1.07))
plt.show()


for i in [1.07, 2, 3]:
    plt.loglog(x, zipf.pmf(x, i), label=str(i))

plt.legend()
plt.show()
