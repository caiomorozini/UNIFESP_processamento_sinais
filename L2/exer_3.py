import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import scipy.io as scp
import scipy.fft as scifft
pacific = scp.loadmat('sombaleia1.mat')
japan = scp.loadmat('sombaleia2.mat')

signals = [pacific['C'],japan['j'][0,:]]
Fs = [pacific['fs_california'], japan['Fs_japao']]
T = [1/f for f in Fs]

t = [np.arange(0,len(signal)*T[index],T[index]) for index, signal in enumerate(signals)]

fft_signals = [scifft.fft(signal) for signal in signals]

magnitudes = [np.absolute(fft_signal) for fft_signal in fft_signals]
df = [Fs[index]/magnitude.shape[0] for index, magnitude in enumerate(magnitudes)]
freq = [np.arange(0,Fs[index],df[index]) for index in range(0,len(Fs))]
#freq = [scipy.fftpack.fftfreq(signal.size, T[index]) for index,signal in enumerate(signals)]
normalized_magnitude = [magnitude/magnitude.shape[0] for magnitude in magnitudes]

for index in range(0,len(signals)):
    plt.figure()
    plt.title(f'Signal {index+1} in time')
    plt.xlabel('Time(s)')
    plt.ylabel('Amplitude')
    plt.plot(t[index], signals[index])

    plt.figure()
    plt.title(f'Signal {index+1} in freq domain')
    plt.xlabel('freq(Hz)')
    plt.ylabel('Magnitude')
    plt.plot(freq[index]/1000, normalized_magnitude[index])
    plt.xlim([0,Fs[index]/2000])

# pacific
s1 = [(t[0] >= i) & (t[0] < i+5) for i in range(0,20,5)]
# japan
s2 = [(t[1] >= 0) & (t[1] < 3), (t[1] >= 3) & (t[1] < 7)]

signal1 = [signals[0][cut] for cut in s1]
signal2 = [signals[1][cut] for cut in s2]

fft_signal1 = [scifft.fft(cut_signal) for cut_signal in signal1]
fft_signal2 = [scifft.fft(cut_signal) for cut_signal in signal2]

magnitudes1 = [np.absolute(fft_signal) for fft_signal in fft_signal1]
df1 = [Fs[0]/magnitude.shape[0] for magnitude in magnitudes1]
freq1 = [np.arange(0,Fs[0],df) for df in df1]
normalized_magnitude1 = [magnitude/magnitude.shape[0] for magnitude in magnitudes1]

magnitudes2 = [np.absolute(fft_signal) for fft_signal in fft_signal2]
df2 = [Fs[1]/magnitude.shape[0] for magnitude in magnitudes2]
freq2 = [np.arange(0,Fs[1],df) for df in df2]
normalized_magnitude2 = [magnitude/magnitude.shape[0] for magnitude in magnitudes2]


plt.figure()
for index, magnitude in enumerate(normalized_magnitude1):
    plt.subplot(4,1,index+1)
    plt.title(f'Som baleia Pacifico corte {index+1}')
    plt.plot(freq1[index]/1000, magnitude)
    plt.ylabel("Magnitude")
    plt.xlim([0, Fs[0] / 2000])

plt.xlabel("Frequency(Hz)")
plt.figure()

for index, magnitude in enumerate(normalized_magnitude2):

    plt.subplot(2,1,index+1)
    plt.plot(freq2[index]/1000, magnitude)
    plt.title(f'Som baleia Japão corte {index+1}')
    plt.ylabel("Magnitude")

    plt.xlim([0, Fs[1] / 2000])

plt.xlabel("Frequency(Hz)")
plt.show()


# As baleias não fazem parte da mesma espécie pois atuam em faixas de frequência diferentes
# Pacífico 1Hz ~ 2,5Hz
# Japão 0Hz ~ 5Hz