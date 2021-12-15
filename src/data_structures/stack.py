class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack = [item] + self.stack

    def pop(self):
        item = self.stack[0]
        self.stack = self.stack[1:]
        return item
    
    def peek(self):
        return self.stack[0]
