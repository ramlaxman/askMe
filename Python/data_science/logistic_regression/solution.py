#!/usr/bin/env python

import numpy
import pylab

DELIMITER = ','

# Load the data
data = numpy.loadtxt('data.txt', delimiter=',')

print data

X = data[:, 0:2]
y = data[:, 2]

pos = numpy.where(y == 1)
neg = numpy.where(y == 0)

pylab.scatter(X[pos, 0], X[pos, 1], marker='o', c='b')
pylab.scatter(X[neg, 0], X[neg, 1], marker='x', c='r')

# Add titles
pylab.xlabel('Factor 1')
pylab.ylabel('Factor 2')

# Add legend
pylab.legend(['Admitted', 'Admitted'])

# Display
pylab.show()
