def add(a, b):
    return a + b


def mul(a, b):
    c = 0
    for _ in range(b):
        c += a
    return c


if __name__ == '__main__':
    import sys
    if '--test' in sys.argv:
        assert add(0, 0) == 0
        assert add(20, 10) == 30
        assert mul(1, 0) == 0
        assert mul(0, 1) == 0
        assert mul(2, 6) == 12
