import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

#line plot
plt.plot(xpoints, ypoints, label= "xsquared")
plt.plot(xpoints, xpoints, label="straight", color="red")
#plt.legend()
#scatterplot
randompoints = np.random.randint(1, 1000, 100)
plt.scatter(xpoints, randompoints, label= "random", color="pink")
plt.savefig("week8testscatterline.png")

#saves plots in filename
#plt.savefig("week8test.png")
#plt.show() shows the plot