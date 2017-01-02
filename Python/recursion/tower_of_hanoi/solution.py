#!/usr/bin/env python

"""
For eaxmple, start and end phases for 3 disks:

Start: 3       End:       3
       2                  2
       1  _ _        _ _  1
"""


class Tower(object):
    """Represents a Hanoi tower."""

    def __init__(self, disks, uniqueID):
        self.disks = disks
        self.id = uniqueID


def moveDisk(srcRod, destRod):
    print("Moving disk")
    counter = 0
    srcItem = srcRod.disks[0]

    while srcItem == '|':
        counter += 1
        srcItem = srcRod.disks[counter]

    srcRod.disks[counter] = "|"

    counter = len(destRod.disks) - 1
    destItem = destRod.disks[counter]

    while destItem != '|':
        counter -= 1
        destItem = destRod.disks[counter]

    destRod.disks[counter] = srcItem


def moveTower(height, leftRod, rightRod, middleRod):
    if height >= 1:

        moveTower(height-1, leftRod, middleRod, rightRod)
        moveDisk(leftRod, rightRod)

        # Print towers
        sorted_towers = [leftRod, middleRod, rightRod]
        sorted_towers.sort(key=id)
        for l, m, r in zip(*[tower.disks for tower in sorted_towers]):
            print("{}       {}      {}".format(l, m, r))
        print("-------------------------")

        moveTower(height-1, middleRod, rightRod, leftRod)


def solveTowerOfHanoi(disksNum):
    """Solves Tower of Hanoi puzzle."""

    # Create towers/rods
    leftRod = Tower([i for i in xrange(disksNum)], 0)
    middleRod = Tower(['|' for i in xrange(disksNum)], 1)
    rightRod = Tower(['|' for i in xrange(disksNum)], 2)

    # Print them
    all_towers = [leftRod, middleRod, rightRod]
    all_towers.sort(key=id)
    for l, m, r in zip(*[tower.disks for tower in all_towers]):
        print("{}       {}      {}".format(l, m, r))
    print("-------------------------")

    # Stat moving towers
    moveTower(disksNum, leftRod, rightRod, middleRod)

# Test solveTowerOfHanoi
# ----------------------
solveTowerOfHanoi(5)
