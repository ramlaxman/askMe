#!/usr/bin/env python

# Explanation: we use list as the placeholder for the deque items, but
# removing and adding items done with methods we defined as part of the
# Deque class.


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

# Test Deque class!
# -----------------
dequeTest = Deque()
print("Deque is empty?: {}".format(dequeTest.isEmpty())) # Should print True
dequeTest.addFront(7)
dequeTest.addFront(1)
dequeTest.addRear(9)
print(dequeTest) # should be 9 7 1
dequeTest.popRear()
print(dequeTest) # should be 7 1
dequeTest.addFront(2)
dequeTest.popFront()
print(dequeTest) # should be 7 1
print("Queue is empty?: {}".format(dequeTest.isEmpty())) # Should print False
print("Queue size: {}".format(dequeTest.size()))
