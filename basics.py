# Variables
#
print('Basic Variables')
x, y = 1, 2

print(f"x {x} y: {y}")
print(type(x))

# Type
print(type(1.1))
print(type(True))

# Type Annotations
#
# age: int = 43
print(f"Age is {age}")

# if you switch linter to mypy the following
# line will be flagged.
age = "Hello"

# Immutable and mutable Variables
#
print('Immutable and mutable Variables')
# Memory location of a variable

x = 22
print(id(x))

x = 44
print(id(x))


# Lists are mutable
x = [1, 2, 3]
print(id(x))
x.append(4)

print(x)
print(id(x))


print('Strings')
