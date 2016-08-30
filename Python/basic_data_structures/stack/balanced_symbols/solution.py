#!/usr/bin/env python

from stack import Stack


def check_balanced_symbols(sequence):

    stacky = Stack()

    brackets = {'{': '}',
                '(': ')',
                '[': ']'}

    if sequence:
        for char in sequence:
            if char in '({[':
                stacky.push(char)
            elif not stacky.isEmpty():
                bracket = stacky.pop()
                if brackets[bracket] != char:
                    return False
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
print(check_balanced_symbols("{[}]"))    # Should print False
print(check_balanced_symbols("{[)}"))    # Should print False
print(check_balanced_symbols("{[]}"))    # Should print True
print(check_balanced_symbols("{}[]()"))  # Should print True
print(check_balanced_symbols(""))        # Should print weird message
