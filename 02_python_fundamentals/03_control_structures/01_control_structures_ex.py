# --- Step 1: Basic If Condition ---
# Checking if a number is positive, negative, or zero using if-elif-else execution flow
num = 10

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# --- Step 2: Grade Calculator ---
# Evaluating conditions sequentially; once a condition is True, subsequent blocks are skipped
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# --- Step 3: Ternary Operator Practice ---
# Shortened inline if-else syntax in Python: variable = value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"
print(status)

# --- Step 4: For Loop over a List ---
# Iterating directly through sequential items within a list container
vehicles = ["car", "motorcycle", "truck", "bicycle"]
for vehicle in vehicles:
    print(f"Vehicle type: {vehicle}")

# --- Step 5: For Loop with Conditions ---
# Using the continue keyword to skip the remainder of the current loop iteration
for i in range(1, 11):
    if i % 2 != 0:
        continue  # Skips odd numbers, moving instantly to the next iteration loop step
    print(i)

# --- Step 6: While Loop Summation ---
# A while loop repeats as long as its conditional evaluation remains True
total_sum = 0
current_num = 1

while current_num <= 100:
    total_sum += current_num
    current_num += 1  # Crucial update step to avoid creating an infinite loop

print(total_sum)

# --- Step 7: Break out of a Loop ---
# Using the break keyword to exit the entire loop structure prematurely
words = ["apple", "pear", "banana", "kiwi", "grapefruit"]
for word in words:
    if len(word) > 5:
        print(word)
        break  # Immediately exits the for loop when a word exceeding 5 letters is reached

# --- Step 8: Nested Loops ---
# A loop within a loop: the inner loop completes fully for every single iteration of the outer loop
people = ["Alice", "Bob", "Charlie"]
pets = ["dog", "cat"]

for person in people:
    for pet in pets:
        print(f"{person} and their potential pet: {pet}")

# --- Step 9: Loop with Else Clause ---
# Python loops have a unique 'else' clause that executes ONLY if the loop finishes normally without hitting a 'break'
items = ["book", "pen", "pencil"]
search_target = "notebook"

for item in items:
    if item == search_target:
        print("Item found!")
        break
else:
    print("The value was not found.")

# --- Step 10: Pass Statement Usage ---
# The pass statement serves as a non-operational syntax placeholder where code block structure is required
unprocessed_items = [10, 20, 30]
for item in unprocessed_items:
    pass  # Used to avoid structural indentation errors before logic is written

# --- Step 11: Pattern Matching ---
# Initializing categorized collections
fruits = ["apple", "banana", "orange"]
veggies = ["carrot", "broccoli", "spinach"]
meat = ["beef", "chicken", "pork"]

item = "carrot"

# Structural pattern matching syntax (Python 3.10+) utilizing 'if' guards
match item:
    case x if x in fruits:
        print(f"{item} is classified as a fruit.")
    case x if x in veggies:
        print(f"{item} is classified as a veggie.")
    case x if x in meat:
        print(f"{item} is classified as a meat product.")
    case _:
        # The wildcard (_) acts as a default catch-all route (equivalent to else)
        print(f"{item} belongs to an unknown food category.")
