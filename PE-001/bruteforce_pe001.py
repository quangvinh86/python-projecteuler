"""
Solution to Project Euler problem 1
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com

"""

def multiples_3_or_5_v1():
    sum_all = 0
    for number in range(3, 1000):
        if not number % 3 or not number % 5:
            sum_all += number
    return sum_all


def multiples_3_or_5_v2():
    return sum([number for number in range(3, 1000) if not number % 3 or not number % 5])


if __name__ == "__main__":
    import time
    print("bruteforce multiples_3_or_5_v1 result:")
    start = time.time()
    print(multiples_3_or_5_v1())
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))

    print("bruteforce multiples_3_or_5_v2 result:")
    start = time.time()
    print(multiples_3_or_5_v2())
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))
