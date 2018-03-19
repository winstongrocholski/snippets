"""
Winston Grocholski
Date: 2018-03-09
From: codingbat.com

You are driving a little too fast, and a police officer stops you. Write code
to compute the result, encoded as an int value: 0=no ticket, 1=small ticket,
2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61
and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2.
Unless it is your birthday -- on that day, your speed can be 5 higher in all
cases.
"""

def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed = speed - 5
  if speed <= 60:
    return 0
  elif 61 < speed <= 80:
    return 1
  else:
    return 2

# test 1
result = caught_speeding(60, False)
print(f'Expected 0 recieved : {result}')

# test 2
result = caught_speeding(80, False)
print(f'Expected 1 recieved : {result}')

# test 3
result = caught_speeding(40, False)
print(f'Expected 0 recieved : {result}')

# test 4
result = caught_speeding(85, True)
print(f'Expected 1 recieved : {result}')
