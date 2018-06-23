"""
Solution to Project Euler problem 19
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com


"""
import datetime


def count_sundays():
    return sum(1 for y in range(1901, 2001)
               for m in range(1, 13)
               if datetime.date(y, m, 1).weekday() == 6)


if __name__ == "__main__":
    import time
    start = time.time()
    result = count_sundays()
    done = time.time()
    print("Have {} sundays on the 1st of a month from 1901 to 2001".format(result))
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))
