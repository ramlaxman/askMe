#!/usr/bin/env python


def has_unique_chars(string):
    """Returns True if a given string has only unique characters.

       Otherwise, returns false.
    """
    return len(set(string)) == len(string)


print("First function")
print(has_unique_chars("abcd"))         # True
print(has_unique_chars("ababababab"))   # False
print(has_unique_chars("asdlkew"))      # True
print(has_unique_chars("mario"))        # True
print(has_unique_chars("aa"))           # False


# Additional possible solution

def has_unique_chars2(string):

    unique_chars = set()

    for char in string:
        if char in unique_chars:
            return False
        unique_chars.add(char)
    return True

print("Seconf function")
print(has_unique_chars2("abcd"))         # True
print(has_unique_chars2("ababababab"))   # False
print(has_unique_chars2("asdlkew"))      # True
print(has_unique_chars2("mario"))        # True
print(has_unique_chars2("aa"))           # False
