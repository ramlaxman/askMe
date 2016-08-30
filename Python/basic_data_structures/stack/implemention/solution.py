#!/usr/bin/env python

# Explanation: we use list as the placeholder for the stack items, but
# removing and adding items done with methods we defined as part of the
# Stack class.

# Stack: [3, 5, 16] -> 16 is at top, first item.

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

    def __str__(self):
        items = "Stack:\n" + '\n'.join(str(item) for item in self.items[::-1])
        return items

# Test Stack class!

stacky = Stack()
print "Stack is empty?: {}".format(stacky.isEmpty())
stacky.push(3)
stacky.push(5)
stacky.push(16)
print stacky
stacky.pop()
print stacky
print "Stack is empty?: {}".format(stacky.isEmpty())
print "Stack size: {}".format(stacky.size())
