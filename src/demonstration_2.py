"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.

As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.

The Stack class that you will use has been provided to you.
"""
class Stack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)
        #this is a special python method
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"

class QueueTwoStacks:
    def __init__(self):
        # Your code here
        #holds the elements in reversed order
        #when we call dequeue method, we'll pop from this stack
        self.outgoing_stack = Stack()
        #holds the incoming elements in queue
        self.incoming_stack = Stack()

    def enqueue(self, item):
        # Your code here
        self.incoming_stack.push(item)

    def dequeue(self):
        # Your code here
        #we need to check if the outgoing_stack is empty
        #if it is, empty the instack into the outstack in the reverse order
        #otherwise, we just pop from the top of the outstack
        # do reverse operation, emptying contents from incoming into outgoing
        if len(self.outgoing_stack) == 0:
            while len(self.incoming_stack) != 0:
                popped = self.incoming_stack.pop()
                self.outgoing_stack.push(popped)

        return self.outgoing_stack.pop()


q = QueueTwoStacks()
print(q.dequeue())
q.enqueue(3)
q.enqueue(6)
print(q.dequeue())
q.enqueue(7)
q.enqueue(8)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

