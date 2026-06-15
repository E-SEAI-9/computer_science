# --- Step 1: Create Strings ---
first_name = "Alice"
last_name = "Smith"

# A multi-line string uses triple quotes.
# Added extra spaces and the word "Python" to satisfy later instructions.
bio = "   I am learning Python for web development. It is a highly popular language.   "

# --- Step 2: Access Characters and Slice Strings ---
# Strings are zero-indexed. Index -1 safely grabs the very last character.
print(first_name[0])
print(last_name[-1])

# Slicing extracts a portion: bio[:10] gets characters from index 0 up to (but not including) 10.
print(bio[:10])

# --- Step 3: Loop Through a String ---
# Strings are iterable, allowing us to loop through each character individually.
for char in first_name:
    print(char)

# --- Step 4: String Length ---
# The len() function returns the total number of characters, including spaces.
print(len(bio))

# --- Step 5: Check Substrings ---
# Using the 'in' and 'not in' membership operators to verify content (returns True/False).
print("Python" in bio)
print("Java" not in bio)

# --- Step 6: Modify Strings ---
# String methods return new values; they do not mutate the original string.
print(first_name.upper())
print(last_name.lower())

# .strip() removes leading/trailing whitespace, .replace() swaps target substrings.
# Method chaining lets you call multiple methods on the same string in one line.
modified_bio = bio.strip().replace("Python", "coding")
print(modified_bio)

# .split() breaks a string into a list of substrings based on a delimiter (default is whitespace).
print(bio.split())

# --- Step 7: Concatenate Strings ---
# Combining strings together using the + operator, adding a literal space string in between.
full_name = first_name + " " + last_name
print(full_name)

# --- Step 8: String Formatting ---
# Approach 1: F-strings (Modern and preferred syntax, prefix with 'f')
print(f"Hello, my name is {full_name} and I love Python!")

# Approach 2: The .format() method (Older syntax using {} placeholders)
age = 25
print("My full name is {} and I am {} years old.".format(full_name, age))

# --- Step 9: Escape Characters ---
# Escape sequences like \' or \" allow quotes inside matching quote marks.
# Alternatively, use single quotes on the outside and double quotes inside (or vice versa).
quote_string = "He said, \"Python's great!\""
print(quote_string)

# --- Step 10: Bonus ---
# .center(width) pads the string with spaces on both sides to align it in the middle.
print(bio.center(50))

# .count(substring) counts the non-overlapping occurrences of a character/substring.
print(full_name.count("a"))