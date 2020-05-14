import divisor_master as div

#######
# Начнём с наивных тестов, потому что непонятно, как это реализовать в Pytest.

# def number_input_test():
#     output = div.number_input()
#     if type(output) == int and 1001 > output > 0:
#         print('Respect +')
#     else:
#         print('Wasted')
# number_input_test()

####### pytest

def test_1_erat():
    assert div.erat(1) == []
    assert div.erat(2) == [2]

def test_2_erat():
    assert div.erat(1000) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]



def max_divisor(num):
    if num == 1:
        pass
    else:
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        max_div = divisors[-2]
        return max_div


def test_1_max_divisor():
    assert max_divisor(1) is None
def test_2_max_divisor():
    assert max_divisor(200) == 100


####### Попробуем Unittest.
import unittest


def divisors_list(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

# print(divisors_list(0))
# print(divisors_list(1))
# print(divisors_list(10))
# print(divisors_list(199))


class Test_divisors_list(unittest.TestCase):
    def test_unit_1(self):
        self.assertEqual(divisors_list(1), [1])
    def test_unit_2(self):
        self.assertTrue(divisors_list(199) == [1, 199])
    def test_unit_3(self):
        self.assertFalse(divisors_list(10) == [1, 2, 5])

