# -*- coding: UTF-8 -*-
import pylab #Для графиков
import math  #Для sin(), cos()
import random
from numpy import * #Для функции arange(), функция поддерживает тип float для аргументов

########## Входные данные ##############

Fd=200.0 #Частота дискретизации аналогового несущего сигнала
Fdd=500.0 #Частота дискретизации цифрового исходного сигнала
Fc=20.0 #Частота несущей
N=30 #Количество передающихся символов
speed=10.0 #Символьная скорость (частота символов)
duration=1/speed #Длительность импульса
time_signal=N*duration #Длительность исходного сигнала из N импульсов
M=3 #Количество уровней модуляции

# Формируем исходную последовательность символов
source_digital_sequence=[random.randint(0,M) for x in range(0,N)]

Wc=2*math.pi*Fc #Угловая частота несущей

# Формируем список значений исходного сигнала
source_digital_signal=[]
for x in range(0,N):
    source_digital_signal+=[source_digital_sequence[x] for y in arange(0,duration,(1.0/Fdd))]

# Формируем список значений модулированного сигнала
ASK=[]
for x in xrange(0,N):
    ASK+=[source_digital_sequence[x]*math.sin(Wc*t) for t in arange(0,duration,(1.0/Fd))]


#################  Определение функции построения графиков  #####################

def plot_signal(x,y,title,labelx,labley,position):
    pylab.subplot (2, 1, position)
    pylab.plot(x,y)
    pylab.title(title)
    pylab.xlabel(labelx)
    pylab.ylabel(labley)
    pylab.grid(True)

plot_signal(arange(0,time_signal,(1.0/Fdd)),source_digital_signal,'Digital sequence','time','',1)
plot_signal(arange(0,time_signal,(1.0/Fd)),ASK,'ASK','time','',2)

#Отображение графиков
pylab.show()
