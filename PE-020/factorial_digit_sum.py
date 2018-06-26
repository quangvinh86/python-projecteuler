"""
Solution to Project Euler problem 20
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com


"""
import math

NUMBER = 100


def sum_number_factorial():
    factorial_number = math.factorial(NUMBER)
    return sum(int(index) for index in str(factorial_number))


if __name__ == "__main__":
    import time
    start = time.time()
    result = sum_number_factorial()
    done = time.time()
    print("sum_all digit in factorial of {} is {}".format(NUMBER, result))
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))
