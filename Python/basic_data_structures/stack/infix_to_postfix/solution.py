#!/usr/bin/env python

from stack import Stack

import string


def infix2postfix(infix):

    stacky = Stack()
    output = []

    level = {'*': 3,
             '/': 3,
             '+': 2,
             '-': 2,
             '(': 1 }

    for char in infix:
        if char in string.ascii_letters or char in string.digits:
            output.append(char)
        elif char == '(':
            stacky.push(char)
        elif char == ')':
            top = stacky.pop()
            while top != '(':
                output.append(top)
                top = stacky.pop()
        elif char in '+-/*':
            while (not stacky.isEmpty() and
                   level[stacky.top()] >= level[char]):
                output.append(stacky.pop())
            stacky.push(char)

    while not stacky.isEmpty():
        output.append(stacky.pop())
    return ' '.join(x for x in output)
        

# Test the function
# -----------------
print(infix2postfix("( A + B ) * ( C + D )"))  # Should print 'A B + C D + *'
print(infix2postfix("( A + B ) * C"))  # Should print 'A B + C *'
print(infix2postfix("A + B * C"))  # Should print 'A B C * +'
print(infix2postfix("( A + B ) * C - ( D - E ) * ( F + G )"))  # Should print 'A B + C * D E - F G + * -'
