import matplotlib.pyplot as plt
import numpy as np

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10
low = 21
high = 65
size = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low, high, size)


xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

#plt.hist(salaries)
#plt.scatter(ages, salaries)
plt.plot(xpoints, ypoints, color="red")

plt.title("Random Plot")
plt.xlabel("Salaries")
plt.ylabel("Age")
plt.legend()

#plt.show()
plt.savefig("prettier-plot.png")