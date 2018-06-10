"""
Solution to Project Euler problem 7
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com


"""

UPPER_LIMIT = 10001


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    counter = 3
    while counter * counter <= number:
        if number % counter:
            counter += 2
        else:
            return False
    return True


def find_10001st_prime_number():
    counter = 2
    prime_number = 3
    while counter < UPPER_LIMIT:
        prime_number += 2
        if is_prime(prime_number):
            counter += 1
    return prime_number


if __name__ == "__main__":
    import time
    print("find_10001st_prime_number of result:")
    start = time.time()
    print(find_10001st_prime_number())
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))
