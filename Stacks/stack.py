class Stack:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.values.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.values[-1]

    def isEmpty(self):
        if len(self.values) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.values)

    def printStack(self):
        print(self.values)

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print(my_stack.pop())
print(my_stack.peek())
my_stack.printStack()
print(my_stack.size())
