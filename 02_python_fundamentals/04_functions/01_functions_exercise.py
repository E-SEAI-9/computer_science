# --- Step 1: Sum of List Elements ---
def sum_list(numbers):
    # Initialize an accumulator variable to keep track of the total sum
    total = 0

    # Iterate through each number in the list sequentially
    for num in numbers:
        total += num

    # Return the final accumulated total back to the caller
    return total


# Testing the function
print(sum_list([10, 20, 30, 40]))


# --- Step 2: Repeated Greeting ---
def repeat_greeting(name, times):
    # Using range() to repeat the block of code 'times' number of times
    # The underscore (_) is used as a throwaway variable since we don't need the index
    for _ in range(times):
        print(f"Hello, {name}!")


# Testing the function
repeat_greeting("Alice", 3)


# --- Step 3: Factorial Calculation ---
def factorial(n):
    # Initialize the result variable to 1 (since multiplying by 0 would wipe it out)
    result = 1

    # Loop from 1 up to and including n (range is upper-bound exclusive)
    for i in range(1, n + 1):
        result *= i

    return result


# Testing the function
print(factorial(5))  # Expected outcome: 120 (5 * 4 * 3 * 2 * 1)


# --- Step 4: Fibonacci Sequence Generator ---
def fibonacci(n):
    # Conditional edge-case handling for 0 or negative inputs
    if n <= 0:
        return []
    # If only 1 term is requested, return the starting base sequence element
    elif n == 1:
        return [0]

    # Initialize the list with the first two distinct Fibonacci sequence values
    sequence = [0, 1]

    # Iterate to generate the remaining terms up to the requested 'n' length
    for i in range(2, n):
        # Calculate the next number by summing the two preceding elements
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence


# Testing the function
print(fibonacci(7))  # Expected outcome: [0, 1, 1, 2, 3, 5, 8]


# --- Step 5: Maximum of Two Numbers ---
def max_of_two(a, b):
    # Use an if...else conditional structure to compare values
    if a > b:
        return a
    else:
        return b


# Testing the function
print(max_of_two(14, 27))


# --- Step 6: Print a Pattern with Nested Loops ---
def print_triangle(rows):
    # Outer loop controls the current row position (from row 1 to total rows)
    for i in range(1, rows + 1):
        # Inner loop controls how many asterisks are printed side-by-side in that row
        for j in range(i):
            # Using end="" keeps the print on the same line instead of starting a new one
            print("*", end="")
        # Print an empty line to cleanly shift down to the next row sequence
        print()


# Testing the function
print_triangle(5)
