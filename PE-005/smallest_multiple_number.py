"""
Solution to Project Euler problem 5
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com

"""

import math


def find_smallest_multiple_number_v3():
    smallest_multiple_number = 2
    for number in range(3, 21):
        smallest_multiple_number = number * smallest_multiple_number // math.gcd(smallest_multiple_number, number)
    return smallest_multiple_number


def is_divided_multi_number(number, max_div):
    for div in range(2, max_div + 1):
        if number % div:
            return False
    return True


def find_smallest_multiple_number_v1():
    smallest_multiple_number = 1
    while True:
        smallest_multiple_number += 1
        if is_divided_multi_number(smallest_multiple_number, 20):
            break
    return smallest_multiple_number


def find_smallest_multiple_number_v2():
    smallest_multiple_number = 0
    while True:
        smallest_multiple_number += 20
        if is_divided_multi_number(smallest_multiple_number, 20):
            break
    return smallest_multiple_number


if __name__ == "__main__":
    import time
    print("find_smallest_multiple_number_v1 result:")
    start = time.time()
    print(find_smallest_multiple_number_v1())
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))

    print("find_smallest_multiple_number_v2 result:")
    start = time.time()
    print(find_smallest_multiple_number_v2())
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))

    print("find_smallest_multiple_number_v3 result:")
    start = time.time()
    print(find_smallest_multiple_number_v3())
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))
