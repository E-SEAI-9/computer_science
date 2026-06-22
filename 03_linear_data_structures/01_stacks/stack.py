class Stack:
    def __init__(self):
        self.items = []

    def push(self, new_item):
        self.items.append(new_item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def is_empty(self):
        return self.size() == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def size(self):
        return len(self.items)


students = Stack()
students.push("Jose")
students.push("Garrett")
students.push("Olena")
students.push("Tobias")

removed_student = students.pop()
print(removed_student) # Tobias

print(students.is_empty()) #False

print(students.peek()) # Will return "Olena". Keep in mind, we removed "Tobias" earlier

print(students.size()) # Will return 3