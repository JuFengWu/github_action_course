from my_main import add_func, minuse_func
import sys

def test_add():
    a = 3
    b = 4
    ideal_result = 7

    result = add_func(3,4)
    if ideal_result != result:
        sys.exit(1)

def test_minuse():
    a = 3
    b = 4
    ideal_result = -1

    result = minuse_func(3,4)
    if ideal_result != result:
        sys.exit(2)

if __name__ == "__main__":
    test_add()
    test_minuse()
