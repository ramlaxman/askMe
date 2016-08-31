#!/usr/bin/env python

from stack import Stack


def decimalToBinary(decimal):

    stacky = Stack()

    while decimal != 0:
        stacky.push(decimal % 2)
        decimal = decimal/2

    return '0'*(8 - stacky.size()) + ''.join(str(num) for num in stacky.items)

# Test the function
# -----------------
print(decimalToBinary(31))  # Should print 00011111
print(decimalToBinary(255))  # Should print 11111111
print(decimalToBinary(15))  # Should print 00001111
