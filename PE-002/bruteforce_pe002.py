"""
Solution to Project Euler problem 2
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com

"""

def sum_fibonacci_under_4_million():
    fi_1st = 1
    fi_2nd = 2
    sum_even = fi_2nd
    fi_n = fi_1st + fi_2nd
    while fi_n < 4000000:
        if not fi_n % 2:
            sum_even += fi_n
        fi_1st, fi_2nd = fi_2nd, fi_n
        fi_n = fi_1st + fi_2nd
    return sum_even


if __name__ == "__main__":
    import time
    print("bruteforce fibonacci result:")
    start = time.time()
    print(sum_fibonacci_under_4_million())
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))

