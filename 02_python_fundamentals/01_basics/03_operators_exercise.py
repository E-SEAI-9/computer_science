# --- Step 1: Arithmetic Operators ---
a = 15
b = 4

# Performing basic mathematical operations
print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division (always returns a float)
print(a // b)  # Floor Division (rounds down to the nearest lower whole number)
print(a % b)   # Modulus (returns the remainder of the division)
print(a ** b)  # Exponentiation (a raised to the power of b)

# --- Step 2: Assignment Operators ---
x = 10

# Modifying the value of x in-place and printing after each change
x += 5         # Equivalent to: x = x + 5
print(x)
x -= 3         # Equivalent to: x = x - 3
print(x)
x *= 2         # Equivalent to: x = x * 2
print(x)
x /= 4         # Equivalent to: x = x / 4 (converts x to a float)
print(x)

# --- Step 3: Comparison Operators ---
# Comparisons evaluate to a Boolean value (True or False)
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to

# --- Step 4: Logical Operators ---
is_python_fun = True
is_java_fun = False

# Combining boolean values using logical operators
print(is_python_fun and is_java_fun)  # True only if BOTH conditions are True
print(is_python_fun or is_java_fun)   # True if AT LEAST ONE condition is True
print(not is_python_fun)              # Reverses the boolean value (Negation)

# --- Step 5: Identity Operators ---
list1 = [1, 2, 3]
list2 = list1  # list2 references the exact same object in memory as list1

# 'is' checks if two variables point to the same memory object location
print(list1 is list2)
print(list1 is not list2)

list3 = [1, 2, 3] # Content is identical to list1, but it is a completely separate object in memory

# Notice the difference: 'is' evaluates object identity, whereas '==' evaluates object value equality
print(list1 is list3)      # False (different locations in memory)
print(list1 == list3)     # True (same values inside the lists)

# --- Step 6: Membership Operators ---
text = "Python programming is fun!"

# Checking for substrings inside a string sequence
print("Python" in text)
print("Java" not in text)

# --- Step 7: Bitwise Operators (Bonus) ---
# Re-assigning variables for bitwise operations (operating on binary representations)
a = 5  # Binary: 0101
b = 3  # Binary: 0011

print(a & b)   # Bitwise AND: Sets each bit to 1 if both bits are 1 (0001 -> 1)
print(a | b)   # Bitwise OR: Sets each bit to 1 if one of two bits is 1 (0111 -> 7)
print(a ^ b)   # Bitwise XOR: Sets each bit to 1 if only one of two bits is 1 (0110 -> 6)
print(a << 1)  # Bitwise Left Shift: Shifts bits left by 1 position (0101 becomes 1010 -> 10)
print(b >> 1)  # Bitwise Right Shift: Shifts bits right by 1 position (0011 becomes 0001 -> 1)

# --- Step 8: Operator Precedence ---
# Standard PEMDAS rules apply (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)
# Default precedence: ** runs first, then *, then +
expr_without_parentheses = 2 + 3 * 4 ** 2
print(expr_without_parentheses)  # Evaluates as: 2 + (3 * (4 ** 2)) -> 2 + (3 * 16) -> 2 + 48 = 50

# Using parentheses to alter normal operator precedence execution order
expr_with_parentheses = (2 + 3) * 4 ** 2
print(expr_with_parentheses)     # Evaluates as: (5) * 4 ** 2 -> 5 * 16 = 80