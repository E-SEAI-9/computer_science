# --- Step 1: Create a Tuple ---
# Tuples are ordered, unchangeable (immutable) collections defined using parentheses ()
my_tuple = ("apple", "banana", "cherry",  "orange", "strawberry")

# --- Step 2: Print the Tuple ---
print(my_tuple)

# --- Step 3: Access Tuple Items ---
# Indexing works exactly like lists, starting from 0 for the first item
print(my_tuple[0])   # First item
print(my_tuple[-1])  # Last item using negative indexing

# --- Step 4: Slice the Tuple ---
# Slicing returns a new tuple containing the requested range of elements
print(my_tuple[1:4])  # Middle items from index 1 up to (but excluding) 4
print(my_tuple[:3])   # Slicing from the start up to index 3
print(my_tuple[2:])   # Slicing from index 2 to the very end

# --- Step 5: Check if an Item Exists ---
# The 'in' operator checks for membership inside the tuple and returns a boolean
if "banana" in my_tuple:
    print("Banana was found in the tuple!")
else:
    print("Banana was not found.")

# --- Step 6: Count and Index ---
# .count() returns the total number of times a specific value appears
print(my_tuple.count("banana"))

# .index() returns the index position of the first occurrence of a specific value
print(my_tuple.index("banana"))

# --- Step 7: Packing and Unpacking ---
# Unpacking extracts tuple items directly into individual variables
# Standard unpacking: The number of variables must match the number of elements exactly
item1, item2, item3, item4, item5 = my_tuple
print(item1)
print(item3)

# Extended unpacking: Using the asterisk (*) to collect multiple remaining items into a list
first, *middle, last = my_tuple
print(first)   # Holds the first element
print(middle)  # Holds a list of all elements captured in between
print(last)    # Holds the last element

# --- Step 8: Joining Tuples ---
another_tuple = ("kiwi", "grape")

# Combining two tuples into a completely brand-new tuple using the '+' operator
combined_tuple = my_tuple + another_tuple
print(combined_tuple)

# Multiplying a tuple by an integer duplicates its structural contents that many times
repeated_tuple = another_tuple * 3
print(repeated_tuple)