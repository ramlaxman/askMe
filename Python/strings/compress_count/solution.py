#!/usr/bin/env python
from __future__ import print_function
import collections
import unittest


def compress(string):
    """Returns compressed string of the given string

       if the compressed version is shorter
    """
    comp_dict = collections.Counter(string)
    # Convert to sorted list since Counter may return it unsorted (e.g a,c,b)
    comp_list = sorted(comp_dict.items())
    compressed = "".join("%s%s" % (i[0], i[1]) for i in comp_list)
    if len(compressed) < len(string):
        return compressed
    else:
        return string


"""
# Additional version, without the magic of using collections.

def compress(string):
    i = 0
    count = 1
    compressed = ""

    while i < len(string)-1:
        if string[i] != string[i+1]:
            compressed += string[i] + str(count)
            count = 1
        else:
            count += 1
        i += 1

    compressed += string[i] + str(count)
    if len(compressed) < len(string):
        return compressed
    else:
        return string
"""

class TestCompressString(unittest.TestCase):

    def test_compressed(self):
        # Compressed result
        compressed = compress("aaaabbbcccc")
        self.assertEqual(compressed, "a4b3c4")

    def test_uncompressed(self):
        # Original string result
        uncompressed = compress("aabbcc")
        self.assertEqual(uncompressed, "aabbcc")

if __name__ == '__main__':
    unittest.main()
