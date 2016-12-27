#!/usr/bin/env python

import datetime
import logging
import Queue
import random
import threading
import time

QUEUE_SIZE = 20
queue = Queue.Queue(QUEUE_SIZE)

logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s')


class Producer(threading.Thread):
    """Represenets a producer thread."""

    def __init__(self):
        super(Producer, self).__init__()

    def run(self):
        """Run producer thread."""
        while True:
            if not queue.full():
                item = datetime.datetime.now()
                queue.put(item)
                logging.info("Put item: %s in the queue", str(item))
                time.sleep(random.random())


class Consumer(threading.Thread):
    """Represenets a consumer thread."""

    def __init__(self):
        super(Consumer, self).__init__()

    def run(self):
        """Run consumer thread."""
        while True:
            if not queue.empty():
                item = queue.get()
                logging.info("Got item: %s from the queue", str(item))
                time.sleep(random.random())


if __name__ == '__main__':

    producer = Producer()
    consumer = Consumer()

    producer.start()
    logging.info("Started producer thread.")
    time.sleep(5)
    consumer.start()
    logging.info("Started consumer thread.")
