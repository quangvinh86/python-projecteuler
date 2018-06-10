"""
Solution to Project Euler problem 4
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com

"""

def make_palindrome_number(first_half):
    return int(str(first_half) + str(first_half)[::-1])


def check_3_digit_numbers_product(palin):
    for number in range(999, 99, -1):
        if not palin % number:
            temp_number = palin // number
            if 100 <= temp_number <= 999:
                return True
    return False


def find_largest_palindrome_product():
    for first_half in range(997, 110, -1):
        palin = make_palindrome_number(first_half)
        if check_3_digit_numbers_product(palin):
            return palin
    return None


if __name__ == "__main__":
    import time
    print("Find_largest_palindrome_product result:")
    start = time.time()
    print(find_largest_palindrome_product())
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))
