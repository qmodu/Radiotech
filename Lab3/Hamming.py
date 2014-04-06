# -*- coding: UTF-8 -*-
import random

N = 4                   #Количество символов в последовательности
Hamming = [7, 4]        #Код Хемминга (7,4,3)

# Для хранения разрядов числа в списке используется прямой порядок (litle-endian order), т.е. A0,A1,A2,A3,
# в отличии от записи числа арабскими цифрами (big-endian), т.е A3,A2,A1,A0.


#source_sequence = [random.randint(0, 1) for x in xrange(0, N)]
source_sequence = [1, 0, 1, 1]
print 'Исходная последовательность\n', source_sequence, '\n'
code_sequence = [((source_sequence[0] + source_sequence[1]) % 2 + source_sequence[3]) % 2,  # c0
                 ((source_sequence[0] + source_sequence[2]) % 2 + source_sequence[3]) % 2,  # c1
                 source_sequence[0],                                                        # a0
                 ((source_sequence[1] + source_sequence[2]) % 2 + source_sequence[3]) % 2,  # c2
                 source_sequence[1],                                                        # a1
                 source_sequence[2],                                                        # a2
                 source_sequence[3]]                                                        # a3

print 'Кодированная последовательность\n', code_sequence, '\n'
print 'c0 ', code_sequence[0]
print 'c1 ', code_sequence[1]
print 'c2 ', code_sequence[3]
# noise = [random.randint(0, 1) for x in xrange(0, Hamming[0])]
# print noise

# output_sequence = []
# for x in xrange(0, N):
#     output_sequence.append((source_sequence[x] + noise[x]) % 2
#
# print output_sequence


# Проверка контрольных символов
decode_sequence = [1, 0, 1, 0, 0, 1, 1]
print 'Кодированная c ошибкой последовательность\n', decode_sequence, '\n'
print 'c0 ', decode_sequence[0]
print 'c1 ', decode_sequence[1]
print 'c2 ', decode_sequence[3], '\n'

#####################################################################################
# Расчет контрольных соотношений для каждого из проверочных символов Ci на основе полученного кода
# с0 = a0 + a1 + a3
# с1 = a0 + a2 + a3
# с2 = a1 + a2 + a3
# Сравнение расчитанных контрольных значений с принятыми
#####################################################################################
c0 = ((decode_sequence[2] + decode_sequence[4]) % 2 + decode_sequence[6]) % 2
print 'C0 ', c0
c1 = ((decode_sequence[2] + decode_sequence[5]) % 2 + decode_sequence[6]) % 2
print 'C1 ', c1
c2 = ((decode_sequence[4] + decode_sequence[5]) % 2 + decode_sequence[6]) % 2
print 'C2 ', c2

# Для определения позиции искаженного символа суммируем веса искаженных проверочных символов
w1 = w2 = w3 = 0

if c0 != decode_sequence[0] or c1 != decode_sequence[1] or c2 != decode_sequence[3]:
    if c0 != decode_sequence[0]:
        w1 = 1
    if c1 != decode_sequence[1]:
        w2 = 2
    if c2 != decode_sequence[3]:
        w3 = 4

        # Нумерация элементов в списке начинается с 0, вычитаем 1
        syndrome = w1 + w2 + w3 - 1
        print 'Ошибка в', syndrome, 'разряде\n'

        if decode_sequence[syndrome] == 1:
            decode_sequence[syndrome] = 0
        else:
            decode_sequence[syndrome] = 1

print 'Исправленная последовательность\n', decode_sequence, '\n'

for x in xrange(0, 6):
    if code_sequence[x] != decode_sequence[x]:
        print "Последовательности не совпадают. Количество ошибок больше, чем может исправить данный код"
        break
    else:
        print '#########  Все ошибки исправлены!  #########'
        break
