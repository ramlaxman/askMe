#!/usr/bin/env python
import logging
import threading
import time


logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s')


class Printer(threading.Thread):
    """Represents a printer."""

    def __init__(self, name, queue, ppg):
        super(Printer, self).__init__()
        self.name = name
        self.queue = queue
        self.ppg = ppg
        self.busy = False

    def printTask(self):
        """Prints the latest task in queue."""
        item = self.queue.dequeue()
        logging.info("Printing %s pages", item.pages)
        time.sleep((item.pages / self.ppg) * 60)

    def run(self):
        """Runs the printer."""
        while True:
            if not self.queue.isEmpty() and not self.busy:
                self.busy = True
                self.printTask()
                logging.info("Print task complete.")
                self.busy = False


class PrinterQueue(object):
    """Represents a printer queue."""

    def __init__(self):
        self.items = []

    def submit_task(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []


class PrintTask(object):
    """Represents a print task."""

    def __init__(self, pages):
        self.pages = pages

if __name__ == '__main__':

    # Create printer queue
    pQueue = PrinterQueue()

    PAGES_PER_MINUTE = 10

    # Create and run printer
    p = Printer("Kimi", pQueue, PAGES_PER_MINUTE)
    p.start()

    # Add tasks
    task = PrintTask(10)
    pQueue.submit_task(task)
    logging.info("Added print task with %s pages", task.pages)

    task = PrintTask(30)
    pQueue.submit_task(task)
    logging.info("Added print task with %s pages", task.pages)

    task = PrintTask(1)
    pQueue.submit_task(task)
    logging.info("Added print task with %s pages", task.pages)
