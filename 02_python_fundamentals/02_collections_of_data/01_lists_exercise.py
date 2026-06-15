# --- Step 1: Create and Print a List ---
# Creating a list containing 5 string items
fruits = ["apple", "banana", "cherry", "orange", "strawberry"]
print(fruits)

# --- Step 2: Access Elements by Index and Negative Index ---
# Positive tracking starts at 0; negative tracking starts from the end at -1
print(fruits[0])   # First item
print(fruits[-1])  # Last item
print(fruits[-2])  # Second to last item

# --- Step 3: Slice a List ---
# Slicing syntax: list[start:end] (the end index is non-inclusive)
print(fruits[1:4])  # Elements from index 1 up to (but not including) index 4
print(fruits[:2])   # Everything from the start up to index 2
print(fruits[2:])   # Everything from index 2 down to the end of the list

# --- Step 4: Check if an Item Exists ---
# The 'in' keyword returns a boolean value (True/False) used for conditional statements
if "apple" in fruits:
    print("Apple is in the list!")
else:
    print("Apple was not found.")

# --- Step 5: Add Items ---
# .append() adds an item directly to the very end of the list
fruits.append("watermelon")
print(fruits)

# .insert() adds an item at a specific index position, shifting later elements right
fruits.insert(2, "grape")
print(fruits)

# --- Step 6: Change Items ---
# Modifying a single value via explicit index assignment
fruits[0] = "mango"
print(fruits)

# Replacing a chunk of elements simultaneously by assigning values to a slice
fruits[1:3] = ["blueberry", "coconut"]
print(fruits)

# --- Step 7: Remove Items ---
# .remove() finds and deletes the first matching instance of a specific value
fruits.remove("coconut")
print(fruits)

# .pop() removes and returns an item at a specified index (defaults to the last item if left empty)
popped_fruit = fruits.pop(3)
print(popped_fruit)
print(fruits)

# Demonstrating .clear() using a temporary list copy so we do not wipe out our primary list
temp_list = fruits.copy()
temp_list.clear()
print(temp_list)  # Outputs an empty list: []

# --- Step 8: Copy a List ---
# Creating an independent shallow copy of the list using the .copy() method
fruits_copy = fruits.copy()

# Alternatively, you can copy using a full slice: fruits_copy = fruits[:]

# Modifying the original list to prove that the copy remains completely separate and unaffected
fruits.append("kiwi")
print(fruits)       # Shows original list containing "kiwi"
print(fruits_copy)  # Shows copy without "kiwi"

# --- Step 9: Concatenate and Extend ---
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# Method 1: The '+' operator combines lists into a completely brand-new list object
combined_list = list_a + list_b
print(combined_list)

# Method 2: .extend() modifies the target list in-place by appending items from another collection
list_a.extend(list_b)
print(list_a)

# --- Step 10: Sort and Reverse ---
# Using the built-in sorted() function to get a new sorted list without changing the original structure
new_sorted_list = sorted(fruits)
print(new_sorted_list)
print(fruits)

# .sort() rearranges the list elements strictly in-place (mutates the original list structure)
fruits.sort()
print(fruits)

# .reverse() flips the order of elements within the list in-place
fruits.reverse()
print(fruits)

# --- Step 11: Count and Index ---
# .count() calculates how many times a given element appears in the sequence
print(fruits.count("blueberry"))

# .index() returns the first index position where a specified element is located
print(fruits.index("blueberry"))

# --- Step 12: List Comprehension (Bonus) ---
# List comprehensions provide a concise syntax to build new lists based on existing iterables
# Syntax structure: [expression for item in iterable if condition]
uppercase_fruits = [fruit.upper() for fruit in fruits if "a" in fruit.lower()]
print(uppercase_fruits)