import numpy as np
import re

class Counter:
    """Counter """
    def __init__(self, initial=0):
        self.value = initial

    

# def f(x):
#   print(x)

# def world_aq(s):
#   return s[0] + s[1:].replace(s[0], '*')

# print(world_aq('chekout'))



# class Perceptron:
    
#     def __init__(self, input_length, weights=None):
#         if weights is not None:
#             self.weights = np.ones(input_length) * 0.5
#         else:
#             self.weights = weights
        
#     @staticmethod
#     def unit_step_function(x):
#         if x > 0.5:
#             return 1
#         return 0
        
#     def __call__(self, in_data):
#         weighted_input = self.weights * in_data
#         weighted_sum = weighted_input.sum()
#         return Perceptron.unit_step_function(weighted_sum)
    
# p = Perceptron(2, np.array([0.5, 0.5]))
# for x in [np.array([0, 0]), np.array([0, 1]), 
#           np.array([1, 0]), np.array([1, 1])]:
#     y = p(np.array(x))
#     print(x, y)


# def get_links(chat_string):
#     return re.sub(r'[/%-]',' ', chat_string)

# input_raw = '/twitter-com-tus/'
# links = get_links(input_raw)


# a = [5, 10, 11, 7, 2]
# b = []
# for i in range(len(a)-1):
#     b.append(a[i+1] + a[i-1])
    
# print(b)


# какой есть метод, чтобы длинный массив сложить в массив массивов по 3 элемента?

"""  """

# short_arrays = [long_array[i:i+3] for i in range(0, len(long_array), 3)]

""" Ну как менять этот стейт что бы clear? """

# from itertools import cycle
# from time import sleep, time
# from time import time


# start_time = time()

# time_finish = time() - start_time

# print("--- {time_finish} seconds ---".format(time_finish))

# finish = time() + 2
# load_state = cycle(['\\', '|', '/', '-'])
# for state in load_state:
#     if time() >= finish:
#         break
#    # print('\r' + state, end='')
#    print('\rWaiting {state}'.format(state=state), end='')
#    sleep(0.5)


# finish = time()+n
# while 1:
#     if time() >= finish:
#         break


""" 
if not x == foo: пишут индусы
if x != foo: нормальные люди

"""


# a = [5]
# b = a[0]
# for i in b:
#     print(i, end = " ")


# import time
# from itertools import cycle
# from time import sleep

# start = time.time()
# load_state = cycle(['\\', '|', '/', '-'])


# for state in load_state:
#   print('\rWaiting {state}'.format(state=state), end='')
#   # print('--- seconds {start} ---'.format(start=time.time() - start))
#   sleep(0.5)
#   # через пять секунд завершиться
#   if time.time() - start > 5:
#     break
# print("finish")



"""
>>> a = [10, 20, 30, 40]
>>> b = ['a', 'b', 'c', 'd', 'e']
>>> for i, j in zip(a, b):
...     print(i, j)
... 
10 a
20 b
30 c
40 d


Здесь выражение zip(a, b) создает объект-итератор, 
из которого при каждом обороте цикла извлекается кортеж, состоящий из двух элементов. Первый берется из списка a, второй - из b. 

Добавлено в Python 2.0
Возвращает итератор по кортежам, где i-тый кортеж содержит i-тый элемент каждой из указанных последовательностей.


zip(*iterables)  -> +py3.0 iterator -py3.0 list
iterables -- Итерируемые объекты, элементы которых следует упаковать в кортежи. Если передана одна последовательность, 
вернётся итератор по кортежам, состоящим из единственного элемента. Если последовательности не переданы, возвращается пустой итератор.
"""


# for i, ii in zip(a, a[1:]):
#     print(i + ii)

# return int(''.join(str(int(i) ** 2 for i in num))




""" 
class foo():
    a=1
    def __init__(self):
        self.b=2
f=foo()
f.__dict__
почему "а" не показывает? {'b':2}. Если "b" ' это атрибут класса, то что такое "а"?

b это атрибут экземпляра, a это класса.
Атрибуы экземпляра лежат в instance.__dict__, атрибуты класса в ClassName.__dict__. 

Не "одинаковый" а он просто один, а у экземпляров лукап работает что если у экземпляра нет то смотрим у класса.

То есть это такой поиск атрибутов по имени. С начало ищет в экземпляре потом у родителя. И если у экземпляра сделать b.a = 10 то у 
экземпляра появится атрибут a=10 при этом у класса будет свой а=1. Правильно мыслю?

"""


""" 
народ, а чтобы всё содержимое из файла вписать в переменную, нужно же так сделать? 
with open(filename) as fp:
    data = fp.read()
"""

""" 
Нужно запустить внешнюю программу и получить: 

from subprocess import Popen, PIPE

out, err = Popen('/tmp/somebody-kill-me.sh', stdout=PIPE).communicate()
print 'Control returned? Yeah!'
print 'Out:\n', out

как и сказали выше, указываешь subprocess.PIPE в stdout и stderr, - их можно считывать и с помощью простого Popen.stdout.read()
код возврата можно получить через Popen.wait() или через Popen.returncode.
также обрати внимание на параметр timeout метода Popen.wait()
чтобы отслеживать состояние процесса, можно обвернуть wait в цикл.
убить процесс можно по Popen.kill() или terminate() или послав сигнал соотв командой.

ля упрощения запуска команд, в пути которых есть пробелы, существует os.startfile:

import os
os.startfile(r'c:/Program Files/Mozilla Firefox/firefox.exe')
os.startfile принимает простой текст, без необходимости заключать в кавычки имена папок с пробелами.
"""


# if __name__ == '__main__':
#     f('Admin')
#     print(links)


""" list and join """
word_letter = "word"
text_new = list('*' * len(word_letter))
print(''.join(text_new))

while "*" in text_new:
    user = input("Type: ")
    for letter in range(len(word_letter)):
        if user == word_letter[letter]:
            text_new[letter] = user
    print(''.join(text_new))    

    # dop = ''
    # for letter in range(len(word_letter)):
    #     if user == word_letter[letter]:
    #         dop = dop + user
    #     else:
    #         dop = dop + text_new[letter]
    # text_new = dop
    # print(text_new)

print("-----------------------------------")

""" ИСКЛЮЧЕНИЕ. """
# try:
#     1 + "42"
# except TypeError as e:
#     # print("No plus")
#     print(e)





print("Error")
