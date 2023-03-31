import matplotlib.pyplot as plt
import numpy as np

#piecharts
fruit = np.array(["Apples", "Oranges", "Bananas"])
numbers = np.array([23,77,500])
plt.pie(numbers, labels = fruit)
#plt.legend()
plt.savefig("week8testpie.png")
#saves plots in filename
#plt.savefig("week8test.png")
#plt.show() shows the plot
