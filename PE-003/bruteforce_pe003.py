"""
Solution to Project Euler problem 3
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com

"""

import math
from prime import is_prime

VICTIM_NUMBER = 600851475143


def find_largest_prime_factor_by_bruteforce():
    largest_prime_factor = 0
    for number in range(2, int(math.sqrt(VICTIM_NUMBER)) + 1):
        if not VICTIM_NUMBER % number and is_prime(number):
            if largest_prime_factor < number:
                    largest_prime_factor = number
    return largest_prime_factor


if __name__ == "__main__":
    import time
    print("bruteforce largest_prime_factor {} result:".format(VICTIM_NUMBER))
    start = time.time()
    print(find_largest_prime_factor_by_bruteforce())
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))

