#!/usr/bin/env python
import time


def timeit(f):
    """Measure time execution of the given function."""

    def inner(*args, **kwargs):
        before = time.time()
        result = f(*args, **kwargs)
        after = time.time()
        print("It took %s to run the method %s" % (
            str(after - before), f.__name__))
        return result

    return inner


@timeit
def test_me(a, b):
    return a + b

# Test timeit decorator
test_me(2, 3)
test_me(5, 6)
