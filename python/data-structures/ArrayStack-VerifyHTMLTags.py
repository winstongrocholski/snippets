"""Use ArrayStack to verify html opening and closing tags are all matched"""

from ArrayStack import ArrayStack

raw_html = "<body><h1>Hello World!</h1><p><b>Check</b> html code</p></body>"

def checkHTML(raw_html):

    stack = ArrayStack()
    i = raw_html.find('<')              # will return -1 if nothing found
    while i != -1:
        j = raw_html.find('>', i+1)     # find the index of the '>'
        if j == -1:
            return False
        tag = raw_html[i+1:j]           # get the tag name ex: <body> --> body
        if not tag.startswith('/'):
            stack.push(tag)             # push opening tag onto stack
        else:
            if stack.is_empty():        # check if stack is empty
                return False
            if tag[1:] != stack.pop():  # check tag with tag on stack
                return False
        i = raw_html.find('<', j+1)     # find the index of the next tag
    return stack.is_empty()

print(checkHTML(raw_html))
