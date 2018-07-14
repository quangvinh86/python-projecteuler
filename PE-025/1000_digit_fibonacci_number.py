"""
Solution to Project Euler problem 25
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com


"""
import math

LIMIT_NUMBER = 1000


def find_fibonacci_number():
    fi_1 = 1
    fi_2 = 1
    fi_3 = fi_1 + fi_2
    limit = 10 ** (LIMIT_NUMBER - 1)
    index = 3
    while fi_3 <= limit:
        fi_2, fi_1 = fi_3, fi_2
        fi_3 = fi_2 + fi_1
        index += 1
    return index


if __name__ == "__main__":
    import time
    start = time.time()
    result = find_fibonacci_number()
    done = time.time()
    print("The first term in the fibonnaci sequence to have more than {} digits is term number: {} ".
          format(LIMIT_NUMBER, result))
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))
