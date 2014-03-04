# -*- coding: UTF-8 -*-
import pylab #Для графиков
import math  #Для sin(), cos()
import random
from numpy import * #Для функции arange(), функция поддерживает тип float для аргументов

########## Входные данные ##############

Tm=4 #Длительность сигнала
Fd=6000.0 #Частота дискретизации
FFTL=8192 #Количество линий спектра

F2=20.0 #Частота несущей

speed=10.0 #Символьная скорость
time=1/speed


random.randint(0,2)
print random.randint(0,1)
source_digital_sequence=[random.randint(0,2) for x in range(0,50)]
print source_digital_sequence

w1=2*math.pi*F2 #Угловая частота несущей

# Формируем список значений несущего сигнала сигнала, длительностью Tm, с шагом 1/Fd

g=[]
for x in xrange(0,50):
    g+=[source_digital_sequence[x]*math.sin(w1*y) for y in arange(0,time,(1.0/Fd))]
print len(arange(0,time,(1.0/Fd)))

#################  Определение функции построения графиков  #####################

def plot_signal(x,y,title,labelx,labley,position):
    pylab.subplot (3, 1, position)
    pylab.plot(x,y)
    pylab.title(title)
    pylab.xlabel(labelx)
    pylab.ylabel(labley)
    pylab.grid(True)           

plot_signal(range(0,50),source_digital_sequence,'Digital secuence','time','',1)

plot_signal(arange(0,50*time,(1.0/Fd)),g,'ASK','time','',3)

#Отображение графиков
pylab.show()
