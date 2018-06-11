"""
Solution to Project Euler problem 9
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com


"""


def find_pythagorean_triplets(sum_triple):
    for a in range(1, int(sum_triple // 3)):
        for b in range(a, int(sum_triple // 2)):
            c = sum_triple - a - b
            if a * a + b * b == c * c:
                return (a, b, c), a * b * c
    return None, None


if __name__ == "__main__":
    import time
    sum_triple = 1000
    start = time.time()
    result = find_pythagorean_triplets(sum_triple)
    print("The Pythagorean triple is {},  the sum is {} , the product is {}".format(result[0], sum_triple, result[1]))
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))
