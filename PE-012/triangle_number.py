"""
Solution to Project Euler problem 12
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com


"""
import math

DIVISOR_COUNT = 500


def count_divisor_of_number(number):
    sqrt_number = int(math.sqrt(number))
    count_divsor = 0
    for index in range(1, sqrt_number + 1):
        if not number % index:
            count_divsor += 2
    if sqrt_number * sqrt_number == number:
        count_divsor -= 1
    return count_divsor


def find_first_triangle_number():
    sum_numbers = 3
    next_number = 3
    while count_divisor_of_number(sum_numbers) < DIVISOR_COUNT:
        sum_numbers += next_number
        next_number += 1
    return sum_numbers


if __name__ == "__main__":
    import time
    start = time.time()
    result = find_first_triangle_number()
    done = time.time()
    print("The first triangle number with over {} divisors is: {}".format(DIVISOR_COUNT, result))
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))

