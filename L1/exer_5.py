import numpy as np
import matplotlib.pyplot as plt
x = np.loadtxt(fname="fone.txt", delimiter=";")

tempo = x[:,0]
sinal = x[:,1]

T = tempo[1] - tempo[0]
Fs = 1/T

plt.plot(tempo,sinal)
plt.xlabel("tempo")
plt.ylabel("sinal")
plt.figure()

s1 = (tempo >=1.4) & (tempo < 1.7)
s2 = (tempo >=2.10) & (tempo < 2.4)
s3 = (tempo >=2.7) & (tempo < 3.0)

plt.subplot(3,1,1)
plt.plot(tempo[s1],sinal[s1])
plt.ylabel("sinal")

plt.subplot(3,1,2)
plt.plot(tempo[s2],sinal[s2])
plt.ylabel("sinal")

plt.subplot(3,1,3)
plt.plot(tempo[s3],sinal[s3])
plt.ylabel("sinal")
plt.xlabel('tempo')
plt.show()