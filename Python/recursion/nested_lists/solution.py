#!/usr/bin/env python
import unittest


def get_items(li):
    """Return all the items of a given list."""
    for item in li:
        if type(item) is list:
            for sub_item in get_items(item):
                if sub_item is list:
                    get_items(sub_item)
                else:
                    yield sub_item
        else:
            yield item


class TestNestedLists(unittest.TestCase):

    def test_get_items(self):
        """Test get_items function."""
        list1 = [1, 2, [3, 4, 5], 6]
        list2 = [1, 2, [3, 4, [5, 6, 7]], 8]

        self.assertEqual(list(get_items(list1)), [1, 2, 3, 4, 5, 6])
        self.assertEqual(list(get_items(list2)), [1, 2, 3, 4, 5, 6, 7, 8])

if __name__ == '__main__':
    unittest.main()
