class FIFO:
    def __init__(self):
        self.fifo = []

    def size(self):
        return len(self.fifo)

    def push(self, val):
        self.fifo.append(val)

    def get(self):
        if self.size() > 0:
            return self.fifo.pop(0)
        else:
            return 'the queue is empty'



fifo = FIFO()
fifo.push(1)
fifo.push(2)
fifo.push(3)
fifo.push(4)
fifo.push(5)

print(fifo.size())

fifo.get() #1
fifo.get() #2
fifo.get() #3
fifo.get() #4

print(fifo.size())

print(fifo.get()) #5

print(fifo.size())