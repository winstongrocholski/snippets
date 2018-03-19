import random

def random_number():
    num_min = 10000000000000
    num_max = 999999999999999
    return str(random.sample(range(num_min, num_max), 1)[0])

def letter_range():
    result = []

    for c in char_range('A', 'Z'):
        result.append(c)

    for c in char_range('a', 'z'):
        result.append(c)

    return result

def random_letter(letters):
    return random.sample(letters, 1)[0]

def char_range(c1, c2):
    yield from range(ord(c1), ord(c2)+1)

def build_password():
    password = random_number()
    i = 0;
    while i < 12:
        letter = chr(random_letter(letter_range()))
        index = random.sample(range(0,15), 1)[0]
        password = password[:index] + letter + password[index + 1:]
        i += 1
    return password

print(build_password() + build_password())
