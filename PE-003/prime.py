import math


def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif not number % 2:
        return False
    max_range = int(math.sqrt(number)) + 1
    for counter in range(3, max_range, 2):
        if not number % counter:
            return False
    return True


if __name__ == "__main__":
    print(is_prime(827063))
