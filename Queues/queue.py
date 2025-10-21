class Queue:
    def __init__(self):
        self.values = []

    def enqueue(self, value):
        self.values.append(value)

    def dequeue(self):
        if not self.isEmpty():
            return self.values.pop(0)

    def peek(self):
        if not self.isEmpty():
            return self.values[0]

    def isEmpty(self):
        return True if len(self.values) == 0 else False

    def size(self):
        return len(self.values)


my_queue = Queue()
print(my_queue.isEmpty())

my_queue.enqueue(5)
my_queue.enqueue(3)
my_queue.enqueue(6)
print("Current size: " + str(my_queue.size()))

val = my_queue.dequeue()
print("Dequeued: " + str(val))
print("Current size: " + str(my_queue.size()))

val = my_queue.peek()
print("First value: " + str(val))
print("Current size: " + str(my_queue.size()))

print(my_queue.isEmpty())
