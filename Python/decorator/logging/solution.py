#!/usr/bin/env python
from StringIO import StringIO
import sys
import unittest

GIVEN_ARGS = "Given args: {}"
RESULT = "Result is: {}"


def logging(f):

    def inner(*args, **kwargs):
        result = f(*args, **kwargs)
        print(GIVEN_ARGS.format(args))
        print(RESULT.format(result))
        return result

    return inner


@logging
def sum(*args):
    result = 0
    for num in args:
        result += num
    return result


class TestLogging(unittest.TestCase):
    """Test logging function."""

    def test_logging(self):
        output_f = StringIO()
        sys.stdout = output_f
        sum(2, 3, 4)
        args, result = output_f.getvalue().strip().splitlines()
        self.assertEqual(args, GIVEN_ARGS.format("(2, 3, 4)"))
        self.assertEqual(result, RESULT.format("9"))

if __name__ == '__main__':
    unittest.main()
