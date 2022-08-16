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


# Хотя list объекты поддерживают аналогичные операции,
# они оптимизированы для быстрых операций с фиксированной длиной
# и несут затраты на перемещение памяти O(n) для pop(0)операций,
# которые изменяют как размер, так и положение базового представления данных