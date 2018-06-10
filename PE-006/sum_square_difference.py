"""
Solution to Project Euler problem 6
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com


"""


def find_sum_square_difference(number=100):
    sum_number = number * (number + 1) / 2
    sum_square = number * (number + 1) * (2 * number + 1) / 6
    return sum_number * sum_number - sum_square


if __name__ == "__main__":
    import time
    number = 1000000
    print("find_sum_square_difference of {} result:".format(number))
    start = time.time()
    print(find_sum_square_difference(number))
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))

