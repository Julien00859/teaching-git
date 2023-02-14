def add(a, b):
    """ Compute the sum of two numbers """
    return a + b


if __name__ == '__main__':
    assert add(1, 2) == 3
    assert add(1, 0) == 1
    assert add(-2, 1) == -1
    print("ok")
