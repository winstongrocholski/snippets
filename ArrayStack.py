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
        print('Added an item to the stack')

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



stack = ArrayStack()

print(f'The current size of the stack : {len(stack)}')
stack.push(3)
print(f'The current size of the stack : {len(stack)}')
stack.push(4)
print(f'The current size of the stack : {len(stack)}')
stack.push(5)
print(f'The current size of the stack : {len(stack)}')

print(f'The top value of the stack is : stack.top()')

print(f'Removed an item from the stack : {stack.pop()}')
print(f'Removed an item from the stack : {stack.pop()}')
print(f'Removed an item from the stack : {stack.pop()}')
