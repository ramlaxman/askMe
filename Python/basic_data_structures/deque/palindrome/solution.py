#!/usr/bin/env python

from deque import Deque


def isPalindrome(string):
    """Given a string, return True if it's a palindrome

    or False if it's not.
    """
    palindrome = True
    deq = Deque()

    for char in "".join(string.split()):
        deq.addRear(char.lower())

    for i in xrange(deq.size() / 2):
        if deq.popRear() != deq.popFront():
            palindrome = False

    return palindrome


# Test the 'isPalindrome' function
# --------------------------------
print(isPalindrome('abba'))  # Should print True
print(isPalindrome('abcd'))  # Should print False
print(isPalindrome(
    'Are we not drawn onward to new era'))  # Should print True
