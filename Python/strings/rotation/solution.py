#!/usr/bin/env python


def is_rotation(str1, str2):
    """Returns True if the first given string is a rotation of the second

    given string.
    """
    return(len(str1) == len(str2) and str1 in str2*2)

# Test the function
# -----------------
print(is_rotation('nope', 'dont_think_so'))  # False
print(is_rotation('yes', 'sye'))  # True
print(is_rotation('yes', 'yesyes'))  # False
print(is_rotation('pizza', 'apizz'))  # True

"""
Additional solution without using 'in' or substring.

def is_rotation(str1, str2):
  if len(str1) != len(str2):
    return False

  for index in range(len(str1)):
    import pdb; pdb.set_trace()
    if str2.startswith(str1[index:]) and str2.endswith(str1[:index]):
      return True

  return False

# Test the function
# -----------------
print(is_rotation('nope', 'dont_think_so'))  # False
print(is_rotation('yes', 'sye'))  # True
print(is_rotation('yes', 'yesyes'))  # False
print(is_rotation('pizza', 'apizz'))  # True

"""
