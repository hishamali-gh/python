# REVERSE THE STRING
""" def reverse_a_string(txt):
    print(txt[::-1])

reverse_a_string('hisham') """

# IS PALINDROME?
""" def is_palindrome(txt):
    return txt[::-1] == txt

print(is_palindrome('malayalam'))
print(is_palindrome('english')) """

# THE LARGEST
""" ''' def find_the_largest(nums):
    return sorted(nums)[-1]

print(find_the_largest([8, 7, 6, 5, 4])) '''

''' def find_the_largest(n1, n2, n3):
    return max(n1, n2, n3)

print(find_the_largest(5, 3, 8)) '''

def find_the_largest(n1, n2, n3):
    largest = n1

    for x in [n2, n3]:
        largest = x if x > largest else largest

    return largest

print(find_the_largest(5, 10, 9)) """

# SWAP TWO VARIABLES W/O USING A THIRD VARIABLE:
""" a = 1
b = 2

print(a, b)

def swap(a, b):
    a, b = b, a

    return a, b

print(swap(a, b)) """

# VOWELS COUNT
""" def count_the_vowels(txt):
    count = 0

    for c in txt:
        if c in 'aeiou':
            count += 1

    return count

print(count_the_vowels('hisham'))
print(count_the_vowels('aeiou')) """

# CONSONANTS COUNT
""" def count_the_consonants(txt):
    count = 0

    for c in txt:
        if c not in 'aeiou':
            count += 1

    return count

print(count_the_consonants('hisham'))
print(count_the_consonants('aeiou')) """

# FACTORIAL USING RECURSION
""" def fact(n):
    if n <= 1:
        return 1

    return fact(n - 1) * n

print(fact(0))
print(fact(1))
print(fact(2))
print(fact(3))
print(fact(4))
print(fact(5)) """

# FACTORIAL USING ITERATION
""" class FactIterator:
    def __init__(self, n):
        self.n = n
        self.res = 1
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr <= self.n:
            self.res *= self.curr
            self.curr += 1

            return self.res

        else:
            raise StopIteration

f = FactIterator(5)

for n in f:
    print(n) """

# FIB USING ITERATION
""" class FibIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.n:
            raise StopIteration

        val = self.prev

        self.prev, self.curr = self.curr, self.prev + self.curr

        self.count +=1 

        return val        

f = FibIterator(5)

for n in f:
    print(n) """

# NORMAL DECORATORS
''' def log(fn):
    def wrapper(*args, **kwargs):
        print(f'Calling <{fn.__name__}>')

        val = fn(*args, **kwargs)

        print(f'Finished <{fn.__name__}>')

        return val

    return wrapper

@log
def greet(name):
    print(f'Hello {name}')

greet('Alice')
print()

@log
def multiply(a, b):
    return a * b

result = multiply(5, 6)

print(result) '''

''' import time

def timer(fn):
    def wrapper(*args, **kwargs):
        start = time.time()

        try:
            return fn(*args, **kwargs)

        finally:
            end = time.time() - start

            print(f'Work took {end:.6f} seconds')

    return wrapper

@timer
def divide(a, b):
    return a / b

result = divide(10, 0)

print(result) '''

def repeater(n):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                fn(*args, **kwargs)

        return wrapper

    return decorator

troi = repeater(3)
cinq = repeater(5)

@cinq
def greet(name):
    print(f'Hi, {name}')

greet('Hisham')
