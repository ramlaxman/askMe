#!/usr/bin/env python

def duplicated_chars(string):

    duplicated = []
    seen = []

    for char in string:
        if char in seen:
            duplicated.append(char)
        else:
            seen.append(char)

    return ' '.join(str(ch) for ch in duplicated)


# Test the function
# -----------------
print duplicated_chars("hello")
print duplicated_chars("character")
