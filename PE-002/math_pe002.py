"""
Solution to Project Euler problem 2
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com

"""

def sum_fibonacci_under_4_million():
    fi_n_6 = 2
    fi_n_3 = 8
    sum_even = fi_n_3 + fi_n_6
    fi_n = 4 * fi_n_3 + fi_n_6
    while fi_n < 4000000:
        sum_even += fi_n
        fi_n_3, fi_n_6 = fi_n, fi_n_3
        fi_n = 4 * fi_n_3 + fi_n_6
    return sum_even


if __name__ == "__main__":
    import time
    print("math fibonacci result:")
    start = time.time()
    print(sum_fibonacci_under_4_million())
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))

