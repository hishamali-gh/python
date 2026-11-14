# OBJECT MEMORY MODEL
""" In languages like C or Java, simple numbers are 'primitives'—just raw binary values stored directly in a variable's memory slot.
Python does not have raw primitives. In Python:
    - Every number, word, function, and class is a "full-fledged object".
    - Variables are not boxes that hold data; they are name tags (pointers) attached to objects. """

# INTERNING
""" x = 43

print(x)

a = 'python'
b = 'python'

print(a == b)
print(a is b) # Wtf!! """

""" a = -6
b = int("-6")

print(a == b)
print(a is b) """

# __dict__
# By default, every instance of a custom class in Python stores its attributes inside a hidden dictionary called '__dict__'.

""" class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)

print(p.__dict__) # {'x': 1, 'y': 2} """
