#!/usr/bin/env python

from queue import Queue


def hot_potato(players, num):

    circle = Queue()

    for player in players:
        circle.enqueue(player)

    while circle.size() > 1:
        for i in xrange(num):
            circle.enqueue(circle.dequeue())

        circle.dequeue()

    return circle.dequeue()


# Test the program
# -----------------
print(hot_potato(["Mario", "Luigi", "Peach", "Bowser", "Shy Guy","Yoshi", "Toad"], 7)) # Should print 'Bowser'
print(hot_potato(["Blue", "Red", "Black", "Pink", "Orange","White"], 7)) # Should print 'Black'
