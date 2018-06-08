import math


def is_prime(number):
    if number <= 1:
        return False
    for index in range(2, int(math.sqrt(number)) + 1):
        if not number % index:
            return False
    return True
