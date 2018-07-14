"""
Solution to Project Euler problem 24
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com


"""

import math

LIMIT_NUMBER = 1000000


def find_millionth_lexicographic_permutation():
    perm = [_ for _ in range(0, 10)]
    numbers = [str(_) for _ in range(0, 10)]
    count = len(perm)
    perm_num = ""
    remain = LIMIT_NUMBER - 1

    for index in range(1, 10):
        step = remain // math.factorial(count - index)
        remain = remain % math.factorial(count - index)
        perm_num = perm_num + numbers[step]
        numbers.pop(step)
        if remain == 0:
            break

    for item in numbers:
        perm_num += item

    return perm_num


if __name__ == "__main__":
    import time
    start = time.time()
    result = find_millionth_lexicographic_permutation()
    done = time.time()
    print("The {}st lexicographic permutation is: {}".
          format(LIMIT_NUMBER, result))
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))
