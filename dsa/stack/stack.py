class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, data):
        self.stack.append(data)
        
    def pop(self):
        if self.stack.isEmpty():
            return "The stack is empty!"
        else:
            return self.stack.pop()
        
    def peek(self):
        if self.stack.isEmpty():
            return "The stack is empty!"
        else:
            return self.stack[-1]
            
    def isEmpty(self) -> bool:
        return len(self.stack) == 0
            
    def size(self):
        return len(self.stack)
            
myStack = Stack()

myStack.push(32)
myStack.push(65)

myStack.pop()
myStack.pop()
myStack.pop()

print(myStack.stack)