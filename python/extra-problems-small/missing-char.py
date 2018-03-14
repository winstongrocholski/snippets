"""
Winston Grocholski
Date: 2018-03-09
From: codingbat.com

Given a non-empty string and an int n, return a new string where the char
at index n has been removed. The value of n will be a valid index of a char
in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
"""


# solution 1
def missing_char_v1(str, n):
  first = ''
  count = 0
  for char in str:
    if count != n:
      first = first + char
    count += 1
  return first

# solution 2
def missing_char_v2(str, n):
  first = str[:n]
  last  = str[n+1:]
  return first+last

# test 1
result = missing_char_v1('kitten',1)
print(f'Expected ktten recieved : {result}')

# test 2
result = missing_char_v1('kitten',4)
print(f'Expected kittn recieved : {result}')

# test 3
result = missing_char_v1('hi',0)
print(f'Expected i recieved : {result}')
