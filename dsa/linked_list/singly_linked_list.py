class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def traverseLinkedList(head):
    current_node = head
    
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    
    print()
    
def findMinValue(head):
    minValue = head.data
    current_node = head.next
    
    while current_node:
        if minValue > current_node.data:
            minValue = current_node.data
            
        current_node = current_node.next
        
    return minValue
    
def deleteNode(head, node):
    if head == node:
        return head.next
    
    current_node = head
    while current_node.next and current_node.next != node:
        current_node = current_node.next
        
    if current_node.next is None:
        return head
        
    current_node.next = current_node.next.next
    
    return head
    
def insetNode(head, new_node, nodePosition):
    if nodePosition == 1:
        new_node.next = head
        return new_node
    
    current_node = head
    for _ in range(nodePosition - 2):
        if current_node.next is None:
            break
        
        current_node = current_node.next
        
    new_node.next = current_node.next
    current_node.next = new_node
    
    return head
    
node1 = Node(12)
node2 = Node(82)
node3 = Node(33)
node4 = Node(63)
node5 = Node(36)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
traverseLinkedList(node1)

print(findMinValue(node1))

node1 = deleteNode(node1, node5)
traverseLinkedList(node1)

node6 = Node(83)

insetNode(node1, node6, 3)
traverseLinkedList(node1)