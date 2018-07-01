"""
Solution to Project Euler problem 23
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com


"""
import math

LIMIT_NUMBER = 28123
sum_divisor_dict = {}


def get_sum_divisor_numbers(number):
    if number in sum_divisor_dict:
        return sum_divisor_dict[number]
    sqrt_of_number = int(math.sqrt(number))
    sum_total = 1
    if number == sqrt_of_number * sqrt_of_number:
        sum_total += sqrt_of_number
        sqrt_of_number -= 1
    for index in range(2, sqrt_of_number + 1):
        if number % index == 0:
            sum_total += index + number // index
    sum_divisor_dict[number] = sum_total
    return sum_total


def is_abundant_number(number):
    sum_number = get_sum_divisor_numbers(number)
    if number < sum_number:
        return True
    else:
        return False


def get_all_abundant_number():
    bundant_numbers = []
    for number in range(12, LIMIT_NUMBER + 1):
        if is_abundant_number(number):
            bundant_numbers.append(number)
    return bundant_numbers


def find_sum_all_non_abundant_sums():
    bundant_numbers = get_all_abundant_number()
    limit_numbers = [index for index in range(0, LIMIT_NUMBER + 1)]
    for number_1 in bundant_numbers:
        for number_2 in bundant_numbers:
            if number_1 + number_2 <= LIMIT_NUMBER:
                limit_numbers[number_1 + number_2] = 0
            else:
                break
    return sum(limit_numbers)


if __name__ == "__main__":
    import time
    start = time.time()
    result = find_sum_all_non_abundant_sums()
    done = time.time()
    print("The sum of all numbers below {} that cannot be written as the sum of two abundant numbers is {}".
          format(LIMIT_NUMBER, result))
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))
