"""Simple stack implemented with a python list"""

class ArrayStack:
    #LIFO Stack implementation using a Python list.
    def __init__(self):

        self.items = [] # empty list

    def __len__(self):

        return len(self.items) # return the size of the stack

    def is_empty(self):

        return len(self.items) == 0 # return true if the stack is empty

    def push(self, item):

        self.items.append(item) # add another item to the stack

    def pop(self):

        if self.is_empty():
            print("Stack is empty")
        else:
            return self.items.pop() # return the top item of the stack

    def top(self):

        if self.is_empty():
            print("Stack is empty")
        else:
            return self.items[-1]
