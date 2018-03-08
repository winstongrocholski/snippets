"""Using the ArrayStack object to reverse data"""

from ArrayStack import ArrayStack

data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

stack = ArrayStack()
before = ''
after = ''

for num in data:
    before += str(num) + ','
    stack.push(num)

while not stack.is_empty():
    after += str(stack.pop()) + ','

print(before)
print(after)
