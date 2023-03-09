def add(a, b):
    """ Compute the sum of two numbers """
    return a + b

def division(a, b):
    """ Compute the quotient of two numbers """
    if b == 0:
        raise DivisionByZeroError()
    return a / b

def mul(a, b):
    """ Compute the product of two numbers """
    m = 0
    for _ in range(b):
        m += a
    return m

def sub(a, b):
    """ Compute the difference of two numbers """
    return a - b

if __name__ == '__main__':
    assert add(1, 2) == 3
    assert add(1, 0) == 1
    assert add(-2, 1) == -1
    assert div(6, 2) == 3
    assert div(3, -1) == -3
    assert mul(3, 2) == 6
    assert mul(3, 0) == 0
    assert mul(-1, 5) == -5
    assert sub(1, 2) == -1
    assert sub(2, 1) == 1
    assert sub(1, 0) == 1
    print("ok")
