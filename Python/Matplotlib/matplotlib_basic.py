import matplotlib.pyplot as plt

import numpy as np

yasListesi = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
kiloListesi = [55, 65, 65, 60, 70, 78, 80, 83, 86, 90]

npYas = np.array(yasListesi)
npKilo = np.array(kiloListesi)

plt.plot(npYas, npKilo, "g")  # Çizim
plt.xlabel("Yas")  # X ekseni adlandırma
plt.ylabel("Kilo")  # Y ekseni adlandırma
plt.title("Kilonun yaşa göre değişimi")  # Grafiği adlandırır
plt.show()  # Ekranda gösterme
