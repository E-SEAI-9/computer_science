# --- Step 1: Create and Print a Dictionary ---
# Dictionaries store data in key-value pairs, defined using curly braces {}
person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
print(person)

# --- Step 2: Access Dictionary Elements ---
# Accessing a value using bracket notation (will raise a KeyError if the key does not exist)
print(person["name"])

# Safely retrieving a value using .get() with a fallback default value if the key is missing
print(person.get("email", "No email provided"))

# Extracting all keys, values, and key-value pairs (items) as special view objects
print(person.keys())
print(person.values())
print(person.items())

# --- Step 3: Check for Key Existence ---
# The 'in' keyword checks specifically for the presence of a key within the dictionary
if "age" in person:
    print("The key 'age' exists in the dictionary.")
else:
    print("The key 'age' was not found.")

# --- Step 4: Change and Update Dictionary Elements ---
# Directly updating an existing value by accessing its key
person["city"] = "Boston"

# Using .update() to modify existing pairs or add new ones simultaneously
person.update({"city": "Chicago", "occupation": "Engineer"})

# --- Step 5: Add New Items to the Dictionary ---
# Direct assignment adding a completely brand-new key-value pair
person["country"] = "USA"

# Using .update() to add another new key-value pair to the dictionary
person.update({"hobby": "cycling"})

# --- Step 6: Remove Items from the Dictionary ---
# .pop() removes the specified key and returns its associated value
removed_value = person.pop("occupation")
print(removed_value)

# .popitem() removes and returns the last inserted key-value pair as a (key, value) tuple
removed_pair = person.popitem()
print(removed_pair)

# The 'del' keyword permanently deletes a specific key-value pair from the dictionary
del person["age"]

# Demonstrating .clear() on a temporary copy so we do not wipe out our main dictionary for upcoming steps
temp_dict = person.copy()
temp_dict.clear()
print(temp_dict)  # Outputs an empty dictionary: {}

# --- Step 7: Copy a Dictionary ---
# Creating an independent shallow copy of the dictionary using the .copy() method
person_copy = person.copy()

# Modifying the original dictionary to verify that the copy remains completely isolated
person["name"] = "Jane Doe"
print(person)       # Shows modified name
print(person_copy)  # Shows original name intact

# --- Step 8: Using setdefault() ---
# .setdefault() returns the value if the key already exists (leaving the dictionary unchanged)
existing_val = person.setdefault("city", "Miami")
print(existing_val)

# If the key does NOT exist, .setdefault() inserts the key with the specified default value
new_val = person.setdefault("phone", "555-1234")
print(new_val)

# Printing the final dictionary to observe the newly structural added "phone" key
print(person)