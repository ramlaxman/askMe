#!/usr/bin/env python

# Explanation: we use list as the placeholder for the queue items, but
# removing and adding items done with methods we defined as part of the
# Queue class.


class Queue(object):
    """Queue implemention."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        return ' '.join(str(item) for item in self.items)

# Test Queue class!
# -----------------
queuey = Queue()
print("Queue is empty?: {}".format(queuey.isEmpty()))
queuey.enqueue(7)
queuey.enqueue(1)
queuey.enqueue(9)
print(queuey)
queuey.dequeue()
print(queuey)
print("Queue is empty?: {}".format(queuey.isEmpty()))
print("Queue size: {}".format(queuey.size()))
