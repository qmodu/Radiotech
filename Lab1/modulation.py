# -*- coding: UTF-8 -*-
import pylab #Для графиков
import math  #Для sin(), cos()
from numpy import * #Для функции arange(), функция поддерживает float
#####################################

Tm=4.0 #Длительность сигнала
Fd=6000.0 #Частота дискретизации
FFTL=8192 #
F1=200.0 #Частота исходного сигнала
F2=2000.0 #Частота несущей

w=2*math.pi*F1 #Угловая частота исходного сигнала
A=1 #Амплитуда исходного сигнала

# Частота сигнала 10 Гц, рисуем график на участке 0-1с, создаем список значений
S=[A*math.sin(w*x) for x in arange(0,Tm,(1.0/Fd))] 

#Делим область вывода на 3 строки, 1 столбец, выводим в первую строку (область)
pylab.subplot (9, 1, 1)
pylab.xlabel('Time (s)')
pylab.ylabel('Amplitude')
pylab.title('Source signal')
pylab.grid(True)
print len(arange(0,(3/F1),(1.0/Fd)))


pylab.plot(arange(0,(3/F1),(1.0/Fd)),S[0:(int(3*Fd/F1))])


print (len(arange(0,Tm,(1.0/Fd))))
######################################

w1=2*math.pi*F2 #Угловая частота несущей
A1=5

# Частота сигнала 100 Гц, рисуем график на участке 0-1с, создаем список значений
M=[A1*math.sin(w1*x) for x in arange(0,Tm,(1.0/Fd))]

#Делим область вывода на 3 строки, 1 столбец, выводим во 2 строку (область)
#pylab.subplot (4, 1, 2)
#pylab.plot(arange(0,Tm,(1.0/Fd)),M)

################   Модулируем  #######################
AM=[A1*(1+A*math.sin(w*x))*math.sin(w1*x) for x in arange(0,Tm,(1.0/Fd))]
#Делим область вывода на 3 строки, 1 столбец, выводим в 3 строку (область)
pylab.subplot (9, 1, 5)

pylab.plot(arange(0,(10/F1),(1.0/Fd)),AM[0:(int(10*Fd/F1))])

#pylab.plot(arange(0,Tm,(1.0/Fd)),AM)
pylab.title('Amplitude modulation')
pylab.xlabel('Time (s)')
pylab.ylabel('Amplitude')
pylab.grid(True)
FFT_AM=fft.rfft(AM,FFTL)
FFT_S=fft.rfft(S,FFTL)
FFT_M=fft.rfft(M,FFTL)
#print b
#print len(arange(0,Fd,(Fd/FFTL)))
#print 'F'
#print len(abs(b))
pylab.subplot (9, 1, 7) 
pylab.plot(arange(0,((Fd/2)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_AM)/len(arange(0,Tm/3,(1.0/Fd))))
pylab.title('Spectrum of AM signal')
pylab.xlabel('Frequency (Hz)')
pylab.ylabel('Amplitude')
pylab.grid(True)
pylab.subplot (9, 1, 3)
pylab.plot(arange(0,((Fd/2)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_S)/len(arange(0,Tm/3,(1.0/Fd))))
pylab.title('Spectrum of source signal')
pylab.xlabel('Frequency (Hz)')
pylab.ylabel('Amplitude')
pylab.grid(True)

pylab.subplot (9, 1, 9) 
pylab.plot(arange(0,((Fd/2)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_M)/len(arange(0,Tm/3,(1.0/Fd))))
pylab.title('Spectrum of AM signal')
pylab.xlabel('Frequency (Hz)')
pylab.ylabel('Amplitude')
pylab.grid(True)
pylab.show()
