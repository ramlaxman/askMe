#!/usr/bin/env python
import collections


def are_permutations(str1, str2):
    """Returns True if the first given string is a permutation of the second

    given string.
    """
    perm = collections.defaultdict(int)
    for char in str1:
        perm[char] += 1
    for char in str2:
        perm[char] -= 1

    return not any(perm.itervalues())

# Test the function
# -----------------
print(are_permutations('Linux', 'unLix'))  # True
print(are_permutations('stamik', 'mastik'))  # True
print(are_permutations('yolo', 'not'))  # False

"""
Less effective solution O(n log(n)):

def are_permutations2(str1, str2):
    return (len(str1) == len(str2) and sorted(str1) == sorted(str2))
"""
