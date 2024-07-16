def add(a:int, b:int):
    '''Function to add two numbers'''
    return a + b


def test_add_positive_integers():
    assert add(1,2) == 3

def test_add_zeros():
    assert add(0,0) == 0

def test_add_negative_integers():
    assert add(-5,-2) == -7

def test_wrong_test():
    assert add(2,3) == 6
