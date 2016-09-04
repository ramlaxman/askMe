#!/usr/bin/env python

from stack import Stack

import string


def calculate(operator, num1, num2):
    """Calculates simple expressions."""

    if operator == '+':
        return num2 + num1
    if operator == '-':
        return num2 - num1
    if operator == '*':
        return num2 * num1
    if operator == '/':
        return num2 / num1


def eval_postfix(postfix):

    stacky = Stack()

    for char in postfix:
        if char in string.digits:
            stacky.push(char)
        elif char in '+-*/':
            result = calculate(char, int(stacky.pop()), int(stacky.pop()))
            stacky.push(result)
    
    return stacky.pop()

# Test the function
# -----------------
print(eval_postfix("1 2 3 * +"))      # Should print 7
print(eval_postfix("7 8 + 3 2 + /"))  # Should print 3
