class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an element to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top element of the stack."""
        if self.is_empty():
            return None  # or raise an exception
        return self.items.pop()

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.items)

def is_valid(s):
    if len(s) <= 1:
        return False

    stack = Stack()

    pairs = {
        ")": "(",
        "]" : "[",
        "}" : "{"
    }

    for char in s:
        if char in pairs:
            # top_element = ""
            # if not stack.is_empty():
            #     top_element = stack.pop()

            top_element = stack.pop() if not stack.is_empty() else ""

            if top_element != pairs[char]:
                return False
        else:
            stack.push(char)
    
    return True

print(is_valid("("))

# --- Solution using python list instead of Stack class ---

def is_valid_2(s):
    if len(s) <= 1:
        return False

    stack = []

    pairs = {
        ")": "(",
        "]" : "[",
        "}" : "{"
    }

    for char in s:
        if char in pairs:
            # top_element = ""
            # if stack:
            #     top_element = stack.pop()

            top_element = stack.pop() if stack else ""

            if top_element != pairs[char]:
                return False
        else:
            stack.append(char)
    
    return True

print(is_valid_2("("))