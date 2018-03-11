"""
Winston Grocholski
Date: 2018-03-10
From: www.practicepython.org

Write a program that asks the user how many Fibonnaci numbers to generate and
then generates them.

Method 1 fibonacci_from_user():
Will ask users how many numbers of the Fibonacci sequence they would like to
find and print them out

Method 2 fibonacci():
Used to calculate the amount of time required to fid all numbers in the
Fibonacci Sequence up to different values.
"""
import time

def fibonacci_from_user():
    num = int(input("How many numbers of the Fibonacci Sequence would you like to generate? "))
    sequence = calculate(num)
    print(output(sequence))

def fibonacci(num):
    start_time = time.time()
    calculate(num)
    print(f"Calc Fibonacci Sequence to {num} numbers took {(time.time() - start_time)} seconds.")

def calculate(num):
    result = [1,1]
    if num <= 0:
        return []
    if num == 1:
        return [1]
    if num == 2:
        return result
    if num > 2:
        for i in range(num - 2):
            # formula n = (n-2) + (n-1)
            result.append(result[i] + result[i+1])
        return result

def output(sequence):
    output = ''
    for value in sequence:
        output += str(value) + ','
    return output

fibonacci_from_user()
#fibonacci(10000)
#fibonacci(20000)
#fibonacci(30000)
#fibonacci(40000)
#fibonacci(50000)
#fibonacci(60000)
#fibonacci(70000)
#fibonacci(80000)
#fibonacci(90000)
#fibonacci(100000)
#fibonacci(200000)
#fibonacci(300000)

""" Results From My Computer
Calc Fibonacci Sequence to 10000 numbers took 0.007687091827392578 seconds.
Calc Fibonacci Sequence to 20000 numbers took 0.02330613136291504 seconds.
Calc Fibonacci Sequence to 30000 numbers took 0.050296783447265625 seconds.
Calc Fibonacci Sequence to 40000 numbers took 0.061985015869140625 seconds.
Calc Fibonacci Sequence to 50000 numbers took 0.08791327476501465 seconds.
Calc Fibonacci Sequence to 60000 numbers took 0.1072547435760498 seconds.
Calc Fibonacci Sequence to 70000 numbers took 0.14338183403015137 seconds.
Calc Fibonacci Sequence to 80000 numbers took 0.19408893585205078 seconds.
Calc Fibonacci Sequence to 90000 numbers took 0.2610149383544922 seconds.
Calc Fibonacci Sequence to 100000 numbers took 0.32678890228271484 seconds.
Calc Fibonacci Sequence to 200000 numbers took 1.4316699504852295 seconds.
Calc Fibonacci Sequence to 300000 numbers took 4.578339099884033 seconds.
"""
