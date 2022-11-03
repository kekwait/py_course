# 1. Среднее
# Дано: 3 случайных числа.
# Задание: написать программу, которая будет вычислять среднее значение этих чисел.
# Пример: (52 + 56 + 60) / 3 = 56

from random import randint


def random_average(n: int):
    i = 1
    sum = 0
    while i <= n:
        num = randint(0, 100)
        sum += num
        i += 1
    return sum / n


# 2. Деление и еще раз деление
# Дано: 2 случайных числа.
# Задание: написать программу, которая будет печать результат целочисленного деления этих  чисел,
# а также остаток от деления первого от второго.
# Пример: x = 177 и y = 10
# Результат: 17, 7

def division(numerator: int, denominator: int):
    return numerator // denominator, numerator % denominator


# 3. Округление
# Дано: число с плавающей точкой.
# Задание: написать программу, которая будет округлять заданное число:
# 1) 2х знаков после запятой; 2) до целого; 3) дополнять слева столько нулей, сколько не хватает числу до 11 знаков.
# Пример: x = 14.721
# 1) 14.72
# 2) 15
# 3) 0000014.721

def ceiling(num: float):
    return round(num, 2), round(num), '{:0>11}'.format(num)


# [Junior] 4. Число "наоборот"
# Дано: целое число (int).
# Задание: написать программу, которая будет инвертировать целое число
# Пример: 1) x = 123 -> 321 2) x = -325 -> -523 3) x = 0 -> 0

def inverse_num(num: int):
    new_num = 0
    k = 1
    if num < 0:
        k = -1
        num *= k
    while True:
        digit = num % 10
        num = num // 10
        new_num = (new_num * 10) + digit
        if num == 0:
            return new_num * k


# [Junior+] 5. Число "наоборот" (усложненное)
# Дано: целое число (int).
# Задание: написать программу, которая будет инвертировать целое число.
# Если инвертированное число выходит за границы (32-bit integer)
# Пример:
# 1) x = 123 -> 321 2) x = -325 -> -523 3) x = 0 -> 0 4) x = 1563847412 -> 0

def inverse_num_v2(num: int):
    new_num = 0
    k = 1

    if num < 0:
        k = -1
        num *= k
    if abs(num) == 7463847412:
        return 2147483647 * k
    while True:
        digit = num % 10
        num = num // 10
        new_num = (new_num * 10) + digit
        if new_num > 2147483647:
            return 0
        if num == 0:
            return new_num * k


print(random_average(3))
print(division(177, 10))
a, b, c = ceiling(14.721)
print(a, b, c)
print(inverse_num(123), inverse_num(-325), inverse_num(0))
print(inverse_num_v2(123), inverse_num_v2(-325), inverse_num_v2(0), inverse_num_v2(1563847412))
