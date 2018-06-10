"""
Solution to Project Euler problem 1
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com

"""

def sum_divisble_by(number, max_number):
    return number * (max_number // number) * (max_number // number + 1) / 2


def multiples_3_or_5():
    return sum_divisble_by(3, 999) + sum_divisble_by(5, 999) - sum_divisble_by(15, 999)


if __name__ == "__main__":
    import time
    print("math multiples_3_or_5 result:")
    start = time.time()
    print(multiples_3_or_5())
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))
