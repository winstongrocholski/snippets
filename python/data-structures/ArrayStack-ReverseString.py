"""Using the ArrayStack object to reverse a string"""

from ArrayStack import ArrayStack

forward = "Never odd or even"
reverse = ""

stack = ArrayStack()

for char in forward:
    stack.push(char)

while not stack.is_empty():
    reverse += str(stack.pop())

print(forward)
print(reverse)
