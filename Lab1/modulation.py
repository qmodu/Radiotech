# -*- coding: UTF-8 -*-
import pylab #Для графиков
import math  #Для sin(), cos()
from numpy import * #Для функции arange(), функция поддерживает float
#####################################

Tm=2.0
Fd=500.0
FFTL=8192

w=2*math.pi*10 #Угловая частота исходного сигнала
A=1 #Амплитуда исходного сигнала

# Частота сигнала 10 Гц, рисуем график на участке 0-1с, создаем список значений
S=[A*math.sin(w*x) for x in arange(0,Tm,(1.0/Fd))] 

#Делим область вывода на 3 строки, 1 столбец, выводим в первую строку (область)
pylab.subplot (7, 1, 1)
pylab.xlabel('Time (s)')
pylab.ylabel('Amplitude')
pylab.title('Source signal')
pylab.grid(True)
pylab.plot(arange(0,Tm,(1.0/Fd)),S)
print (len(arange(0,Tm,(1.0/Fd))))
######################################

w1=2*math.pi*100 #Угловая частота несущей
A1=10

# Частота сигнала 100 Гц, рисуем график на участке 0-1с, создаем список значений
M=[A1*math.sin(w1*x) for x in arange(0,Tm,(1.0/Fd))]

#Делим область вывода на 3 строки, 1 столбец, выводим во 2 строку (область)
#pylab.subplot (4, 1, 2)
#pylab.plot(arange(0,Tm,(1.0/Fd)),M)

################   Модулируем  #######################
AM=[A1*(1+A*math.sin(w*x))*math.sin(w1*x) for x in arange(0,Tm,(1.0/Fd))]
#Делим область вывода на 3 строки, 1 столбец, выводим в 3 строку (область)
pylab.subplot (7, 1, 5)
pylab.plot(arange(0,Tm,(1.0/Fd)),AM)
pylab.title('Amplitude modulation')
pylab.xlabel('Time (s)')
pylab.ylabel('Amplitude')
pylab.grid(True)
FFT_AM=fft.rfft(AM,FFTL)
FFT_S=fft.rfft(S,FFTL)
#print b
#print len(arange(0,Fd,(Fd/FFTL)))
#print 'F'
#print len(abs(b))
pylab.subplot (7, 1, 7) 
pylab.plot(arange(0,((Fd/2)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_AM)/len(arange(0,Tm,(1.0/Fd))))
pylab.title('Spectrum of AM signal')
pylab.xlabel('Frequency (Hz)')
pylab.ylabel('Amplitude')
pylab.grid(True)
pylab.subplot (7, 1, 3)
pylab.plot(arange(0,((Fd/2)+(Fd/FFTL)),(Fd/FFTL)),abs(FFT_S)/len(arange(0,Tm,(1.0/Fd))))
pylab.title('Spectrum of source signal')
pylab.xlabel('Frequency (Hz)')
pylab.ylabel('Amplitude')
pylab.grid(True)
pylab.show()
