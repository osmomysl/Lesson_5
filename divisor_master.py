

'''
1) Проверка числа на простоту.
'''

n = 1000


def number_input():
    while True:
        try:
            print('Введите любое натуральное число от 1 до ', n, ': ', sep='', end='')
            x = int(input())
            if 1 <= x <= n:
                break
        except ValueError:
            pass
    return x


if __name__ == '__main__':
    num = number_input()

########### Число x является простым, если оно больше 1 и при этом делится без остатка только на 1 и на x.

# Вариант 1: определить все простые числа на отрезке от 1 до 1000 и проверить, входит ли указанное число в список.


def erat(n):
    # Создадим список простых чисел, используя метод "решето Эратосфена" (Sieve of Eratosthenes)
    # 2 - наименьшее простое. Создаём список всех натуральных чисел от 2 до n включительно
    sieve = [i for i in range(2, n + 1)]
    for p in range(len(sieve)):
        composites = [num * sieve[p] for num in sieve  # Выбираем составные числа с условиями:
                      if sieve[p] ** 2 <= (num * sieve[p]) <= n]
        # Список начинается с квадрата выбранного числа - не обязательно, но это показывает,
        # какие составные числа мы убираем из списка 'sieve' на каждой итерации;
        # Нам нужны составные числа не больше заданного числа n.
        if composites:  # Если список составных не пуст,
            sieve = list(
                set(sieve) - set(composites))  # вычитаем из множества натуральных чисел множество составных.
            sieve.sort()  # После преобразования множества обратно в список сортируем его, чтобы избежать ошибок.
            # print(p, 'composites', composites, sep =': ')
            # print(p, 'naturals', sieve, sep = ': ')
            # print('natural numbers left:', len(sieve))
            # В итоге, остались только простые числа.
        else:
            break
    return sieve


def check_prime(num):
    if num == 1:
        pass
    elif num in erat(num):
        return print('(Способ 1) Простое')
    else:
        return print('(Способ 1) Составное')


if __name__ == '__main__':
    check_prime(num)


###########
# Вариант 2: проверить, есть ли делители, кроме 1 и самого числа.

def is_prime(num):    # Проверка на простоту через делители.
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    odds = [i for i in range(num + 1) if i % 2 != 0]
    if num == 1:
        return print('Единица имеет ровно один делитель и не является ни простым, ни составным.')
    # Все простые числа, кроме "2" - нечётные. По определению в списке их делителей только два числа.
    elif num == 2 or (num in odds and len(divisors) == 2):
        return print('(Способ 2) Простое')
    else:
        return print('(Способ 2) Составное')


if __name__ == '__main__':
    is_prime(num)

'''
2) Вывод списка всех делителей числа.
'''


def divisors_list(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return print('Делители числа: ', divisors)


if __name__ == '__main__':
    divisors_list(num)

'''
3) Вывод самого большого простого делителя числа.
'''


def max_prime_div(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    odds = [i for i in range(num + 1) if i % 2 != 0]
    for i in range(1, len(divisors)):
        max_div = divisors[-i]    # Перебираем делители числа, начиная с конца и проверяем на простоту.
        div_check = [d for d in range(1, max_div + 1)
                     if max_div % d == 0]
        if max_div in odds and len(div_check) == 2 or max_div == 2:
            return print('Наибольший простой делитель:', max_div)
        else:
            continue


if __name__ == '__main__':
    max_prime_div(num)

'''
4) Функция выводит каноническое разложение числа на простые множители
'''
"""
a=p1⋅a1, где a1=a:p1, 
a=p1⋅a1=p1⋅p2⋅a2, где a2=a1:p2, …, 
a=p1⋅p2⋅…⋅pn⋅an, где an=an−1:pn. 
При получении an=1 равенство принимает вид 
a=p1⋅p2⋅…⋅pn  
Заметим, что p1≤p2≤p3≤…≤pn.
"""


def prime_factors(num):
    if num == 1:
        pass
    else:
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        from collections import Counter
        factor = []
        a = num
        for p in divisors:
            while p in erat(a) and a % p == 0:
                a = int(a / p)
                factor.append(p)
        degree = Counter(factor)
        keys = list(degree.keys())
        print('Каноническое разложение на простые множители:')
        print(factor)

        def print_factorization():
            if num not in erat(num):    # Не выполняем разложение на множители для простых чисел.
                print(num, '=', end=" ")
                for i in range(len(degree)):
                    if i < len(degree) - 1:
                        if degree[keys[i]] > 1:
                            print(keys[i], '^', sep='', end="")
                            print(degree[keys[i]], '*', end=" ")
                        else:
                            print(keys[i], '* ', end="")
                    else:
                        if degree[keys[i]] > 1:
                            print(keys[i], '^', sep='', end="")
                            print(degree[keys[i]])
                        else:
                            print(keys[i])
            else:
                pass
        return print_factorization()


if __name__ == '__main__':
    prime_factors(num)


'''
5) Функция выводит самый большой делитель (не обязательно простой) числа.
'''


def max_divisor(num):
    if num == 1:
        pass
    else:
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        max_div = divisors[-2]    # Нас интересует наибольший делитель, отличный от самого числа.
        return print('Наибольший собственный делитель:', max_div)


if __name__ == '__main__':
    max_divisor(num)
