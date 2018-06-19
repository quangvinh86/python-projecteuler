"""
Solution to Project Euler problem 16
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com


"""
import math


def calc_power_digit_sum(power):
    numbers = int(math.pow(2, power))
    # print(numbers)
    return sum([int(number) for number in str(numbers)])


if __name__ == "__main__":
    import time
    start = time.time()
    power = 1000
    result = calc_power_digit_sum(power)
    done = time.time()
    print("The sum digits of 2^{} is: {}".format(power, result))
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))
