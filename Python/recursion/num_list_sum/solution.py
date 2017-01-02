#!/usr/bin/env python


def numListSum(numList):
    """Given a list of numbers, returns the sum of the numbers."""
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + numListSum(numList[1:])

# Test numListSum
# ---------------
print(numListSum([1, 2, 3]))  # 6
print(numListSum([0, 1, 0]))  # 1
print(numListSum([0, 5, 5, 5, 5, 5, 5]))  # 30
