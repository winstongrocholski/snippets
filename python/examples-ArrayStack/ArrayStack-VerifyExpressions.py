"""Use ArrayStack to verify expressions"""

from ArrayStack import ArrayStack

expression = "(3+4) - 4 + 5 * (5-2)"

left = "{[("
right = '}])'

def check(expression):
    stack = ArrayStack()

    for delimeter in expression:
        if delimeter in left:
            stack.push(delimeter) # add delemeter to stack
        elif delimeter in right:
            if stack.is_empty():
                return False
            if left.index(stack.pop()) != right.index(delimeter):
                return False

    return stack.is_empty() # return true if all delimeters are matched

print(check(expression))
