# reduce() = apply a function to an iterable and reduce it to a single cumulative value
# performs function on first two elements and repeats the process until 1 value remains
# reduce(function, iterable)

from functools import reduce

letters = ['H', 'e', 'l', 'l', 'o']
word = reduce(lambda x, y: x + y, letters)
print(word)

factorial = [5, 4, 3, 2, 1]
result = reduce(lambda x, y: x * y, factorial)
print(result)
