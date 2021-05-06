import matplotlib.pyplot as plt

import numpy as np

npDizi1 = np.linspace(1,10,20)
npDizi2 = npDizi1 ** 2

#---- Renklendirme

#(myFiguer,myAxes) = plt.subplots()
#myAxes.plot(npDizi1,npDizi2,color="#0E0505",alpha=0.2) # Alpha değeri saydamlığı ayarlar
#myAxes.plot(npDizi2,npDizi1,color="#00F7FF")
#plt.show()


#------- Çizgi ayarları

(newFigure,newAxes)=plt.subplots()
newAxes.plot(npDizi1,npDizi1 + 2,color = "#FF8000",linewidth=5.0) # linewidth çizgi kalınlığını ayarlar
newAxes.plot(npDizi1,npDizi1 + 3,color="blue")
newAxes.plot(npDizi1,npDizi1 + 4,color="red",linestyle="dotted") # linestyle çizgi desenini ayarlar  "--","-.",":"
newAxes.plot(npDizi1,npDizi1 + 5,color="#000000",marker="o",markersize=5,markerfacecolor="yellow") # marker  verileri gösteren noktaları ayarlar
plt.show()