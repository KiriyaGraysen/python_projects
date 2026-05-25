class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, value):
        self.queue.append(value)
        
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty. Cannot peek"
        
        self.queue.pop(0)
        
    def isEmpty(self):
        return len(self.queue) == 0
        
    def peek(self):
        if self.isEmpty():
            return "Queue is empty. Cannot peek"
            
        return self.queue[0]
        
    def size(self):
        return len(self.queue)
        
myQueue = Queue()

myQueue.enqueue(45)
myQueue.enqueue(55)
myQueue.enqueue(23)

myQueue.dequeue()

print(myQueue.peek())
print(myQueue.size())

print(myQueue.queue)