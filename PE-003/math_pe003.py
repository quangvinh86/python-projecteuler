"""
Solution to Project Euler problem 3
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com

"""

import math


VICTIM_NUMBER = 600851475143


def find_largest_prime_factor_by_math():
    number = VICTIM_NUMBER
    while True:
        prime_factor = find_smallest_prime_factor(number)
        if prime_factor < number:
            number = number // prime_factor
        else:
            return prime_factor


def find_smallest_prime_factor(number):
    for index in range(2, int(math.sqrt(number) + 1)):
        if not number % index:
            return index
    return number


if __name__ == "__main__":
    import time
    print("math largest_prime_factor {} result:".format(VICTIM_NUMBER))
    start = time.time()
    print(find_largest_prime_factor_by_math())
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))

