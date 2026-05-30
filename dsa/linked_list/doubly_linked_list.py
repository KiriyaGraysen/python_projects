class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
        
def traverseLinkedList(head):
    current_node = head
    while current_node:
        print(current_node.data, end=" -> ")
        
        current_node = current_node.next
    
    print()

def addNode(head, new_node, position):
    if position == 1:
        new_node.next = head
        head.prev = new_node
        
        return new_node
        
    current_node = head
    for _ in range(position - 2):
        if current_node.next is None:
            break
        
        current_node = current_node.next
    
    new_node.next = current_node.next
    new_node.prev = current_node
    
    if current_node.next is not None:
        current_node.next.prev = new_node
        
    current_node.next = new_node
    
    return head

# the only problem when using this is time complexity becomes 0(n)
def linkedListSize(head):
    size = 0
    
    current_node = head
    while current_node:
        size += 1
        current_node = current_node.next
        
    return size

node1 = Node(5)
node2 = Node(23)
node3 = Node(14)
node4 = Node(83)
node5 = Node(56)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node2.prev = node1
node3.prev = node2
node4.prev = node3
node5.prev = node4

node6 = Node(99)

addNode(node1, node6, 3)

traverseLinkedList(node1)

print(linkedListSize(node1))