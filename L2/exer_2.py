import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as scp

pi = np.pi
Fs = 1000
T = 1/Fs
t = np.arange(0,7,T)

X1 = 0.7 * np.sin(2*pi*65*t)
X2 = 2 * np.sin(2*pi*125*t + 0.5 * pi)
N = 0.5 * np.random.randn(np.size(t))

signal = X1 + X2
noise_signal = signal + N


fft_noise_signal = scp.fft(noise_signal)
mag = np.absolute(fft_noise_signal)
df = Fs/mag.shape[0]
freq = np.arange(0,Fs,df)
mag_norm = 2*mag/mag.shape[0]

plt.figure()
plt.title('Signal + Noise fft')
plt.plot(freq,mag_norm)
plt.xlim(0,Fs/2)


eg = mag**2/mag.shape[0]



s = (mag<0.1)
fft_noise_signal[s] = 0
yy = scp.ifft(fft_noise_signal)


plt.figure()
plt.title('Signal + Noise')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.plot(t,signal,t,N)



plt.figure()
plt.plot(freq,mag_norm)
plt.title('Magnitude')
plt.xlabel('Frequencia (Hz)')
plt.ylabel('Magnitude')
plt.xlim([0,Fs/2])

plt.figure()
plt.plot(freq,eg)
plt.title('Energia')
plt.xlabel('Frequencia (Hz)')
plt.ylabel('Magnitude')
plt.xlim([0,Fs/2])

plt.figure()
plt.plot(t,yy)
plt.title('Inversa sem ruido')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.show()



