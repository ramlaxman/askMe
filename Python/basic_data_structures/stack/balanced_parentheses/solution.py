#!/usr/bin/env python

from stack import Stack


def check_balanced_parentheses(sequence):

    stacky = Stack()

    if sequence:
        for char in sequence:
            if char == '(':
                stacky.push(char)
            elif not stacky.isEmpty():
                stacky.pop()
            else:
                return False
        if stacky.isEmpty():
            return True
        else:
            return False
    else:
        print("Seriosly? Empty string?")
        return False


# Test the function
print(check_balanced_parentheses("(())))"))  # Should print False
print(check_balanced_parentheses(")("))      # Should print False
print(check_balanced_parentheses("()"))      # Should print True
print(check_balanced_parentheses("((()))"))  # Should print True
print(check_balanced_parentheses(""))        # Should print weird message
