##### Задание 5.
"""
Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000.
Модуль содержит функции:
1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
2) выводит список всех делителей числа;
3) выводит самый большой простой делитель числа.
4) функция выводит каноническое разложение числа на простые множители;
5) функция выводит самый большой делитель (не обязательно простой) числа.
"""

import divisor_master as div

number = div.number_input()

'''
1) Проверка числа на простоту.
'''
# (Способ 1) Через решето Эратосфена
div.check_prime(number)

# (Способ 2) Через количество делителей
div.is_prime(number)

'''
2) Вывод списка всех делителей числа.
'''
div.divisors_list(number)

'''
3) Вывод самого большого простого делителя числа.
'''
div.max_prime_div(number)

'''
4) Функция выводит каноническое разложение числа на простые множители
'''
div.prime_factors(number)

'''
5) Функция выводит самый большой делитель (не обязательно простой) числа.
'''
div.max_divisor(number)
