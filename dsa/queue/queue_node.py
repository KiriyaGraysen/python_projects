class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
        
    def enqueue(self, value):
        # initialize a new node
        new_node = Node(value)
        
        # if there's neither node assigned to front and rear then assign new_node
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
            
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1
        
    def dequeue(self):
        # check if the queue is empty
        if self.isEmpty():
            return "The queue is empty. Cannot dequeue data."
        
        # if dequeue has value/data then proceed
        dequeued_node = self.front
        self.front = dequeued_node.next
        self.length -= 1
        
        # if front is None then change the value of rear to None
        if self.front is None:
            self.rear = None
            
        return dequeued_node.value
        
    def peek(self):
        # check if the queue is empty
        if self.isEmpty():
            return "The queue is empty. Cannot dequeue data."
        
        return self.front.value
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def printQueue(self):
        current_node = self.front
        
        while current_node:
            print(current_node.value, end=" <- ")
            current_node = current_node.next
        
        # we have this to add a new line since we used the end keyword to prevent
        # the code in creating a new line
        print()
        
myQueue = Queue()

print("Is the queue empty?:", myQueue.isEmpty())

myQueue.enqueue(45)
myQueue.enqueue(65)
myQueue.enqueue(29)
myQueue.enqueue(34)
myQueue.enqueue(50)

print("Is the queue empty?:", myQueue.isEmpty())
print("Size:", myQueue.size())

myQueue.printQueue()

myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()

myQueue.printQueue()

print("Value waiting to be dequeue:", myQueue.peek())