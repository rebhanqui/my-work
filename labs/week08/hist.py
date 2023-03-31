import matplotlib.pyplot as plt
import numpy as np

#histogram
#seed makes data run the same in random 
np.random.seed(1)
normData = np.random.normal(size=10)
plt.hist(normData)
#plt.legend()
plt.savefig("week8testhist.png")

#saves plots in filename
#plt.savefig("week8test.png")
#plt.show() shows the plot