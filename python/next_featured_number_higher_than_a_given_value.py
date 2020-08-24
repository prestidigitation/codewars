# Make a function that receives a value, val and outputs the smallest higher number than the given value, and this number belong to a set of positive integers that have the following properties:
# * their digits occur only once
# * they are odd
# * they are multiple of three


# naive solution
from collections import Counter


def has_unique_digits(num):
    for value in Counter(str(num)).values():
        if value > 1:
            return False
    return True

def is_odd(num):
    return num % 2 != 0

def is_multiple_of_three(num):
    return num % 3 == 0

def next_numb(num):
    while num < 9999999999:
        num += 1
        if has_unique_digits(num) and is_odd(num) and is_multiple_of_three(num):
            return num
    return "There is no possible number that fulfills those requirements"
