#!/usr/bin/env python
import collections
import os
import shutil
import tempfile
import unittest


def words_count(f):
    """Prints each word and the number of times it appers

    in the given file.
    """
    with open(f) as f:
        words_count = collections.Counter(f.read().split())

    for word, count in words_count.iteritems():
        print("{}: {}".format(word, count))

    return dict(words_count)


class TestWordsCount(unittest.TestCase):

    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp_dir)

    def test_words_count(self):
        with open(os.path.join(self.tmp_dir, 'wc'), 'w') as f:
            f.write("dog cat dog snake cat fish")
        wc = words_count(os.path.join(self.tmp_dir, 'wc'))
        self.assertEqual(wc, {'dog': 2, 'cat': 2, 'snake': 1, 'fish': 1})

if __name__ == '__main__':
    unittest.main()
