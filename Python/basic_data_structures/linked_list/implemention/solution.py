#!/usr/bin/env python


class Node(object):
    """Represenets a node in a linked list."""

    def __init__(self, data):
        self._data = data
        self._nextNode = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def nextNode(self):
        return self._nextNode

    @nextNode.setter
    def nextNode(self, node):
        self._nextNode = node


class LinkedList(object):
    """Represenets a linked list."""

    def __init__(self):
        self.head = None

    def add(self, node):
        temp = self.head
        self.head = node
        self.head.nextNode = temp

    def isEmpty(self):
        """Returns True if the linked list is empty.

        Otherwise, returns False
        """
        return self.head is None

    def size(self):
        """Returns the size of the linked list.

        The size is the number of nodes.
        """
        counter = 0
        curr = self.head

        while curr is not None:
            counter += 1
            curr = curr.nextNode

        return counter

    def remove(self, data):
        """Given data, removes the first found node with

        that matches the data.
        """
        pre = None
        curr = self.head
        found = False

        while not found:
            if curr.data == data:
                found = True
            else:
                pre = curr
                curr = curr.nextNode

        if pre:
            pre.nextNode = curr.nextNode
        else:
            self.head = curr.nextNode

    def __str__(self):

        nodes = []
        curr = self.head
        while curr is not None:
            nodes.append(str(curr.data))
            curr = curr.nextNode

        return " ".join(nodes)


# Test Node Class
# ---------------
n = Node(32)
print(n.data)  # Should print 32
n.data = 25
print(n.data)  # Should print 25

# Test LinkedList Class
# ---------------------
l = LinkedList()
print(l.isEmpty())  # True
l.add(Node(2))
l.add(Node(5))
print(l)  # 5 2
print(l.size())  # 2
l.add(Node(10))
l.remove(5)
print(l)  # 10 2
