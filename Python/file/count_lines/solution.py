#!/usr/bin/env python
import os
import shutil
import tempfile
import unittest


def count_lines(f):
    """Return number of lines in a given file."""
    return sum(1 for line in open(f))


class TestCountLines(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_count_lines(self):
        with open(os.path.join(self.temp_dir, 'cl'), 'w') as f:
            f.writelines("Hello\nIs it me\nYou looking fori\n")
        lines_num = count_lines(os.path.join(self.temp_dir, 'cl'))
        self.assertEqual(lines_num, 3)

if __name__ == '__main__':
    unittest.main()
