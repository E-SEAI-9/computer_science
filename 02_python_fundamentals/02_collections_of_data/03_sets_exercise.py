# --- Step 1: Create a Set ---
# Sets are unordered, unindexed collections that strictly contain unique values
fruits = {"apple", "banana", "cherry", "orange", "strawberry"}
print(fruits)

# --- Step 2: Check Membership ---
# The 'in' operator performs high-efficiency membership checks on sets
if "apple" in fruits:
    print("Apple is in the set!")
else:
    print("Apple is not in the set.")

# --- Step 3: Add and Update Items ---
# .add() appends a single unique element to the set
fruits.add("coconut")
print(fruits)

# Defining an entirely separate set of fruits
more_fruits = {"grape", "kiwi", "lemon"}

# .update() merges elements from another collection (or any iterable) into the current set
fruits.update(more_fruits)
print(fruits)

# --- Step 4: Remove Items ---
# .remove() deletes a specific element. Raises a KeyError if the element does not exist.
fruits.remove("banana")
print(fruits)

# .discard() deletes a specific element but safely. Does NOT raise an error if the element is missing
fruits.discard("watermelon")

# .pop() removes and returns an arbitrary element because sets do not maintain an index order
popped_fruit = fruits.pop()
print(popped_fruit)
print(fruits)

# .clear() removes all elements, leaving an empty set
fruits_copy = fruits.copy()
fruits_copy.clear()
print(fruits_copy)  # Outputs: set() - which represents an empty set in Python

# --- Step 5: Set Operations ---
set_a = {"apple", "banana", "cherry"}
set_b = {"cherry", "date", "elderberry"}

# .union() returns a new set containing all distinct items from both sets
print(set_a.union(set_b))

# .intersection() returns a new set containing only items present in both sets
print(set_a.intersection(set_b))

# .difference() returns a new set containing items in set_a that are NOT in set_b
print(set_a.difference(set_b))

# .symmetric_difference() returns a new set containing items unique to each set (excluding common items)
print(set_a.symmetric_difference(set_b))

# --- Step 6: In-place Set Operations ---
# In-place operations modify the target set directly instead of returning a new one
demo_set = set_a.copy()

# Removes items from demo_set that are also in set_b
demo_set.difference_update(set_b)
print(demo_set)

# Resetting demo_set to keep only the items common to both sets
demo_set = set_a.copy()
demo_set.intersection_update(set_b)
print(demo_set)

# Resetting demo_set to pull in all unique items from set_b
demo_set = set_a.copy()
demo_set.update(set_b)
print(demo_set)

# --- Step 7: Relational Methods ---
small_set = {"apple", "banana"}
large_set = {"apple", "banana", "cherry", "date"}

# .issubset() evaluates if every element of small_set exists inside large_set
print(small_set.issubset(large_set))

# .issuperset() evaluates if large_set contains every element found within small_set
print(large_set.issuperset(small_set))

# .isdisjoint() evaluates if two sets share absolutely zero common elements
set_c = {"kiwi", "mango"}
print(small_set.isdisjoint(set_c))