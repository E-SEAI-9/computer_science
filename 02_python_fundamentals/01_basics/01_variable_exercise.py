# --- Step 1: Create variables ---
# Assigning different data types: string, integer (whole number), and float (decimal)

name = "Alice" # String (str)
age = 25 # Integer (int)
height = 1.68 # Float (float)

# --- Step 2: Print the variables ---
# Using the print() function to display each variable's value

print(name)
print(age)
print(height)

# --- Step 3: Check the type of the variables ---
# The type() function reveals the data type of the value stored in the variable
print(type(name))
print(type(age))
print(type(height))

# --- Step 4: Casting ---
# Converting the integer 'age' to a string using str() so it can be concatenated
age_str = str(age)

# Combining strings using the '+' operator to print the required sentence
print("My name is " + name + " and I am " + age_str + " years old.")


# --- Step 5: Global Variable (Bonus) ---
# Defining a variable in the global scope (outside of any function)
global_message = "Original global message."

# The 'global' keyword permits us to modify the global variable
# from within this local function scope instead of creating a new local variable.
def modify_global_message():
    global global_message
    global_message = "Modified global message from inside the function!"

# Printing the global variable before calling the function
print(global_message)

# Execute the function to modify the global variable
modify_global_message()

# Printing the global variable after calling the function to show the modification
print(global_message)