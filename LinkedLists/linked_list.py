"""A linked list is a data structure of nodes that contain some data and a pointer to the next nodes
Benefits:
    Memory does not have to be contiguous like with arrays
    When a node is added or removed nodes do not need to be shifted
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    current_node = head
    while(current_node):
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("Null")

def findLowestValue(head):
    min_val = head.data
    current_node = head.next
    while(current_node):
        if current_node.data < min_val:
            min_val = current_node.data
        current_node = current_node.next
    return min_val

def deleteSpecificNode(head, nodeToDelete):
    previous_node = None
    current_node = head
    if head == nodeToDelete:
        return head.next

    while(current_node.next and current_node.next != nodeToDelete):
        current_node = current_node.next
    
    if current_node.next is None:
        return head
    current_node.next = current_node.next.next
    
    return head

def insertNode(head, location_node, new_node):
    if location_node == head:
        new_node.next = head
        return new_node

    current_node = head
    while(current_node.next and current_node.next != location_node):
        current_node = current_node.next

    if current_node.next is None:
        current_node.next = new_node
        new_node.next = None
        return head

    current_node.next = new_node
    new_node.next = location_node
    return head
n1 = Node(1)
n2 = Node(2)
n3 = Node(0)
n4 = Node(3)

n1.next = n2
n2.next = n3

head = deleteSpecificNode(n1, n2)
head = insertNode(head, None, n4)
traverseAndPrint(head)
print(findLowestValue(head))
