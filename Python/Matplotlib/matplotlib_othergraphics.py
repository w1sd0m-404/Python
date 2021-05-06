import matplotlib.pyplot as plt

import numpy as np

np1 = np.linspace(1,10,20)
np2 = np1 ** 2
rand1 = np.random.randint(1,50,20)
#----------scatter grafik
#plt.scatter(np1,np2)
#plt.show()


#---------- histogram grafik
#plt.hist(rand1)
#plt.show()


#---------- boxplot grafik
plt.boxplot(rand1)
plt.show()