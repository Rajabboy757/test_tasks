from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)


fifo = Queue()
fifo.enqueue(1)
fifo.enqueue(2)
fifo.enqueue(3)
fifo.enqueue(4)
fifo.enqueue(5)

print(fifo.size())

fifo.dequeue() #1
fifo.dequeue() #2
fifo.dequeue() #3
fifo.dequeue() #4

print(fifo.size())

print(fifo.dequeue()) #5

print(fifo.size())