#!/usr/bin/env python


class Stack(object):
    """Stack implemention."""

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[-1]

    def __str__(self):
        items = "Stack:\n" + '\n'.join(str(item) for item in self.items[::-1])
        return items
