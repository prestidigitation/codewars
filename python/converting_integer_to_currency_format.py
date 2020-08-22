# Write a function that takes an integer in input and outputs a string with currency format.
# Integer in currency format is expressed by a string of number where every three characters are separated by comma.
# For example:
# 123456 --> "123,456"
# Input will always be an positive integer, so don't worry about type checking or negative/float values.Naive

# naive implementation
def to_currency(price):
    nums = str(price)
    new_string = ''
    for i, num in enumerate(nums):
        if (len(nums) - i) % 3 == 0 and i != 0:
            new_string += ','
        new_string += num
    return new_string

# using hard-to-read list comprehension
def to_currency_ugly_one_liner(price):
    return ''.join([',' + num if (len(str(price)) - i) % 3 == 0 and i != 0 else num for i, num in enumerate(str(price))])

# using thousands separator from format specification mini-language. Enlightened!
def to_currency_f_string(price):
    return f"{price:,}"
