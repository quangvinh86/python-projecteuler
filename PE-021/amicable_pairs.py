"""
Solution to Project Euler problem 21
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com


"""
import math

LIMIT_NUMBER = 100000
sum_divisor_dict = {}


def get_sum_divisor_numbers(number):
    if number in sum_divisor_dict:
        return sum_divisor_dict[number]
    sqrt_of_number = int(math.sqrt(number))
    sum_total = 1
    if number == sqrt_of_number * sqrt_of_number:
        sum_total += sqrt_of_number
        sqrt_of_number -= 1
    for index in range(2, sqrt_of_number):
        if number % index == 0:
            sum_total += index + number // index
    sum_divisor_dict[number] = sum_total
    return sum_total


def is_amicable_pairs(number):
    sum_number = get_sum_divisor_numbers(number)
    if number == get_sum_divisor_numbers(sum_number) and number != sum_number:
        return True, number, sum_number
    else:
        return False, 0, 0


def get_sum_amicable_pair_numbers():
    list_amicable_pairs = []
    for number in range(5, LIMIT_NUMBER + 1):
        if number not in list_amicable_pairs:
            result = is_amicable_pairs(number)
            if result[0]:
                list_amicable_pairs.append(result[1])
                list_amicable_pairs.append(result[2])
    return sum(list_amicable_pairs)


if __name__ == "__main__":
    import time
    start = time.time()
    result = get_sum_amicable_pair_numbers()
    done = time.time()
    print("The largest sum of all amicable pairs less than {}: {}".format(LIMIT_NUMBER, result))
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))
