GIRD = [
    [75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [95, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [17, 47, 82, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [18, 35, 87, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [20, 4, 82, 47, 65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [19, 1, 23, 75, 3, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [88, 2, 77, 73, 7, 63, 67, 0, 0, 0, 0, 0, 0, 0, 0],
    [99, 65, 4, 28, 6, 16, 70, 92, 0, 0, 0, 0, 0, 0, 0],
    [41, 41, 26, 56, 83, 40, 80, 70, 33, 0, 0, 0, 0, 0, 0],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 0, 0, 0, 0, 0],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 0, 0, 0, 0],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 0, 0, 0],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 0, 0],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 0],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]


def find_maximum_path():
    """
    Fail solution =))
    :return:
    """
    max_lenght = len(GIRD[0])
    x, y = 0, 0
    path = [75]

    for index in range(0, max_lenght - 1):
        if x + 1 <= max_lenght and y + 1 <= max_lenght:
            if GIRD[x+1][y] > GIRD[x+1][y+1]:
                path.append(GIRD[x + 1][y])
                x, y = x+1, y
            else:
                path.append(GIRD[x + 1][y + 1])
                x, y = x + 1, y + 1
        else:
            path.append(GIRD[x + 1][y])
        print(index, path)
    return sum(path)


def calc_maximum_path_v2():
    """
    swap GRID to reverse_gird and start calc from (0, 0)
    :return:
    """
    max_lenght = len(GIRD[0])
    reverse_gird = GIRD[::-1]
    for x in range(1, max_lenght):
        for y in range(0, max_lenght):
            try:
                if reverse_gird[x][y] != 0:
                    reverse_gird[x][y] = reverse_gird[x][y] + max(reverse_gird[x-1][y], reverse_gird[x-1][y + 1])
                print(x, y, reverse_gird[x][y])
            except Exception as ex:
                print(x,y, reverse_gird[x][y], ex.__str__())


def calc_maximum_path_v1():
    max_lenght = len(GIRD[0])
    for x in range(max_lenght - 2, -1, -1):
        for y in range(0, max_lenght):
                if GIRD[x][y] != 0:
                    GIRD[x][y] = GIRD[x][y] + max(GIRD[x + 1][y], GIRD[x + 1][y + 1])
    return GIRD[0][0]


if __name__ == "__main__":
    import time
    start = time.time()
    result = calc_maximum_path_v1()
    done = time.time()
    print("The maximum path sum: {}".format(result))
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))
