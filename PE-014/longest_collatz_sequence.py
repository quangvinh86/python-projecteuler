"""
Solution to Project Euler problem 14
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com


"""
UPPER_LITMIT = 1000000


def count_collatz_sequence(number):
    count = 1
    while number != 1:
        if number % 2:
            number = 3 * number + 1
        else:
            number = number // 2
        count += 1
    return count


def find_longest_collatz_sequence():
    count_cache = {1: 1, 2: 2}
    max_lenght = 2
    max_lenght_number = 2
    for sequence in range(3, UPPER_LITMIT + 1):
        lenght = 1
        number = sequence
        while number != 1:
            if number % 2:
                number = 3 * number + 1
            else:
                number = number // 2
            if number in count_cache:  # count_cache[number] != -1:
                lenght += count_cache[number]
                break
            lenght += 1
        count_cache[sequence] = lenght
        if max_lenght < lenght:
            max_lenght = lenght
            max_lenght_number = sequence
    return max_lenght_number, max_lenght


if __name__ == "__main__":
    import time
    start = time.time()
    result = find_longest_collatz_sequence()
    done = time.time()
    print("The starting number {} produces a sequence of {}".format(*result))
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))
