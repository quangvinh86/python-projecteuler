"""
Solution to Project Euler problem 10
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com


"""

import math

UPPER_LIMIT = 2000000


def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif not number % 2:
        return False
    max_range = int(math.sqrt(number)) + 1
    for counter in range(3, max_range, 2):
        if not number % counter:
            return False
    return True


def calc_summation_of_primes():
    sum_of_prime = 2
    number = 3
    while number <= UPPER_LIMIT:
        if is_prime(number):
            sum_of_prime += number
        number += 2
    return sum_of_prime


if __name__ == "__main__":
    import time
    start = time.time()
    ##
    result = calc_summation_of_primes()
    ##
    done = time.time()
    elapsed = done - start
    print("Prime sum of all primes below {} is {}".format(UPPER_LIMIT, result))
    print("elapsed time: {}s".format(elapsed))
