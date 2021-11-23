
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as scp

Fs = 500
freq = [45,60,92]
T = 1/Fs
pi = np.pi

t = np.arange(0,5,T)
y = np.zeros_like(t)

signal = 2*np.cos(freq[0]*t*2*pi) + 5*np.cos(freq[1]*t*2*pi) + 10*np.cos(freq[2]*t*2*pi)
fft_signal = scp.fft(signal)

fft_freq = Fs/np.size(fft_signal)
real = np.real(fft_signal)
imag = np.imag(fft_signal)

mag = np.absolute(fft_signal)
df = Fs/mag.shape[0]
freq2 = np.arange(0,Fs,df)
mag_norm = 2*mag/mag.shape[0]


eg = mag**2/mag.shape[0]


plt.figure()
plt.plot(freq2,real)
plt.title('Parte real fft')
plt.xlim([0,Fs/2])

plt.figure()
plt.plot(freq2,imag)
plt.title('Parte imaginária fft')
plt.xlim([0,Fs/2])



plt.figure()
plt.plot(freq2,mag_norm)
plt.title('magnitude')
plt.xlim([0,Fs/2])


plt.figure()
plt.plot(freq2,eg)
plt.title('espectro de energia')
plt.xlim([0,Fs/2])

plt.show()
