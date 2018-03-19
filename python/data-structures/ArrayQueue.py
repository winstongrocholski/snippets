"""Simple queue implemented with an array"""

class ArrayQueue:

    MAX_QUEUE_SIZE = 2

    def __init__(self):

        self.data = [None] * ArrayQueue.MAX_QUEUE_SIZE
        self.index = 0
        self.size = 0

    def __len__(self):

        return self.size

    def is_empty(self):

        return self.size == 0

    def peak(self):

        if self.is_empty():
            return "Queue is empty"
        else:
            return self.data[self.index]

    def push(self, item):

        if self.size == len(self.data):
            self.resize_data(self.size * 2)
        pos = (self.index + self.size) % len(self.data)
        self.data[pos] = item
        self.size += 1

    def pop(self):

        if self.is_empty():
            return "Queue is empty"
        item = self.data[self.index]
        self.data[self.index] = None
        self.index = (self.index + 1) % len(self.data)
        self.size -= 1
        return item

    def resize_data(self, new_size):

        old_data = self.data
        self.data = [None] * new_size
        for i in range(self.size):
            self.data[i] = old_data[self.index]
            self.index = (self.index + 1) % len(old_data)
        self.index = 0
        print(f'Queue resized to {new_size}')

queue = ArrayQueue()

data = {1,2,3,4,5,6,7,8,9,10,11}
for item in data:
    queue.push(item)

for i in range(len(data)+3):
    print(queue.pop())
