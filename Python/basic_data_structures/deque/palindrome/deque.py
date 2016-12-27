#!/usr/bin/env python

class Deque(object):
    """Deque implemention."""

    def __init__(self):
        self.items = []

    def addRear(self, item):
        self.items.insert(0, item)

    def addFront(self, item):
        self.items.append(item)

    def popFront(self):
        return self.items.pop()

    def popRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        return ' '.join(str(item) for item in self.items)
