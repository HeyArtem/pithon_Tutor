# Дано положительное действительное число X. Выведите его дробную часть.
# print('  Дано положительное действительное число X. Выведите его дробную часть.')
# # мое реш
# from math import floor
# x = float(input('введите число с цирами после запятой: '))
# z = x*10-(floor(x)*10)
# y = float(z/10)
# print('ответ: ', y)
#
# print('Решение разработчиков')
# x = float(input())
# print(x - int(x))
#
# x=19.6
#
# Задача «МКАД»
# Длина Московской кольцевой автомобильной дороги —109 километров. Байкер Вася стартует с нулевого километра МКАД
# и едет со скоростью v километров в час. На какой отметке он остановится через t часов?
#
# Программа получает на вход значение v и t. Если v>0, то Вася движется в положительном направлении по МКАД,
# если же значение v<0, то в отрицательном.
# Программа должна вывести целое число от 0 до 108 — номер отметки, на которой остановится Вася.
# print('    Задача «МКАД»')

# Моё
# speedV = int(input('введите скорость: '))
# timeT = int(input(' Введите время: '))
# if speedV > 0:
#     distanceS = (speedV * timeT)
#     laps = distanceS//109
#     distanceS2 = (distanceS -(laps*109))
#     print(distanceS2)
# else:
#     distanceS = -(speedV * timeT)
#     laps = distanceS//109
#     distanceS2 =109 - (distanceS - (laps*109))
#     if distanceS2 == 109:
#         print(0)
#     else:
#         print(distanceS2)
#
# print('МКАД Решение разработчиков')
# a = int(input())
# b = int(input())
# print((a * b) % 109)
#
#
# # Задача «Последняя цифра числа»
# #
# # Дано натуральное число. Выведите его последнюю цифру.
# print('Задача «Последняя цифра числа»')
#
# # мое реш
# x=str(input('Введите люб цел число? Лучше неск симв'))
# print(x[-1])
#
# # От разрабов
#
# a = int(input())
# print(a % 10)
#
# print()
# # Задача «Первая цифра после точки»
# #
# # Дано положительное действительное число X. Выведите его первую цифру после десятичной точки.
# print('  Задача «Первая цифра после точки»')
#
# x = float(input('Введите число с символами после запятой: '))
# y = int(x*10)
# z = y%10
# print('символы после запятой: ', z)
#
# #ОТ разрабов
# print(' ОТ разрабов')
#
# x = float(input())
# print(int(x * 10) % 10)

print()
print('   Задача «Конец уроков»')
# Задача «Конец уроков»
#
# В некоторой школе занятия начинаются в 9:00. Продолжительность урока — 45 минут, после 1-го, 3-го, 5-го и т.д.
# уроков перемена 5 минут, а после 2-го, 4-го, 6-го и т.д. — 15 минут.
#
# Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок.
#
# Выведите два целых числа: время окончания урока в часах и минутах.


# Мое реш

всегоУроков = int(input('введите кол-во уроков, но не более 10: '))

from math import floor
# Расчет общей длины перемен
длина_5_минПер = (floor(всегоУроков/2))*5

количество_15мин_перемен = (всегоУроков- 1 - (floor(всегоУроков/2)))

длина_15_минПер = количество_15мин_перемен*15
общДлинаПеремен = длина_5_минПер + длина_15_минПер

# Расчет общей продолжительности уроков
продУроков = всегоУроков *45

урИперем = продУроков + общДлинаПеремен + (9*60)

часы = урИперем//60
минуты = урИперем - (60*часы)

print(часы, минуты)
# Реш от разрабов

print('Реш от разрабов')
a = int(input())
a = a*45 + (a//2)*5 + ((a+1)//2-1)*15
print(a//60 + 9, a%60)
# эту не веду она не синхрогизируется