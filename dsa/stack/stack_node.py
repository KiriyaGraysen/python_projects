class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def push(self, value):
        # Initialize a new node which will hold a value
        new_node = Node(value)
        
        # if head is not empty the value of new_node.next will be the current head
        if self.head:
            new_node.next = self.head
        
        # update the value of head using the object of the new_node
        self.head = new_node
        self.length += 1
        
    def pop(self):
        # check first if the stack is empty
        if self.isEmpty():
            return "The stack is empty. Cannot pop a stack."
            
        popped_node = self.head
        self.head = self.head.next
        self.length -= 1
        
        return popped_node
        
    def peek(self):
        if self.isEmpty():
            return "The stack is empty. No stack to peek."
            
        return self.head.value
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def traverseAndPrint(self):
        current_node = self.head
        
        while current_node:
            print(current_node.value, end=" -> ")
            
            current_node = current_node.next
        print()
        
myStack = Stack()

print(myStack.isEmpty())

myStack.push(45)
myStack.push(34)
myStack.push(21)

print(myStack.peek())
print(myStack.isEmpty())

myStack.pop()

print(myStack.peek())
myStack.traverseAndPrint()