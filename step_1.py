# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.


# строка ввода секунд
sec = int(input('Введите число '))
# в часе 3600 секунд
hour = str(sec // 3600)
# в минуте 60 секунд
mine = (sec // 60) % 60
sec = sec % 60
if mine < 10:
    mine = '0' + str(mine)
else:
    mine = str(mine)
if sec < 10:
    sec = '0' + str(sec)
else:
    sec = str(sec)
print(hour + " часов" + ':' + mine + " минут" + ':' + sec + " секунд/ы")

# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# спрашиваем неизвестное
n = input("Введите число: ")
n = int(n)
# узнаем nn умножив на 11
nn = int(n) * 11
# аналогично узнаем nnn умножив на 111
nnn = int(n) * 111
print(nnn + nn + n)

# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
# узнаем число 
num = int(input("Введите число "))
# mak - максиммальное число и введенном + исклчаем остаток от деления и ставим деление целого числа
mak = num % 10
num = num // 10
# цикл проверки
while num > 0:
    if num % 10 > mak:
        mak = num % 10
    num = num // 10
print(mak)

""" Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль - выручка больше издержек или убыток - издержки больше выручки). 
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника. """

# работает.но мне хотелось бы еще доработать ее от возможности вводить буквы,
# попытки были но в итоге крашится, есть предположение что надо каждое действие в if\else оборачивать а потом уже в try \ except


# prib - прибыль
prib = input("Какая прибыль? ")
prib = int(prib)
# izde - издержки
izd = input("Какие издержки? ")
izd = int(izd)
if izd <= prib:
    print("Работаем в плюс")
    # suum - выручка
    suum = input("А какая выручка товарищЪ? ")
    suum = int(suum)
    # rent - рентабельность по формуле прибыль / выручку * 100
    rent = (prib / suum * 100)
    rent = int(rent)
    print("Рентабельность равна " + str(rent) + " едениц-ы ")
    # sot - количество сотрудников
    sot = input("Сколько сотрудников в компании? ")
    sot = int(sot)
    # doh - доход на 1 сотрудника
    doh = (prib / sot)
    doh = int(doh)
    print("Доход на 1 сотрудника составляет " + str(doh) + " единиц-ы ")
else:
    print("Работаем в минус")

"""Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10% относительно предыдущего. 
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. 
Программа должна принимать значения параметров a и b и выводить одно натуральное число - номер дня.
"""

