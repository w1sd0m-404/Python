import matplotlib.pyplot as plt

import numpy as np

npDizi1 = np.linspace(1,10,20)
npDizi2 = (npDizi1 ** 3)

#plt.plot(npDizi1,npDizi2,"b*-")
#plt.show()

#plt.subplot(1,2,1) # Yan yana 2 grafik
#plt.plot(npDizi1,npDizi2,"b--")
#plt.subplot(1,2,2)
#plt.plot(npDizi2,npDizi1,"g*-")
#plt.show()

#------------ Figure eklemek

#myFigure = plt.figure()
#figureAxes = myFigure.add_axes([0.2,0.2,0.6,0.6])
#figureAxes.plot(npDizi1,npDizi2,"b")
#figureAxes.set_xlabel("X ekseni veri adı")
#figureAxes.set_ylabel("Y ekseni veri adı")
#figureAxes.set_title("Grafik başlığı")
#plt.show()

#------------- İç içe grafikler

#myFigure2 = plt.figure()
#eksen1 = myFigure2.add_axes([0.1,0.1,0.7,0.7])
#eksen2 = myFigure2.add_axes([0.2,0.4,0.3,0.3])

#eksen1.plot(npDizi1,npDizi2,"g")
#eksen1.set_xlabel("X ekseni")
#eksen1.set_ylabel("Y ekseni")
#eksen1.set_title("Ana grafik başlığı")

#eksen2.plot(npDizi2,npDizi1,"b")
#eksen2.set_xlabel("X ekseni")
#eksen2.set_ylabel("Y ekseni")
#eksen2.set_title("Sub grafik başlığı")

#plt.show()


#------------- Subplots()

#(benimFigure,benimEksenler) = plt.subplots(nrows=1,ncols=2)
#for i in benimEksenler:
#    i.plot(npDizi1,npDizi2,"b")
#    i.set_xlabel("X ekseni")
#plt.tight_layout() # Yan yana grafiklerin aralarını biraz açar
#plt.show()


#------------- Görsel Geliştirme

newFigure = plt.figure()
## plt.figure(dpi=150)  , dpi = kalite
newAxes = newFigure.add_axes([0.1,0.1,0.8,0.8])
newAxes.plot(npDizi1,npDizi2,"b",label="numpyDizisi ** 3")
newAxes.plot(npDizi1,npDizi1 ** 2,"g",label="numpyDizisi ** 2")
newAxes.plot(npDizi1,npDizi1 ** 4,"y",label="numpyDizisi ** 4")
newAxes.legend(loc=6) # loc=location
plt.show()
# newFigure.savefig("deneme.png",dpi=200)  png formatında figürü kaydeder